#!/usr/bin/env python3
"""Aplana una foto + su fundido al color de fondo en un solo JPG de slide (1920×1080 por defecto).

Para qué: Chrome, al imprimir a PDF, rompe `mask-image` (la foto que se funde con el fondo
queda con un corte o una línea). Con la foto ya fundida en un JPG, el PDF sale limpio.
Usá el JPG como fondo de la slide (clase .fondo) en lugar de la foto con máscara.

Necesita Pillow: pip install pillow

Ejemplos:
  python3 aplanar_foto.py nico.jpg img/fondos/nico-fondo.jpg                     # foto a la izquierda, fundido hacia la derecha
  python3 aplanar_foto.py evento.jpg img/fondos/evento-fondo.jpg --lado derecha --ancho 0.5
  python3 aplanar_foto.py foto.jpg salida.jpg --fondo "#03060D" --foco 0.3 0.25
"""
import argparse
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("Falta Pillow: corré `pip install pillow`.")


def color(hexa):
    hexa = hexa.lstrip("#")
    return tuple(int(hexa[i:i + 2], 16) for i in (0, 2, 4))


def main():
    p = argparse.ArgumentParser(description="Funde una foto con el color de fondo en un JPG de slide.")
    p.add_argument("foto")
    p.add_argument("salida")
    p.add_argument("--size", default="1920x1080", help="tamaño de la slide (ancho x alto)")
    p.add_argument("--lado", choices=["izquierda", "derecha"], default="izquierda", help="de qué lado va la foto")
    p.add_argument("--ancho", type=float, default=0.45, help="fracción del ancho que ocupa la foto (0–1)")
    p.add_argument("--fundido", type=float, default=0.30, help="fracción de la foto que se funde hacia el fondo (0–1)")
    p.add_argument("--fondo", default="#03060D", help="color de fondo de la marca")
    p.add_argument("--foco", type=float, nargs=2, default=(0.5, 0.3), metavar=("X", "Y"),
                   help="punto de la foto que tiene que quedar a la vista al recortar (0–1)")
    a = p.parse_args()

    W, H = (int(x) for x in a.size.lower().split("x"))
    fw = int(W * a.ancho)
    foto = Image.open(a.foto).convert("RGB")

    # recorte tipo "cover" centrado en el foco
    escala = max(fw / foto.width, H / foto.height)
    foto = foto.resize((round(foto.width * escala), round(foto.height * escala)), Image.LANCZOS)
    x = min(max(int(foto.width * a.foco[0] - fw / 2), 0), foto.width - fw)
    y = min(max(int(foto.height * a.foco[1] - H / 2), 0), foto.height - H)
    foto = foto.crop((x, y, x + fw, y + H))

    # máscara: opaca, y se funde en el borde que da al centro de la slide
    mascara = Image.new("L", (fw, H), 255)
    ancho_fundido = max(int(fw * a.fundido), 1)
    for i in range(ancho_fundido):
        opacidad = 255 - int(255 * ((i + 1) / ancho_fundido) ** 1.4)
        col = fw - ancho_fundido + i if a.lado == "izquierda" else ancho_fundido - 1 - i
        mascara.paste(opacidad, (col, 0, col + 1, H))

    lienzo = Image.new("RGB", (W, H), color(a.fondo))
    lienzo.paste(foto, (0 if a.lado == "izquierda" else W - fw, 0), mascara)
    lienzo.save(a.salida, quality=90)
    print(f"ok  {a.salida}")


if __name__ == "__main__":
    main()
