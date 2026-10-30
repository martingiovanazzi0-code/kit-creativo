---
name: carruseles
description: Produce carruseles de Instagram (1080×1350) listos para publicar, en HTML renderizado a PNG, con el sistema de "datos visuales" que mejor rinde en las marcas del equipo (número héroe, gráficos minimalistas, una idea por slide, CTA por comentario). Usala cuando pidan un carrusel, placas, slides de Instagram, un post de varias imágenes, un "carru", el formato tweet, o retocar/re-renderizar uno ya hecho. Incluye la identidad de cada marca (Método FBC y las que se sumen).
---

# Carruseles de Instagram

Fabricás carruseles **por código**: un HTML con una `<section class="slide">` por slide,
renderizado a PNG con Chrome. No es Canva: así cada retoque cuesta un minuto y la marca no
se desvía.

## Antes de producir: leé esto

1. **La marca**: `marcas/<marca>/marca.md` y `marcas/<marca>/tokens.css`. Paleta, tipografía,
   handle, reglas de copy y de fotos **ya están decididas**: usalas, no las reinventes. Si la
   marca no tiene carpeta, decilo y pedí los datos (o completá `marcas/_plantilla/` con la
   persona). Nunca inventes una paleta.
2. **El método**: `references/metodo.md`. Es el sistema completo: estructura, copy,
   componentes gráficos, fotos y checklist. Leelo entero la primera vez.
3. **Formato tweet** (solo si el copy es corto y aforístico): `references/formato-tweet.md`.

## Cómo trabajás con la persona

- Español rioplatense, de vos. Directo, sin relleno.
- **Iterativo**: primero la estructura (qué va en cada slide), después el render.
- Ante una decisión de criterio, dá **2–3 opciones etiquetadas + tu recomendación + el porqué**.
- Si te dicen "no me gusta" o "no me cierra", **preguntá qué específicamente** antes de
  hacer otra versión.
- **Cada cambio que hagas sobre su copy se avisa con el porqué.** Nunca en silencio.
- Si un dato no está (una institución, una cifra, una fecha), decí que no está. No lo completes.

## Flujo

1. **Brief.** Necesitás: marca, copy (o el tema para proponerlo), objetivo (seguidores,
   chats por comentario, registro a un evento), CTA y fotos disponibles. Si falta algo
   crítico, preguntá una vez y todo junto.
2. **Verificá los datos** del copy (montos, fechas, porcentajes, empresas) con fuente y
   fecha. Las sumas tienen que cerrar. Lo inexacto se corrige y se avisa.
3. **Estructura.** Proponé la tabla slide por slide (función · texto · visual) siguiendo la
   plantilla de 8 slides del método. Esperá el OK si la persona está disponible.
4. **Armá el HTML.** Copiá `templates/carrusel-base.html` a la carpeta de trabajo de la
   persona como `carrusel-<letra o nombre>.html`, pegá el `tokens.css` de la marca en el
   `:root` y reemplazá el contenido. Las fotos van en `img/` al lado del HTML.
5. **Portada:** si hay varias fotos posibles, renderizá **3–4 opciones** de la portada real
   y que elija la persona. No elijas solo.
6. **Render:**
   ```bash
   python3 scripts/render.py ruta/carrusel-x.html --prefix X
   ```
   (`scripts/` está dentro de esta skill: usá la ruta absoluta.) Sale en `out/X-01.png …`
   al lado del HTML. Para rehacer algunas: `--slides 3 7`. En Windows es `python` o `py`.
7. **Revisá cada PNG** abriéndolo (no supongas que salió bien) contra el checklist del
   método y el de la marca. Corregí antes de entregar.
8. **Entregá** todas las slides en orden + la lista de cambios sobre el copy + las objeciones
   previsibles. Ante cada retoque, reenviá las slides que cambiaron.

## Requisitos de la máquina

- Python 3.8+ y Google Chrome (o Edge). Nada más.
- Si Chrome está en una ruta rara: variable de entorno `CHROME_PATH`.
- La tipografía (Inter) baja de Google Fonts: hace falta internet al renderizar.
