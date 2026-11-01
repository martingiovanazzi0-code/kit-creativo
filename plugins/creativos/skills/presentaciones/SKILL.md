---
name: presentaciones
description: Arma presentaciones 16:9 (1920×1080) en HTML y las exporta a PNG, PDF y PPTX con notas del orador, con el sistema visual de cada marca. Pensada para presentaciones de ventas que usan closers en llamada, decks de oferta (programas, precios, bonus) y clases. Usala cuando pidan una presentación, un deck, diapositivas, slides para una llamada, pasar un Miro/documento a slides, o retocar/re-exportar un deck ya hecho. Para slides narradas de un VSL o un webinar (guion dicho frase por frase) usá la skill vsl-chat.
---

# Presentaciones

Fabricás el deck **por código**: un HTML con una `<section class="slide">` por diapositiva,
exportado con Chrome a PNG, PDF y PPTX. La fuente editable es siempre el HTML; el PPTX lleva
cada slide como imagen y las notas para quien presenta en las notas del orador.

**¿Es un VSL o un webinar con guion narrado?** Entonces no es esta skill: usá `vsl-chat`
(narrado frase por frase, muchas slides, sin bullets). Esta es para decks de closer, oferta
y clases, con el estándar "tope de gama".

## Antes de producir: leé esto

1. **La marca**: `marcas/<marca>/marca.md` y `marcas/<marca>/tokens.css`. Paleta, tipografía,
   logo y reglas de copy **ya están decididas**: usalas. Si la marca no tiene carpeta, decilo y
   pedí los datos. Nunca inventes una paleta.
2. **El método**: `references/metodo.md` (orden, criterio slide por slide, oferta y precio,
   testimonios, sistema visual, checklist). Leelo entero la primera vez.
3. **La oferta vigente** (precios, planes, bonus, fechas) **no está en este repo**: pedila o
   leela de la fuente de verdad del cliente. Nunca uses precios de una presentación vieja sin
   confirmarlos.

## Cómo trabajás con la persona

- Español rioplatense, de vos. Directo, sin relleno.
- **Iterativo**: primero el guion (tabla slide por slide), después el diseño, slide por slide.
- Ante una decisión de criterio: **2–3 opciones etiquetadas + recomendación + el porqué**.
- Si te dicen "no me gusta", **preguntá qué específicamente** antes de rehacer.
- Si algo choca con la ficha de la marca o con la oferta vigente (un precio, un plan que no
  existe, una promesa de rentabilidad), **marcalo** antes de ponerlo en una slide.
- Si un dato no está, decí que no está. No lo completes.

## Flujo

1. **Brief.** Para quién es (closer en llamada, webinar, clase), marca, objetivo, material de
   origen (Miro, doc, grabación, deck anterior), oferta vigente y fotos/capturas disponibles.
2. **Guion slide por slide** (título · contenido · visual · nota para quien presenta) con el
   orden del método. Marcá los huecos y las inconsistencias. Esperá el OK si se puede.
3. **Armá el HTML.** Copiá `templates/deck-base.html` a la carpeta de trabajo como
   `deck/presentacion.html`, pegá el `tokens.css` de la marca en el `:root` y reemplazá el
   contenido. Imágenes en `img/` al lado del HTML. Las notas del orador van en el atributo
   `data-notas` de cada `<section>`.
4. **Render:**
   ```bash
   python3 scripts/render.py ruta/presentacion.html --size 1920x1080 --pdf --pptx --prefix Presentacion
   ```
   (`scripts/` está dentro de esta skill: usá la ruta absoluta.) Sale en `out/` al lado del
   HTML. Para rehacer algunas slides: `--slides 4 9` (sin `--pptx`). En Windows: `python` o `py`.
   El PPTX necesita `pip install python-pptx pillow` (Pillow es opcional: achica el archivo
   unas 5 veces). Si no se puede instalar, entregá PNG + PDF y avisá.
5. **Revisá cada PNG** abriéndolo, contra el checklist del método y el de la marca.
6. **Entregá** PDF + PPTX + la lista de huecos y decisiones pendientes. Si hay versiones por
   plan (una por oferta), cada una es un HTML aparte que comparte el CSS.

## Requisitos de la máquina

- Python 3.8+ y Google Chrome (o Edge). `python-pptx` (+ `pillow`) solo para el PPTX.
- Si Chrome está en una ruta rara: variable de entorno `CHROME_PATH`.
- Inter baja de Google Fonts: hace falta internet al renderizar.
