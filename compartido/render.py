#!/usr/bin/env python3
"""Renderiza un HTML de slides a PNG (y opcionalmente PDF y PPTX) con Chrome headless.

Funciona en Mac, Windows y Linux. Solo necesita Python 3.8+ y Google Chrome (o Edge).
El PPTX además necesita `pip install python-pptx` (y, si está Pillow, va en JPEG y pesa menos).

Convención del HTML: cada slide es un <section class="slide">. Con `?s=N` el HTML
muestra solo la slide N (1 = la primera). Sin `?s` muestra todas (sirve para el PDF).

Ejemplos:
  python3 render.py carrusel.html                          # todas las slides, 1080x1350
  python3 render.py carrusel.html --slides 1 3 --prefix E  # solo la 1 y la 3 → out/E-01.png, out/E-03.png
  python3 render.py deck.html --size 1920x1080 --pdf --pptx
"""
import argparse
import functools
import html.parser
import http.server
import os
import platform
import shutil
import socketserver
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path


def buscar_chrome():
    """Devuelve la ruta a Chrome/Chromium/Edge. Se puede forzar con la variable CHROME_PATH."""
    env = os.environ.get("CHROME_PATH")
    if env and Path(env).exists():
        return env
    sistema = platform.system()
    candidatos = []
    if sistema == "Darwin":
        candidatos = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "/Applications/Chromium.app/Contents/MacOS/Chromium",
            "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        ]
    elif sistema == "Windows":
        for base in (os.environ.get("PROGRAMFILES"), os.environ.get("PROGRAMFILES(X86)"), os.environ.get("LOCALAPPDATA")):
            if base:
                candidatos += [
                    os.path.join(base, "Google", "Chrome", "Application", "chrome.exe"),
                    os.path.join(base, "Microsoft", "Edge", "Application", "msedge.exe"),
                ]
    for c in candidatos:
        if Path(c).exists():
            return c
    for nombre in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome", "msedge"):
        ruta = shutil.which(nombre)
        if ruta:
            return ruta
    sys.exit("No encontré Chrome. Instalalo o indicá la ruta con la variable CHROME_PATH.")


class _Silencioso(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def levantar_server(carpeta):
    """Sirve la carpeta del HTML por localhost (con file:// Chrome a veces no carga las fuentes de Google)."""
    handler = functools.partial(_Silencioso, directory=str(carpeta))
    server = socketserver.TCPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, server.server_address[1]


def correr_chrome(chrome, args, salida, espera=30):
    """Corre Chrome headless y espera a que el archivo de salida exista y deje de crecer."""
    perfil = tempfile.mkdtemp(prefix="render-chrome-")
    if salida.exists():
        salida.unlink()
    cmd = [chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
           "--no-default-browser-check", f"--user-data-dir={perfil}", "--virtual-time-budget=6000"] + args
    proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    tamanio, limite = -1, time.time() + espera
    while time.time() < limite:
        if salida.exists() and salida.stat().st_size > 0:
            if salida.stat().st_size == tamanio:
                break
            tamanio = salida.stat().st_size
        if proc.poll() is not None and salida.exists():
            break
        time.sleep(0.5)
    if proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
    shutil.rmtree(perfil, ignore_errors=True)
    if not salida.exists() or salida.stat().st_size == 0:
        sys.exit(f"Chrome no generó {salida}. Probá de nuevo o revisá el HTML.")


class _LectorSlides(html.parser.HTMLParser):
    """Cuenta las <section class="slide"> y junta su atributo data-notas (notas del orador)."""

    def __init__(self):
        super().__init__()
        self.notas = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "section" and "slide" in (a.get("class") or "").split():
            self.notas.append(a.get("data-notas") or "")


def armar_pptx(pngs, notas, destino, ancho, alto):
    try:
        from pptx import Presentation
        from pptx.util import Emu
    except ImportError:
        sys.exit("Para el PPTX falta python-pptx: corré `pip install python-pptx` y repetí con --pptx.")
    try:
        from PIL import Image  # opcional: con Pillow las slides van en JPEG y el PPTX pesa ~5 veces menos
    except ImportError:
        Image = None
    prs = Presentation()
    prs.slide_width = Emu(12192000)  # 13,333 in: 16:9
    prs.slide_height = Emu(int(12192000 * alto / ancho))
    tmp = tempfile.mkdtemp(prefix="render-pptx-")
    for png, nota in zip(pngs, notas):
        imagen = png
        if Image:
            imagen = Path(tmp) / (png.stem + ".jpg")
            Image.open(png).convert("RGB").save(imagen, quality=90)
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        slide.shapes.add_picture(str(imagen), 0, 0, prs.slide_width, prs.slide_height)
        if nota:
            slide.notes_slide.notes_text_frame.text = nota
    prs.save(str(destino))
    shutil.rmtree(tmp, ignore_errors=True)


def main():
    p = argparse.ArgumentParser(description="Renderiza slides HTML a PNG/PDF/PPTX con Chrome headless.")
    p.add_argument("html", help="archivo HTML con las <section class=\"slide\">")
    p.add_argument("--size", default="1080x1350", help="ancho x alto en px (carrusel 1080x1350, deck 1920x1080)")
    p.add_argument("--slides", nargs="*", type=int, help="números de slide a renderizar (por defecto, todas)")
    p.add_argument("--out", default="out", help="carpeta de salida, relativa al HTML (por defecto: out)")
    p.add_argument("--prefix", help="prefijo de los PNG (por defecto, el nombre del HTML)")
    p.add_argument("--pdf", action="store_true", help="además genera un PDF con todas las slides")
    p.add_argument("--pptx", action="store_true", help="además genera un PPTX (una imagen por slide + notas)")
    a = p.parse_args()

    html_path = Path(a.html).resolve()
    if not html_path.exists():
        sys.exit(f"No existe {html_path}")
    ancho, alto = (int(x) for x in a.size.lower().split("x"))
    lector = _LectorSlides()
    lector.feed(html_path.read_text(encoding="utf-8"))
    total = len(lector.notas)
    if total == 0:
        sys.exit('El HTML no tiene ninguna <section class="slide">.')
    numeros = a.slides or list(range(1, total + 1))
    fuera = [n for n in numeros if not 1 <= n <= total]
    if fuera:
        sys.exit(f"El HTML tiene {total} slides; no existen: {fuera}")

    salida = (html_path.parent / a.out).resolve()
    salida.mkdir(parents=True, exist_ok=True)
    prefijo = a.prefix or html_path.stem
    chrome = buscar_chrome()
    server, puerto = levantar_server(html_path.parent)
    url = f"http://127.0.0.1:{puerto}/{html_path.name}"

    pngs = []
    try:
        for n in numeros:
            png = salida / f"{prefijo}-{n:02d}.png"
            correr_chrome(chrome, [f"--window-size={ancho},{alto}", f"--screenshot={png}", f"{url}?s={n}"], png)
            pngs.append(png)
            print(f"ok  {png}")
        if a.pdf:
            pdf = salida / f"{prefijo}.pdf"
            correr_chrome(chrome, [f"--print-to-pdf={pdf}", "--no-pdf-header-footer", url], pdf, espera=60)
            print(f"ok  {pdf}")
    finally:
        server.shutdown()

    if a.pptx:
        if len(pngs) != total:
            sys.exit("El PPTX necesita todas las slides: corré sin --slides.")
        pptx = salida / f"{prefijo}.pptx"
        armar_pptx(pngs, lector.notas, pptx, ancho, alto)
        print(f"ok  {pptx}")


if __name__ == "__main__":
    main()
