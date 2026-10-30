# Método: carrusel de datos visuales

Destilado de la producción de los carruseles A–H de Método FBC (2026-09 a 2026-10). El que
mejor rindió (E, "¿Querés cobrar dividendos en dólares todos los meses? Agarrá 500 dólares y
hacé esto.") y el segundo (D, "Agarrá tu sueldo y hacé esto") comparten este sistema.
Los ejemplos son de FBC; el método sirve para cualquier marca.

---

## 1. Por qué funciona (lo que hay que preservar)

1. **El hook promete un resultado concreto con un recurso concreto y chico.** No "aprendé a
   invertir": una receta con un monto que el lector se imagina poniendo.
2. **"Hacé esto" promete un paso a paso**, y el carrusel lo cumple: una cosa por slide.
3. **El dato se ve antes de leerse.** Número gigante + gráfico con un tramo encendido: se
   entiende en medio segundo y el texto solo confirma. D tenía solo el número y rindió bien;
   E sumó gráficos minimalistas y rindió mejor.
4. **Nombres tangibles** (McDonald's, Coca-Cola): bajan la sensación de "esto es para expertos".
5. **Una slide para guardar**: el resumen que junta todo en una imagen es lo que se guarda y
   se comparte.
6. **CTA por comentario con palabra clave** ("Comentá DIVIDENDOS") que promete algo más por
   privado. La métrica que importa son los **chats abiertos**, no los likes.
7. **Autoridad antes del contenido**: slide 2 con la persona en un escenario y su trayectoria.

---

## 2. Estructura de 8 slides (plantilla)

| Slide | Función | Contenido | Visual |
|---|---|---|---|
| 1 | **Hook** | Solo el hook. Nada más | Foto de la persona a sangre, cuerpo visible, texto abajo |
| 2 | **Autoridad + puente** | Quién es + instituciones/logros + puente ("Con 4 empresas armás… Al final te digo cómo…") | Foto en escenario/conferencia a sangre + pills |
| 3–6 | **Un ítem por slide** | Label "Paso N de 4" · número héroe · nombre · 1–2 datos | Número gigante + 1 o 2 gráficos en tarjetas |
| 7 | **Resumen guardable** | Título que cierra la promesa del hook + gráfico síntesis + regla para adaptarlo + filtro de criterio | Un gráfico que junta todo |
| 8 | **CTA** | "**Comentá [PALABRA]** y te mando [X] por privado." + disclaimer chico | Texto centrado, CTA en color comercial |

- Carrusel de captación a un evento: 6 slides también funciona (hook · autoridad · problema ·
  costo · solución · tarjeta del evento con fecha, hora y "no queda grabada").
- Remake de uno que rindió: mismas piezas, cambia el hook y el cierre.

---

## 3. Copy

### Hook (slide 1)
- Fórmula: **"¿Querés [resultado concreto y deseable]? Agarrá [recurso concreto] y hacé esto."**
- La pregunta en blanco; **"Agarrá … y hacé esto." en el color de resaltado, en renglón
  propio**, partido en bloques que se lean juntos ("Agarrá 500 dólares / y hacé esto.").
  Nunca dejes "Agarrá" colgando al final del renglón de la pregunta.
- En portada **solo el hook**: sin label, sin logo.

### Ítems (slides 3–6)
- **Un ítem por slide, misma estructura en todas**: el ojo aprende el patrón y desliza más rápido.
- Número héroe = lo que el lector tiene que recordar (US$125, ×150).
- Abajo, solo nombre + 1 o 2 datos. El resto lo cuentan los gráficos.

### Datos (no negociable)
- **Todo dato se verifica** con fuente y fecha antes de producir. Si no se puede verificar,
  se dice; no se inventa.
- **Las sumas cierran**: 125 + 110 + 200 + 65 = 500; 25 + 22 + 40 + 13 = 100.
- Si el copy simplifica algo de forma inexacta, **se corrige con el gráfico, no con más texto**.
  Ej.: el copy decía "se repite cada tres meses"; no era exacto (enero cobra 1, diciembre 3),
  así que el resumen mostró los 12 meses reales.
- Si un dato tiene fecha (cotizaciones, capitalizaciones), imprimí la fecha en la slide y
  avisá que hay que actualizarlo si se publica más de una semana después.
- Marcá las **objeciones previsibles** antes de publicar (montos reales chicos, impuestos,
  supuestos agresivos). No las metas en el carrusel sin consultar.

### Cierre (slides 7 y 8)
- Slide 7: título que cierra la promesa ("Eso te da un cobro en dólares **los 12 meses del
  año.**") + regla para adaptarlo + filtro de criterio.
- Slide 8: "**Comentá [PALABRA EN MAYÚSCULAS]**" en el color comercial, en renglón propio, a
  76px; el resto en blanco. **El CTA no se achica.**
- Disclaimer a **22px, en tarjeta**, más chico que el CTA. El bloque CTA + disclaimer va
  **centrado verticalmente**.
- Sin CTA por comentario: "Seguime para [beneficio]" en el color comercial.

### Tono y cortes
- Frases cortas, de vos.
- **Ninguna palabra suelta al principio o al final de un renglón** ("los / 12 meses" está
  mal). Forzá bloques con `<br>` o `display:block`.

---

## 4. Sistema visual

### Layout (1080 × 1350)
- Márgenes laterales 84px. Label arriba-izquierda (`Paso 1 de 4`), número de slide
  arriba-derecha (`03`).
- Pie: handle a la izquierda + `Deslizá →` a la derecha, en todas menos la última.
- Slides de ítem: contenido arriba (pill → número héroe → nombre) y gráficos en tarjetas
  anclados abajo (`bottom: 180px`).
- Fondo de las slides de texto: glow radial suave + viñeta interior + grano al 6%.

### Tipografía (tamaños probados, Inter)
| Elemento | Tamaño / peso |
|---|---|
| Hook portada | 78–84px / 700, interlineado 1.08 |
| Título de slide | 56–66px / 700 |
| Número héroe | 240px / 800, tracking -0.05em; prefijo ("US$", "×") a 100px en resaltado |
| Nombre del ítem | 66px / 700 |
| Cuerpo | 29–33px / 400, color secundario |
| Labels | 21–23px / 600, MAYÚSCULAS, tracking .24–.32em |
| CTA cierre | 76px / 800 |
| Disclaimer | 22px / 400 |

### Componentes gráficos minimalistas (todos están en la plantilla)
1. **Número héroe**: un solo número enorme por slide.
2. **Barra partida**: barra dividida en tramos proporcionales; **solo el tramo de la slide
   actual se enciende**. Muestra "qué porción del total es esto" sin leer.
3. **Tira de 12 meses**: 12 celdas, los meses relevantes encendidos + una línea de texto que
   lo confirma.
4. **Calendario / matriz de puntos** (resumen): filas = ítems, columnas = meses, punto
   encendido donde aplica + fila de totales que prueba la promesa ("ningún mes en cero").
5. **Tarjeta de ejemplo**: "Ejemplo · con un sueldo de $1.000.000" + el resultado en grande.
6. **Plan agrupado** en tarjetas (Gastar / Guardar / Llegar).
7. **Íconos de personas** llenos/vacíos para comparar cantidades.
8. **Tarjeta de evento**: fecha · hora · en vivo · "no queda grabada".

Reglas:
- **Sin ejes, sin grillas, sin leyendas.** Formas planas, esquinas redondeadas.
- **Un solo color de énfasis** contra apagados. Ganancia/pérdida solo si la marca los define.
- **Máximo 2 gráficos por slide** de ítem, 1 en el resumen.
- **Mismo gráfico en el mismo lugar** en todas las slides de ítem: lo único que cambia es qué
  se enciende. Eso da ritmo y hace que el lector compare.
- El color comercial (dorado en FBC) **nunca** va en gráficos.
- Si un número o una comparación se puede dibujar, dibujalo.

---

## 5. Fotos

- **Portada: la persona con el cuerpo visible** (torso, manos), cara en el tercio superior y
  cuerpo por arriba del texto.
- **Slide 2: en escenario/conferencia** (autoridad).
- Siempre la persona real, nunca stock.
- Evitá: cabezas de terceros tapando, texto de pantallas pegado a la cabeza, repetir la foto
  de portada de otro carrusel, texto encima de la cara.
- **Recorte a sangre**: la foto es más grande que la slide y se posiciona con `left/top`.
  Degradé al fondo desde abajo: transparente hasta ~45–50%, `.6` a ~60%, `.96` a ~75%.
  Sombra suave arriba (`.35–.55` en el primer 15%) si el fondo es claro.
- **Dá 3–4 opciones renderizadas de la portada** y que elija la persona.

---

## 6. Checklist antes de entregar

- [ ] Portada: solo el hook, sin label, sin logo, cuerpo visible, "Agarrá…" en renglón propio.
- [ ] Slide 2: foto de escenario, trayectoria confirmada en la ficha de la marca.
- [ ] Ítems: misma estructura, número héroe, gráficos en el mismo lugar, solo el actual encendido.
- [ ] Datos verificados con fuente y fecha; sumas que cierran.
- [ ] Resumen con un gráfico que prueba la promesa del hook.
- [ ] CTA en color comercial, renglón propio, 76px, sin achicar; disclaimer 22px; bloque centrado.
- [ ] Color comercial solo en el CTA.
- [ ] Sin palabras sueltas al principio o al final de un renglón.
- [ ] Ningún texto pisa una cara.
- [ ] Cambios sobre el copy avisados con el porqué.
- [ ] Revisaste cada PNG abierto, no supusiste.

---

## 7. Correcciones que ya se hicieron (no repetir)

| Corrección |
|---|
| En la portada va **solo el hook**. |
| Slide 2 con el mismo formato que la portada (foto a sangre), con foto de conferencia. |
| Sin logo ni label "Quién te habla" en portada y slide 2. |
| La trayectoria va la que confirma la ficha de la marca, no la que traiga el copy. |
| Todo carrusel cierra con CTA. |
| Portada: **se tiene que ver el cuerpo**. Dar opciones y que elija la persona. |
| "Agarrá 500 dólares y hacé esto" no puede quedar partido con "Agarrá" suelto. |
| Disclaimer más chico; **el CTA no se achica**; bloque final centrado. |
| Dos cajas que dicen lo mismo → se fusionan (el dato pasa a ser encabezado del gráfico). |
