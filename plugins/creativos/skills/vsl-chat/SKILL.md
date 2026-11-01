---
name: vsl-chat
description: Arma las slides narradas que acompañan un VSL (video de ventas) o un webinar, a 1920×1080, generadas por código con un build.py y exportadas a PDF/PNG. Es el formato del "VSL Chat": el video que se manda por chat (Instagram o WhatsApp) a quien contó su situación, narrado frase por frase, muy visual, sin bullets, con metáforas dibujadas (iceberg, grilla de puntos, pictogramas), objeciones con testimonios y cierre con CTA por chat. Usala cuando pidan slides para un VSL, un VSL chat, un video de ventas, un webinar narrado, pasar un guion a slides, o retocar uno ya hecho.
---

# VSL Chat: slides narradas para video de ventas y webinar

El guion lo dice la persona a cámara (o en off) y **cada slide muestra la frase de ese
momento**, sin dejar huecos para improvisar. No es un deck de closer (para eso está la skill
`presentaciones`): acá hay muchas slides (100+ es normal), una idea por slide, casi sin
imágenes y con dibujos simples que explican.

## Antes de producir: leé esto

1. **La marca**: `marcas/<marca>/marca.md` y `tokens.css`. Paleta, logo y reglas de copy ya
   están decididos. Si la marca no tiene carpeta, pedí los datos; nunca inventes una paleta.
2. **El método**: `references/metodo.md` (qué es, estructura en bloques, criterio narrado,
   componentes, testimonios, datos, exportación a PDF, checklist). Leelo entero.
3. **El guion** lo trae la persona. Es la fuente: la slide sigue al guion, no al revés.

## Cómo trabajás con la persona

- Español rioplatense, de vos. Directo.
- **Iterativo**: primero la partición del guion en slides, después el diseño por bloques.
- Ante decisiones de criterio: **2–3 opciones + recomendación + el porqué**.
- Si te dicen "no me gusta", **preguntá qué específicamente** antes de rehacer.
- **Cada cambio sobre el guion se avisa con el porqué** (un dato corregido, un nombre que no
  coincide). Si un dato del guion choca con la fuente de verdad del cliente, marcalo.
- Si falta algo (qué testimonio va, qué frase), decí que falta. No lo inventes.

## Flujo

1. **Partí el guion en frases.** Cada frase que tiene que quedar es una slide (o media slide).
   Marcá dónde van metáforas visuales, testimonios, regalos y el CTA. Mostrá la partición.
2. **Copiá `templates/build.py`** a la carpeta de trabajo (por ej. `vsl/deck/build.py`),
   pegá el `tokens.css` de la marca en el bloque `:root` del CSS y reemplazá las slides de
   ejemplo por las del guion, usando las funciones (`nar`, `objecion`, `iceberg`, `dots`…).
   **Se edita el `build.py`, nunca el HTML generado.**
3. **Generá** con `python3 build.py` (sale `vsl.html` al lado). Imágenes en `img/`.
4. **Revisá en miniatura**: abrí `vsl.html?grid=1-15` (y los rangos siguientes) en el
   navegador, o renderizá los PNG. Revisá cada tanda contra el checklist del método.
5. **Exportá**:
   ```bash
   python3 scripts/render.py ruta/vsl.html --size 1920x1080 --pdf --prefix VSL
   ```
   (`scripts/` está dentro de esta skill: usá la ruta absoluta.) El PDF es el entregable; los
   PNG sirven para quien edita el video. Para rehacer slides sueltas: `--slides 12 40`.
6. **Mirá el PDF**, no solo el HTML: Chrome rompe algunos efectos al imprimir (ver método).
7. **Entregá** el PDF + la lista de cambios sobre el guion + los huecos pendientes.

## Requisitos de la máquina

- Python 3.8+ y Google Chrome (o Edge). Para aplanar fotos de fondo: `pip install pillow`.
- Inter baja de Google Fonts: hace falta internet al renderizar.
