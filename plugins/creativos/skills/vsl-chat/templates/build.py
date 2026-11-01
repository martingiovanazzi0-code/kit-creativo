#!/usr/bin/env python3
# Arma vsl.html: slides narradas para un VSL o un webinar (1920×1080).
# Uso: python3 build.py   → escribe vsl.html al lado de este archivo.
#
# Se edita ESTE archivo, nunca el HTML. Abajo de todo están las slides (lista S): reemplazá las
# de ejemplo por las del guion usando las funciones de la sección "Piezas".
# Revisión: abrí vsl.html?grid=1-15 (miniaturas, 3 por fila) · vsl.html?s=7 (una sola slide).
# Export:   python3 <skill>/scripts/render.py vsl.html --size 1920x1080 --pdf --prefix VSL
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SALIDA = AQUI / "vsl.html"
TITULO = "VSL"
LOGO = "img/logo.png"   # si no existe, no se muestra

# ============================== CSS ==============================
CSS = """
/* ===== TOKENS DE MARCA (reemplazar por marcas/<marca>/tokens.css; estos son los de Método FBC) ===== */
:root{
  --bg:#03060D; --card:#0C1729; --card2:#0A1224; --line:rgba(111,155,255,.16);
  --glow:rgba(27,52,113,.38); --glow2:rgba(27,52,113,.2); --acc:#4477DC;
  --hi:#6F9BFF; --t1:#FFFFFF; --t2:#9FB0CC; --gold:#F0B429; --up:#34D399; --down:#F87171;
  --font:'Inter';
  /* propios del VSL */
  --zafiro:#1B3471; --medio:#2F58B0; --dim:#4b5c7a; --off:#5d6f8f;
}
@page{size:1920px 1080px;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#000}
body{font-family:var(--font),Arial,sans-serif;color:var(--t1);-webkit-font-smoothing:antialiased}

/* Base minimalista: glow bajo, mucho aire, una idea por slide */
.slide{width:1920px;height:1080px;position:relative;overflow:hidden;background:var(--bg);break-after:page}
.slide::before{content:"";position:absolute;inset:0;pointer-events:none;z-index:1;
  background:radial-gradient(1000px 650px at var(--gx,78%) var(--gy,30%),var(--glow),transparent 70%)}
.slide::after{content:"";position:absolute;inset:0;pointer-events:none;z-index:50;
  background:radial-gradient(ellipse at center,transparent 58%,rgba(0,0,0,.5) 100%),
   url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(%23n)' opacity='.06'/></svg>")}
.slide.c{--gx:50%;--gy:52%}
.slide.l{--gx:28%;--gy:60%}
.in{position:absolute;inset:0;padding:0 180px;z-index:2;display:flex;flex-direction:column;justify-content:center}
.in.center{align-items:center;text-align:center}
.logo{position:absolute;top:64px;left:180px;height:34px;z-index:5;opacity:.85}
.num{position:absolute;bottom:56px;right:180px;font-size:17px;font-weight:600;color:var(--dim);z-index:5;letter-spacing:.12em}
.blk{position:absolute;bottom:56px;left:180px;font-size:17px;font-weight:700;color:var(--dim);z-index:5;letter-spacing:.18em;text-transform:uppercase}

.eyebrow{font-size:22px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--hi);margin-bottom:34px}
h1{font-size:92px;font-weight:800;line-height:1.04;letter-spacing:-.03em}
h2{font-size:72px;font-weight:800;line-height:1.06;letter-spacing:-.025em}
.sub{font-size:36px;color:var(--t2);line-height:1.4;font-weight:500;margin-top:40px;max-width:1300px}
.center .sub{margin-left:auto;margin-right:auto}
.hi{color:var(--hi)} .gold{color:var(--gold)} .muted{color:var(--t2)}
.rule{width:96px;height:4px;background:var(--hi);border-radius:2px;margin:48px 0}
.disc{position:absolute;bottom:100px;left:180px;font-size:19px;color:#6d7f9e;font-style:italic;z-index:5}

/* Narrada: conector en tono de voz, idea central, una línea de apoyo */
.con{font-size:32px;font-style:italic;font-weight:500;color:var(--t2);margin-bottom:28px;max-width:1500px}
.center .con{margin-left:auto;margin-right:auto}
.nar{font-size:80px;font-weight:800;line-height:1.08;letter-spacing:-.028em;max-width:1500px}
.nar.xl{font-size:104px;line-height:1.02;letter-spacing:-.035em}
.nar.md{font-size:66px}
.center .nar{margin-left:auto;margin-right:auto}
.nar .g{color:var(--gold)}
.nar2{font-size:36px;color:#dbe4f3;line-height:1.45;font-weight:500;margin-top:40px;max-width:1300px}
.nar2 b{color:#fff;font-weight:800}
.center .nar2{margin-left:auto;margin-right:auto}

/* Numerados (solo donde se enumera de verdad) */
.steps{display:flex;flex-direction:column;margin-top:44px;border-top:1px solid var(--line)}
.steps .s{display:grid;grid-template-columns:150px 1fr;align-items:baseline;padding:34px 0;border-bottom:1px solid var(--line)}
.steps .k{font-size:30px;font-weight:800;color:var(--hi);letter-spacing:.06em}
.steps .t{font-size:44px;font-weight:700;line-height:1.25}
.steps .t small{display:block;font-size:28px;font-weight:500;color:var(--t2);margin-top:8px}
.steps.g .k{color:var(--gold)}

/* Dúo: apagado contra encendido */
.duo{display:grid;grid-template-columns:1fr 1px 1fr;gap:100px;margin-top:56px}
.duo .bar{background:var(--line)}
.duo .n{font-size:24px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:var(--hi);margin-bottom:18px}
.duo .n.off{color:var(--dim)}
.duo p{font-size:50px;font-weight:800;line-height:1.15;letter-spacing:-.015em}
.duo p.off{color:var(--off)}
.stat{font-size:200px;font-weight:900;line-height:.92;letter-spacing:-.05em;color:var(--hi)}

/* Objeción: lo que te dicen en gris, la respuesta en blanco */
.obj{font-size:76px;font-weight:800;line-height:1.08;letter-spacing:-.025em;color:var(--off)}
.obj::before{content:"“";color:var(--dim)} .obj::after{content:"”";color:var(--dim)}
.ans{font-size:60px;font-weight:800;line-height:1.12;letter-spacing:-.02em}

/* Testimonio: frase clave arriba, captura abajo con la línea marcada */
.pr{position:absolute;inset:0;z-index:2;padding:130px 180px 170px;display:flex;flex-direction:column;justify-content:center}
.pr .hl{font-size:52px;font-weight:800;line-height:1.16;letter-spacing:-.02em;max-width:1520px}
.pr .hl::before{content:"“";color:var(--hi)} .pr .hl::after{content:"”";color:var(--hi)}
.pr .meta{font-size:26px;color:var(--t2);margin-top:20px}
.pr .meta b{color:#fff;font-weight:800}
.shot{position:relative;border-radius:24px;overflow:hidden;border:1px solid rgba(111,155,255,.28);margin-top:46px;align-self:flex-start}
.shot img{display:block;width:100%}
.mark{position:absolute;border:3px solid var(--hi);border-radius:12px;background:rgba(111,155,255,.10)}
.media{margin-top:46px;width:1100px;height:380px;border:2px dashed rgba(111,155,255,.35);border-radius:24px;display:flex;align-items:center;justify-content:center;font-size:24px;color:var(--t2)}

/* Barras que se achican (ilustrativo, sin cifras) */
.shrink{display:flex;align-items:flex-end;gap:60px;height:330px;margin-top:70px}
.shrink div{width:150px;border-radius:14px 14px 0 0;background:linear-gradient(180deg,var(--acc),var(--zafiro));position:relative}
.shrink div span{position:absolute;bottom:-50px;left:0;right:0;text-align:center;font-size:24px;font-weight:700;color:var(--t2)}
.shrink-cap{margin-top:80px;font-size:24px;color:var(--dim);font-weight:600;letter-spacing:.04em}

/* Iceberg: arriba lo que se ve, abajo lo que no */
.ib .ice{position:absolute;inset:0;z-index:1}
.ib .lab{font-size:20px;font-weight:800;letter-spacing:.22em;text-transform:uppercase;color:var(--dim)}
.ib .seen{position:absolute;left:1090px;top:280px;z-index:3}
.ib .seen .t{font-size:56px;font-weight:900;letter-spacing:-.02em;margin-top:10px}
.ib .water{position:absolute;left:0;right:0;top:400px;height:2px;z-index:2;background:linear-gradient(90deg,transparent,rgba(111,155,255,.7) 20%,rgba(111,155,255,.7) 80%,transparent)}
.ib .bot{position:absolute;left:0;right:0;top:480px;text-align:center;z-index:3}
.ib .bot ul{list-style:none;margin-top:34px;display:flex;flex-direction:column;gap:26px;align-items:center}
.ib .bot li{font-size:48px;font-weight:800;line-height:1.15;color:var(--hi)}
.ib .bot li span{color:#fff}
.ib .bot li em{font-style:normal;font-size:24px;font-weight:800;letter-spacing:.14em;color:var(--dim);margin-right:22px;vertical-align:middle}

/* Regalos y cierre */
.emo{font-size:200px;line-height:1;margin-bottom:40px;font-family:'Apple Color Emoji','Segoe UI Emoji','Noto Color Emoji',sans-serif}
.stage{position:absolute;right:150px;top:50%;transform:translateY(-50%);z-index:1;font-size:420px;font-weight:900;line-height:.8;color:rgba(240,180,41,.07);letter-spacing:-.05em}
.stage ~ .in{padding-right:860px}
.gline{margin-top:54px;display:flex;align-items:center;gap:20px;font-size:28px;font-weight:600;color:var(--gold)}
.gicon{width:34px;height:34px;flex:0 0 auto}
.gar{font-size:150px;font-weight:900;line-height:.95;letter-spacing:-.03em;text-transform:uppercase;color:var(--gold)}
.cta{display:inline-block;margin-top:56px;padding:40px 70px;border-radius:999px;border:2px solid var(--gold);background:rgba(240,180,41,.08);font-size:62px;font-weight:900;letter-spacing:-.015em;color:var(--gold)}
.tag{display:inline-flex;align-items:center;gap:16px;padding:16px 30px;border:1.5px solid rgba(111,155,255,.45);border-radius:999px;font-size:22px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--hi);margin-bottom:56px}
.tag i{width:12px;height:12px;border-radius:50%;background:var(--hi);display:block}
/* Aura (en vez de box-shadow, que se rompe en el PDF) detrás de capturas */
.aura{position:absolute;right:110px;top:140px;width:900px;height:800px;z-index:1;background:radial-gradient(closest-side,rgba(68,119,220,.45),rgba(27,52,113,.18) 60%,transparent 100%)}
/* Foto de fondo YA APLANADA con su degradé (scripts/aplanar_foto.py): no usar mask-image */
.fondo{position:absolute;inset:0;z-index:0;background-size:1920px 1080px;background-repeat:no-repeat}
"""

# ============================== Piezas ==============================
GIFT = ('<svg class="gicon" viewBox="0 0 24 24" fill="none" stroke="#F0B429" stroke-width="1.8" stroke-linecap="round" '
        'stroke-linejoin="round"><rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13M19 12v9H5v-9M7.5 8a2.5 2.5 '
        '0 1 1 0-5C11 3 12 8 12 8s1-5 4.5-5a2.5 2.5 0 1 1 0 5"/></svg>')
DISC = '<div class="disc">Experiencia individual. Toda inversión conlleva riesgos.</div>'


def nar(blk, con, head, sub="", align="", size="", extra="", style=""):
    """Slide narrada: conector arriba, idea central, una línea de apoyo. align: '' / 'c' (centro) / 'l'."""
    cls = {"c": "slide c", "l": "slide l"}.get(align, "slide")
    inner = "in center" if align == "c" else "in"
    con_h = f'<div class="con">{con}</div>' if con else ""
    sub_h = f'<p class="nar2">{sub}</p>' if sub else ""
    st = f' style="{style}"' if style else ""
    return (f'<section class="{cls}" data-b="{blk}"{st}><div class="{inner}">{con_h}'
            f'<div class="nar {size}">{head}</div>{sub_h}{extra}</div></section>')


def raw(blk, body, cls="slide", style=""):
    """Slide libre: para piezas que no entran en nar()."""
    st = f' style="{style}"' if style else ""
    return f'<section class="{cls}" data-b="{blk}"{st}>{body}</section>'


def steps(items, gold=False):
    """Lista numerada. items: textos (pueden llevar <small>bajada</small>)."""
    rows = "".join(f'<div class="s"><div class="k">{i:02d}</div><div class="t">{t}</div></div>' for i, t in enumerate(items, 1))
    return f'<div class="steps{" g" if gold else ""}">{rows}</div>'


def duo(lab_a, a, lab_b, b):
    """Dos columnas: a apagado (gris), b encendido."""
    return (f'<div class="duo"><div><div class="n off">{lab_a}</div><p class="off">{a}</p></div>'
            f'<div class="bar"></div><div><div class="n">{lab_b}</div><p>{b}</p></div></div>')


def objecion(blk, n, total, obj, ans):
    """La frase del lead en gris entre comillas; la respuesta abajo."""
    return raw(blk, f'<div class="in"><div class="eyebrow">Duda {n} de {total}</div>'
                    f'<div class="obj">{obj}</div><div class="rule"></div><div class="ans">{ans}</div></div>')


def testimonio(blk, frase, nombre, meta, img="", marks=(), width=1100):
    """Frase clave arriba; captura abajo con la(s) línea(s) marcada(s). marks: (left%, top%, width%, height%)."""
    if img:
        mk = "".join(f'<div class="mark" style="left:{l}%;top:{t}%;width:{w}%;height:{h}%"></div>' for l, t, w, h in marks)
        pieza = f'<div class="shot" style="width:{width}px"><img src="{img}" alt="">{mk}</div>'
    else:
        pieza = '<div class="media">Captura del testimonio (datos personales tapados)</div>'
    return raw(blk, f'<div class="pr"><div class="hl">{frase}</div><div class="meta"><b>{nombre}</b> · {meta}</div>{pieza}</div>{DISC}')


def iceberg(blk, con, seen, lab, items, gid, numerado=False):
    """Iceberg: arriba lo que se ve, abajo la lista de lo que no. gid: 1, 2… (único por slide)."""
    lis = "".join(f'<li><em>{i:02d}</em>{t}</li>' if numerado else f'<li>{t}</li>' for i, t in enumerate(items, 1))
    return raw(blk, f'''
  <svg class="ice" viewBox="0 0 1920 1080" preserveAspectRatio="none" aria-hidden="true">
    <defs>
      <linearGradient id="ig{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2F58B0" stop-opacity=".32"/><stop offset="1" stop-color="#1B3471" stop-opacity="0"/></linearGradient>
      <linearGradient id="it{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6F9BFF" stop-opacity=".10"/><stop offset="1" stop-color="#6F9BFF" stop-opacity=".22"/></linearGradient>
    </defs>
    <polygon points="960,250 880,401 1040,401" fill="url(#it{gid})" stroke="rgba(111,155,255,.35)" stroke-width="1.5"/>
    <polygon points="880,401 1040,401 1360,620 1250,1080 690,1080 540,640" fill="url(#ig{gid})" stroke="rgba(111,155,255,.22)" stroke-width="1.5"/>
  </svg>
  <div class="con" style="position:absolute;left:180px;top:150px;z-index:3">{con}</div>
  <div class="seen"><div class="lab">Lo que se ve</div><div class="t">{seen}</div></div>
  <div class="water"></div>
  <div class="bot"><div class="lab">{lab}</div><ul>{lis}</ul></div>''', cls="slide ib", style="--gx:50%;--gy:78%")


def dots(total, lit, cols, size=34, gap=14, lit_color="#6F9BFF"):
    """Grilla de puntos con algunos encendidos (1 de cada 100, 2 horas de 168)."""
    rows = -(-total // cols)
    w, h = cols * (size + gap), rows * (size + gap)
    c = "".join(f'<circle cx="{(i % cols) * (size + gap) + size / 2}" cy="{(i // cols) * (size + gap) + size / 2}" r="{size / 2}" '
                f'fill="{lit_color if i in lit else "rgba(111,155,255,.13)"}"/>' for i in range(total))
    return f'<svg viewBox="0 0 {w} {h}" style="width:{w}px;height:{h}px">{c}</svg>'


def people(n_full, frac, color, size=96):
    """Pictograma de personas: n completas y una fracción (1,42 · 2,1)."""
    p = '<g{a}><circle cx="24" cy="16" r="12"/><path d="M4 62c0-14 9-24 20-24s20 10 20 24z"/></g>'
    out = []
    for i in range(n_full + (1 if frac else 0)):
        cid = f"cp{color[1:]}{i}"
        if i == n_full and frac:
            body = (f'<clipPath id="{cid}"><rect x="0" y="0" width="{48 * frac}" height="64"/></clipPath>'
                    + p.format(a=' fill="rgba(111,155,255,.12)"') + p.format(a=f' fill="{color}" clip-path="url(#{cid})"'))
        else:
            body = p.format(a=f' fill="{color}"')
        out.append(f'<svg viewBox="0 0 48 64" style="width:{size * .75}px;height:{size}px">{body}</svg>')
    return '<div style="display:flex;gap:18px;align-items:flex-end;margin-top:30px">' + "".join(out) + "</div>"


def shrink(labels=("Hoy", "En 1 año", "En 2 años", "En 3 años"), alturas=(100, 82, 66, 52), cap="Lo que podés comprar con la misma plata. Ilustrativo."):
    bars = "".join(f'<div style="height:{h}%"><span>{l}</span></div>' for l, h in zip(labels, alturas))
    return f'<div class="shrink">{bars}</div><div class="shrink-cap">{cap}</div>'


SLOPE = '''<svg viewBox="0 0 1560 420" style="width:1560px;height:420px;margin-top:40px">
  <defs><linearGradient id="mt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2F58B0" stop-opacity=".35"/><stop offset="1" stop-color="#1B3471" stop-opacity="0"/></linearGradient></defs>
  <polygon points="0,420 780,40 1560,420" fill="url(#mt)" stroke="rgba(111,155,255,.3)" stroke-width="1.5"/>
  <path d="M80 400 L760 70" stroke="#5d6f8f" stroke-width="5" stroke-dasharray="14 12" fill="none"/><circle cx="80" cy="400" r="14" fill="#5d6f8f"/>
  <path d="M800 70 L1480 400" stroke="#6F9BFF" stroke-width="6" fill="none"/><circle cx="1480" cy="400" r="16" fill="#6F9BFF"/>
  <text x="250" y="250" fill="#5d6f8f" font-family="Inter" font-size="34" font-weight="800">Cuesta arriba</text>
  <text x="1130" y="250" fill="#6F9BFF" font-family="Inter" font-size="34" font-weight="800">Cuesta abajo</text>
</svg>'''


def network(solo="SOLO", red="CON RED"):
    """Una persona sola (punto gris) contra una persona con red (punto azul conectado)."""
    return f'''<svg viewBox="0 0 1500 330" style="width:1500px;height:330px;margin-top:30px">
  <circle cx="300" cy="165" r="26" fill="#5d6f8f"/>
  <text x="300" y="250" text-anchor="middle" fill="#5d6f8f" font-family="Inter" font-size="28" font-weight="800">{solo}</text>
  <g stroke="rgba(111,155,255,.45)" stroke-width="3">
    <line x1="1100" y1="165" x2="960" y2="60"/><line x1="1100" y1="165" x2="1240" y2="60"/><line x1="1100" y1="165" x2="930" y2="230"/>
    <line x1="1100" y1="165" x2="1270" y2="230"/><line x1="1100" y1="165" x2="1100" y2="30"/><line x1="960" y1="60" x2="1100" y2="30"/><line x1="1240" y1="60" x2="1100" y2="30"/>
  </g>
  <g fill="rgba(111,155,255,.55)"><circle cx="960" cy="60" r="16"/><circle cx="1240" cy="60" r="16"/><circle cx="930" cy="230" r="16"/><circle cx="1270" cy="230" r="16"/><circle cx="1100" cy="30" r="16"/></g>
  <circle cx="1100" cy="165" r="26" fill="#6F9BFF"/>
  <text x="1100" y="300" text-anchor="middle" fill="#6F9BFF" font-family="Inter" font-size="28" font-weight="800">{red}</text>
</svg>'''


ACCOUNT = '''<svg viewBox="0 0 760 520" style="width:760px;height:520px">
  <rect x="40" y="60" width="520" height="400" rx="34" fill="rgba(27,52,113,.35)" stroke="#6F9BFF" stroke-width="3"/>
  <text x="300" y="130" text-anchor="middle" fill="#9FB0CC" font-family="Inter" font-size="26" font-weight="800" letter-spacing="4">TU CUENTA · A TU NOMBRE</text>
  <g fill="#6F9BFF"><ellipse cx="240" cy="330" rx="70" ry="22"/><ellipse cx="240" cy="300" rx="70" ry="22" opacity=".8"/><ellipse cx="240" cy="270" rx="70" ry="22" opacity=".6"/>
  <ellipse cx="380" cy="330" rx="70" ry="22"/><ellipse cx="380" cy="300" rx="70" ry="22" opacity=".8"/></g>
  <path d="M560 260 L700 260" stroke="#ff6b6b" stroke-width="6" stroke-dasharray="14 10"/><path d="M690 245 l20 15 -20 15" stroke="#ff6b6b" stroke-width="6" fill="none"/>
  <g stroke="#ff6b6b" stroke-width="8" stroke-linecap="round"><line x1="605" y1="215" x2="655" y2="305"/><line x1="655" y1="215" x2="605" y2="305"/></g>
</svg>'''


def gift_slide(blk, linea1, linea2):
    """Slide grande de regalos: 🎁 + titular con la segunda línea en dorado."""
    return raw(blk, '<div style="position:absolute;inset:0;z-index:2;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">'
                    f'<div class="emo">🎁</div><h1 style="font-size:120px;font-weight:900;line-height:1.04">{linea1}<br><span class="gold">{linea2}</span></h1></div>',
               style="--gx:50%;--gy:50%")


def regalo(blk, n, con, nombre, dorado, sub):
    """Un regalo por slide, con el número fantasma dorado a la derecha."""
    return raw(blk, f'<div class="stage">{n:02d}</div><div class="in"><div class="con">{con}</div>'
                    f'<div class="nar">{nombre} <span class="g">{dorado}</span></div><p class="nar2">{sub}</p></div>', cls="slide l")


# ============================== Slides (EJEMPLO: reemplazar por el guion) ==============================
S = []
add = S.append

B = "Apertura"
add(raw("", '<div class="in center"><div class="tag"><i></i>Video privado</div><h1>Este video<br>no es público.</h1>'
            '<p class="sub">Lo grabé para las personas que me escribieron contándome su situación.</p></div>', cls="slide c"))
add(nar(B, "Así que te pido una sola cosa:", 'Miralo con tranquilidad,<br><span class="hi">hasta el final.</span>', align="c", size="xl"))
add(nar(B, "Y sabés que si queda ahí quieta…", '<span class="hi">pierde contra la inflación.</span>', extra=shrink()))
add(nar(B, "Y te voy a decir algo que capaz no esperás:", 'La plata parada<br><span class="hi">no es el problema.</span>', align="c", size="xl"))
add(iceberg(B, "Es la punta de un iceberg:", "Plata parada", "Lo que hay debajo",
            ['<span>Miedo a</span> perderla', '<span>Miedo a</span> no recuperarla', '<span>No entender</span> cómo se mueve'], 1))
add(raw(B, '<div class="in"><div class="con">En los próximos minutos te voy a mostrar tres cosas:</div>'
           + steps(['Qué hay <span class="hi">debajo</span>', 'El <span class="hi">orden</span> para que deje de dar miedo',
                    'Cómo trabajamos, y <span class="hi">qué hacer</span> si es para vos'])
           + f'<div class="gline">{GIFT}Y a lo largo del video te dejo varios regalos: quedate hasta el final.</div></div>'))
add(gift_slide(B, "Quedate hasta el final,", "que hay regalos"))

B = "Metáforas"
add(raw(B, '<div class="in" style="padding-right:900px"><div class="con">Mirá este número:</div>'
           '<div class="nar">1 de cada 100 <span class="hi">lo hace con un plan.</span></div></div>'
           f'<div style="position:absolute;right:170px;top:50%;transform:translateY(-50%);z-index:2">{dots(100, {0}, 10, 40, 16)}</div>', cls="slide l"))
add(raw(B, '<div class="in"><div class="con">Hoy, por cada jubilado:</div><div class="duo">'
           f'<div><div class="n">Aportantes hoy</div><div class="stat" style="font-size:170px">1,42</div>{people(1, .42, "#6F9BFF")}</div><div class="bar"></div>'
           f'<div><div class="n off">Los que harían falta</div><div class="stat" style="color:var(--off);font-size:170px">2,1</div>{people(2, .1, "#5d6f8f")}</div></div></div>'))
add(raw(B, '<div class="in"><div class="con">Con el orden correcto,</div>'
           '<div class="nar md">invertir deja de ser una montaña<br><span class="hi">y pasa a ser lo obvio.</span></div>' + SLOPE + '</div>'))
add(raw(B, '<div class="in"><div class="con">Pensalo con dos personas que arrancan igual:</div>' + network("SOLA", "CON GRUPO")
           + '<p class="nar2">La diferencia no es el talento: <b>es con quién lo hace.</b></p></div>'))
add(raw(B, '<div class="in" style="padding-right:900px"><div class="con">Y lo más importante:</div>'
           '<div class="nar">tu plata queda <span class="hi">siempre a tu nombre.</span></div></div>'
           f'<div style="position:absolute;right:120px;top:50%;transform:translateY(-50%);z-index:2">{ACCOUNT}</div>', cls="slide l"))

B = "Lo que te frena"
add(objecion(B, 1, 3, "Lo más seguro es no moverme.", 'Te entiendo: <span class="hi">es la plata que te costó años juntar.</span>'))
add(testimonio(B, "Ya estoy invirtiendo y entiendo lo que hago.", "Nombre Apellido", "llegó con miedo a invertir"))

B = "Tus regalos"
add(regalo(B, 1, "El primero:", "mi cartera personal,", "<br>en los tres perfiles.", "Conservador, moderado y arriesgado: <b>ves cómo pienso cada decisión.</b>"))

B = "Tu decisión"
add(iceberg(B, "Cuando trabajás lo de abajo, lo de arriba cambia:", "Tu plata, en movimiento", "Lo que trabajamos debajo",
            ["Pilar uno", "Pilar dos", "Pilar tres", "Pilar cuatro"], 2, numerado=True))
add(raw(B, '<div class="in center"><div class="con">Y como confío tanto en lo que armamos:</div>'
           '<div class="gar">Garantía de<br>10 días hábiles</div>'
           '<p class="nar2">Desde que tenés el acceso, tenés 10 días hábiles para ver si es para vos. <b>Si sentís que no, te devolvemos tu dinero.</b></p></div>',
        cls="slide c", style="--gy:55%"))
add(raw(B, '<div class="in"><div class="con">Así que tenés dos caminos:</div>'
           + duo("Camino 1", "Seguir decidiendo por tu cuenta, como hasta ahora.", "Camino 2",
                 'Hacerlo con alguien que <span class="hi">mire tu caso con vos.</span>') + '</div>'))
add(raw(B, '<div class="in center"><div class="con">Si elegís el segundo camino, escribime por donde estuvimos hablando:</div>'
           '<div class="cta">«quiero mi sesión»</div>'
           '<p class="nar2" style="margin-top:60px">Te mando un abrazo. <b>Nos vemos del otro lado.</b></p></div>', cls="slide c", style="--gy:60%"))

# ============================== Salida ==============================
SCRIPT = """<script>
// Logo, nombre del bloque y número en cada slide: se completan solos
document.querySelectorAll('.slide').forEach(function(s,i){
  var logo=document.createElement('img');logo.className='logo';logo.alt='';logo.src='%s';logo.onerror=function(){logo.remove()};s.appendChild(logo);
  if(s.dataset.b){var b=document.createElement('div');b.className='blk';b.textContent=s.dataset.b;s.appendChild(b);}
  var n=document.createElement('div');n.className='num';n.textContent=String(i+1).padStart(2,'0');s.appendChild(n);
});
// ?s=N: una sola slide (así renderiza scripts/render.py) · ?grid=FROM-TO: miniaturas, 3 por fila
var q=location.search, o=q.match(/[?&]s=(\\d+)/), g=q.match(/grid=(\\d+)-(\\d+)/);
if(o)document.querySelectorAll('.slide').forEach(function(s,i){if(i+1!=+o[1])s.remove();});
if(g){document.body.style.cssText='display:grid;grid-template-columns:repeat(3,640px);width:1920px';
  document.querySelectorAll('.slide').forEach(function(s,i){if(i+1<+g[1]||i+1>+g[2])s.remove();else s.style.zoom=1/3;});}
</script>""" % LOGO

html = (f'<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<title>{TITULO}</title>\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=block" rel="stylesheet">\n'
        f'<style>{CSS}</style>\n</head>\n<body>\n' + "\n\n".join(S) + "\n\n" + SCRIPT + "\n</body>\n</html>\n")
SALIDA.write_text(html, encoding="utf-8")
print(len(S), "slides →", SALIDA.name)
