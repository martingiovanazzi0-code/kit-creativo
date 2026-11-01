# Método: VSL Chat (slides narradas para video de ventas y webinar)

Destilado de armar el **VSL Chat de Método FBC** (2026-10-30 y 2026-10-31, v1 a v4), con el
criterio de Pedro Nestares y de Martín. Los ejemplos son de ese VSL; el método sirve para
cualquier VSL o webinar.

---

## 1. Qué es

Las slides que acompañan un **video de ventas que se manda por chat** (Instagram o WhatsApp)
a quien ya contó su situación. La persona del video habla y la pantalla muestra, slide a slide,
la frase que está diciendo. El CTA no es un link: es **escribir una frase por el mismo chat**
(«quiero mi sesión de auditoría»).

Mismo criterio para **webinars**: guion largo, mucho texto dicho, muchas slides.

**No es** un deck de closer ni de oferta (eso es la skill `presentaciones`, estándar "tope de gama").

---

## 2. El criterio narrado (no negociable)

Pedido de Pedro Nestares al corregir la v1, que era "frase + bullets" y dejaba las transiciones
en el aire (Nico tenía que armar la frase en el momento y el video perdía hilo):

- **Palabra por palabra en el sentido del hilo:** cada slide lleva la frase de ese pasaje del
  guion, completa. Quien habla amplía de palabra, pero nunca tiene que inventar la transición.
- **Conector arriba**: una línea chica, en itálica y en la voz de quien habla, que engancha la
  slide con la anterior ("Y te voy a decir algo que capaz no esperás:"). Debajo, la idea central
  en grande.
- **Más slides, no más texto.** Si una slide tiene dos ideas, son dos slides. 100–130 slides
  para un VSL de ~25 minutos es normal.
- **Sin bullets.** Listas solo donde quien habla enumera de verdad (3 cosas, 4 etapas,
  4 pilares, 5 regalos), y van **numeradas** (01, 02…).
- **Nunca un párrafo en pantalla.** La slide muestra la idea que tiene que quedar.
- **Muy visual pero minimalista:** más texto que imagen, sin tarjetas. La jerarquía la hacen el
  tamaño y el peso de la letra. Una palabra clave en el color de resaltado por slide.
- **Lo que se promete o se garantiza va grande y explicado** (ej.: "GARANTÍA DE 10 DÍAS
  HÁBILES" en mayúscula y dorado, con qué cubre y desde cuándo).

### Cómo partir el guion
1. Leé el guion entero y separalo en **bloques** (cada uno con un nombre corto que aparece
   abajo a la izquierda de sus slides).
2. Dentro de cada bloque, partí en **frases que tienen que quedar**. Cada una es una slide.
3. Marcá dónde una idea **se puede dibujar** (sección 4) y dónde va testimonio, regalo o CTA.
4. Si el guion pide "a cámara" (garantía mirándote a los ojos, por ejemplo), **no lleva slide**.

---

## 3. Estructura en bloques (la del VSL de FBC, 16 bloques)

| # | Bloque | Qué hace | Piezas típicas |
|---|---|---|---|
| 1 | La punta del iceberg | Video privado, "miralo hasta el final", espejo de la situación, el problema no es el que creés | Tag "Video privado", barras que se achican, **iceberg**, "3 cosas que te voy a mostrar", aviso de regalos |
| 2 | Por qué te hablo de esto | Autoridad | Foto de fondo aplanada + 3 datos duros |
| 3 | Lo que hay debajo | Las causas reales | Frases narradas, dato grande |
| 4 | Ganar bien no es saber gestionarte | Romper una creencia | Pictograma de personas (1,42 contra 2,1), dúo de contraste |
| 5 | El dinero se aprende | Caso comparado | Red de una persona contra el punto solo de otra |
| 6 | El orden | El método | Etapas numeradas, montaña cuesta arriba / cuesta abajo |
| 7 | Lo que te frena | **Objeciones** (dudas 1 a N), cada una con su testimonio | Objeción en gris entre comillas + respuesta; captura del testimonio con la línea marcada |
| 8 | Dos caminos | Contraste de decisiones | Dúo apagado / encendido |
| 9 | Cómo trabajamos | Modelo, pilares, plataforma | Pilares numerados, capturas de la plataforma sobre aura |
| 10 | ¿Cuánto sale? | Encuadre del valor (sin prometer rentabilidad) | Calculadora estática como ejemplo |
| 11 | El primer paso | Qué pasa en la sesión | Pasos numerados |
| 12 | Tus regalos | Regalos, uno por slide | Slide grande 🎁 + titular dorado; número fantasma dorado |
| 13 | Mirándote a los ojos | Garantía | **Sin slide**: a cámara |
| 14 | Con total honestidad | Urgencia real | Dos razones numeradas + "la urgencia más grande es la tuya" |
| 15 | Lo que dicen adentro | Prueba social final | Miniaturas de videos de clientes + foto de evento |
| 16 | Tu decisión | Resumen, iceberg de vuelta, garantía, dos caminos, CTA | Iceberg con lo trabajado abajo, garantía grande, CTA dorado |

Los regalos se **anticipan al principio** ("quedate hasta el final, que hay regalos") y se
entregan cerca del final.

---

## 4. Componentes (todos están en `templates/build.py`)

| Función / pieza | Para qué |
|---|---|
| `nar(bloque, conector, idea, sub=…, align=…, size=…)` | La slide base: conector arriba, idea central, una línea de apoyo opcional |
| `objecion(bloque, n, total, objeción, respuesta)` | La frase del lead en gris entre comillas; la respuesta en blanco y azul |
| `iceberg(…)` | Lo que se ve arriba del agua, lo que hay debajo. **El favorito**: abre y cierra el VSL |
| `dots(total, encendidos, columnas)` | Grilla de puntos: "1 de cada 100", "2 horas de las 168 de la semana" |
| `people(n, fracción, color)` | Pictograma de personas con fracción (1,42 contra 2,1 aportantes) |
| `duo(…)` | Dos columnas: lo apagado (gris) contra lo encendido (resaltado) |
| `steps([...])` | Lista numerada, solo cuando se enumera de verdad |
| `SLOPE`, `NETWORK`, `ACCOUNT` | Montaña arriba/abajo · red contra punto solo · cuenta "a tu nombre" con salida tachada |
| `shrink` (barras) | El poder de compra que se achica (ilustrativo, sin cifras) |
| `gift_slide`, `stage` | Regalos: slide grande 🎁 + número fantasma dorado |
| `testimonio(…)` | Frase clave arriba en grande + captura con la línea de donde sale marcada |
| `.gar`, `.cta` | Garantía grande; CTA dorado en pastilla |

**Metáforas visuales: si una idea se puede dibujar, se dibuja.** Dibujo simple y plano, un
solo color encendido contra apagados, y la frase encima.

---

## 5. Testimonios

- **La frase clave arriba, en grande**; abajo, la captura real con **la línea de donde sale
  marcada** (recuadro en el color de resaltado).
- Capturas en **dos piezas** si hace falta (nombre arriba, mensajes abajo) para sacar lo que no
  suma (etiquetas internas, mensajes de más).
- **Teléfonos y datos personales tapados.** Si el testimonio es un video, un frame del video
  con el tramo de tiempo anotado.
- Cada objeción lleva el testimonio que la responde. La persona que encarga el VSL **elige**
  cuáles van; no los elijas solo.
- Siempre la aclaración: "Experiencia individual. Toda inversión conlleva riesgos." (o la que
  defina la marca).

---

## 6. Datos y promesas

- Todo dato del guion se contrasta con la **fuente de verdad del cliente**; si choca, gana la
  fuente más reciente y se avisa (ej.: el guion decía USD 1.200 millones; la fuente, 1.500).
- Nombres que cambian dentro del guion (Sandra / Marta): se unifica y se avisa.
- **Proyecciones solo como ejemplo ilustrativo**, estáticas, con la aclaración de que no es
  una promesa. Nunca prometer rentabilidad.
- Si el guion dice que algo no se puede nombrar (confidencialidad) y el sobreimpreso lo nombra,
  se marca como pendiente.

---

## 7. Exportar a PDF sin que se rompan las capas

Chrome, al imprimir a PDF, rompe dos efectos que en pantalla se ven bien:
- **`mask-image`** (foto que se funde con el fondo): deja un corte o una línea en el borde.
  **Solución:** aplanar foto + degradé en un solo JPG con `scripts/aplanar_foto.py` y usarlo
  como fondo.
- **`box-shadow` con desenfoque** (sombras, brillos): sale como un bloque rectangular.
  **Solución:** no usarlo en piezas que van a PDF; usar un `radial-gradient` (clase `.aura`).
- El grano va como SVG en línea (no como imagen suelta) para que pese poco.

Para verificar, **se mira el PDF**, no el HTML.

---

## 8. Checklist antes de entregar

- [ ] Cada slide sigue una frase del guion; ninguna transición queda en el aire.
- [ ] Conector arriba en las slides narradas; una sola idea por slide.
- [ ] Sin bullets; listas solo numeradas y donde se enumera de verdad.
- [ ] Ningún párrafo en pantalla.
- [ ] Metáforas dibujadas donde la idea se puede dibujar.
- [ ] Objeciones con su testimonio; frase clave arriba y línea marcada; datos personales tapados.
- [ ] Datos contrastados con la fuente; proyecciones como ejemplo; sin promesas de rentabilidad.
- [ ] Dorado solo en lo comercial (regalos, sesión, garantía, CTA).
- [ ] Garantía y CTA grandes y explicados.
- [ ] Revisaste las miniaturas (`?grid=`) y el PDF final, no solo el HTML.
- [ ] Lista de cambios sobre el guion y de huecos pendientes entregada aparte.
