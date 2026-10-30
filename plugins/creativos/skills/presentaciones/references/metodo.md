# Método: presentación de ventas (y decks en general)

Destilado de armar la presentación de ventas de Método FBC para closers y webinar
(2026-10), con el criterio de Nico Méndez y la referencia del PDF de ventas de Marketing
Ingenioso. Sirve para cualquier deck de oferta; lo general (sección 5 en adelante) sirve para
cualquier presentación.

---

## 1. Para qué existe la presentación

Que **quien presenta muestre siempre lo mismo y en el mismo orden**, sin depender de un Miro
desordenado ni de la memoria. Va **de lo macro a lo micro**: primero la validación (quién,
método, etapas) y después el detalle. **Los detalles suben el valor percibido**: a la gente
le sirve ver cantidad de cosas concretas.

## 2. Orden

1. **Promesa** (portada): qué logra la persona, en una frase.
2. **Autoridad** de la figura principal: primero y como protagonista.
3. **Equipo**: debajo de la figura principal.
4. **Metodología y etapas**.
5. **Modelo: cómo lo llevamos** (contenido · clases · comunidad · contacto).
6. **Plataforma y recursos** (herramientas, plantillas).
7. **Testimonios / casos**.
8. **Programas**: uno por plan, con los entregables de mayor a menor.
9. **Precio, siempre debajo de los entregables.** Mostrarlo antes es un error grave.
10. **Bonus** (si hay), uno por slide, al final.
11. **Por qué ahora** (urgencia real, si existe).

## 3. Criterio slide por slide

- **Personas (figura y equipo): nada de texto corrido.** "No lo va a leer." Solo 3 datos duros
  por persona (cargo, cifra fuerte, institución). La bio larga va en las notas del orador.
- **El dato más fuerte, en grande** (ej.: "gestiona USD 1.500 millones"), no escondido en un párrafo.
- **Lo humano se remarca** si es diferencial (una coach humana, no un bot).
- **Etapas**: solo nombre + objetivo principal de cada una (el tiempo, opcional). El detalle
  lo cuenta quien presenta.
- **Plataforma**: si se muestra en vivo, en la slide va solo el título y lo que hay adentro.
- **Modelo**: 4 pastillas en fila (Contenido · Clases · Comunidad · Contacto), cada una con
  una línea abajo.
- **Recursos**: título + una bajada + 1–2 capturas grandes.
- **Eventos y llamadas en lista escalonada y descriptiva**, no en cajas sueltas.
- **"Próximamente" se borra.** Si no tiene fecha de entrega, no va.
- **Calificación** (ej. 4,8/5): bien marcada, **con fuente** (de cuántas reseñas, de dónde) en
  las notas, para que quien presenta la pueda sostener.

## 4. Oferta, precio y testimonios

### Programa / oferta (una slide por plan)
- Título grande + **bajada en mayúsculas** (qué es, en una línea).
- Lista de entregables con **lo fuerte en negrita**, de mayor a menor: horas de contenido ·
  duración · clases (días, horarios, con quién) · seguimiento 1 a 1 · recursos ·
  actualizaciones permanentes · evento presencial (si tiene fecha).
- El diferencial del plan superior, **marcado aparte** (tarjeta con borde en color comercial).

### Precio
- **Solo el pago único y su equivalente mensual.** Las cuotas, si se muestran, **tachadas con
  una X roja grande** (la gente siempre va a querer cuotas: el ancla es el pago único).
- El precio en el **color comercial** (dorado en FBC), en tarjeta propia, abajo o a la
  derecha de los entregables. "Precio válido solo en esta llamada" debajo, si aplica.
- **Precios siempre de la fuente vigente**, confirmados. Un deck viejo no es fuente.

### Testimonios
- **Nada de capturas de chat sueltas** ("es un revoltijo").
- Formato: **foto de la figura con el alumno + recorrido breve** (con qué dolor y creencia
  entró → qué logró).
- **Ordenados por perfil** (cobró una indemnización, empleado que ahorra X por mes…), así
  quien presenta muestra el caso que se parece al lead. Un caso muy particular no va como
  highlight general.
- Resultados de inversión: **siempre con "rendimientos pasados no garantizan resultados
  futuros"** y nombres tapados. Nunca como resultado esperable.

### Promesas que no se hacen
- No prometer rentabilidad ("mientras aprendés vas generando plata" → "tu plata deja de
  estar quieta desde el día 1").
- Frases tipo "la misma plataforma que Harvard": solo si se pueden respaldar.

---

## 5. Sistema visual (16:9, 1920×1080)

- **Una idea por slide, fondo oscuro, sin texto corrido.**
- Márgenes: 96px arriba/abajo, 120px a los lados. Logo chico arriba a la izquierda (o a la
  derecha si la foto ocupa la izquierda). Número de slide abajo a la derecha, discreto.
- Glow radial suave (su posición cambia por slide con `--gx/--gy` para que no se repita
  igual), viñeta y grano al 6%.
- **Fotos de personas**: a sangre en un lateral con fundido al fondo (mask-image), o en
  tarjeta con radio 22px. El equipo secundario puede ir en blanco y negro para que la figura
  principal resalte.
- **Capturas**: en marco con borde fino, radio 20px y sombra profunda; en celulares, marco de
  teléfono.

### Tipografía (Inter, tamaños probados)
| Elemento | Tamaño / peso |
|---|---|
| Título portada | 100px / 800 |
| Título de slide | 56–64px / 800 |
| Eyebrow (sobre el título) | 22px / 700, MAYÚSCULAS, tracking .16em, color de resaltado |
| Bajada | 30–34px / 500, color secundario |
| Lista | 27–30px, lo fuerte en negrita blanca |
| Dato grande | 60–80px / 900, color de resaltado |
| Título de oferta | 96px / 900 |
| Precio | 112px (en slide de oferta) · 190px (en slide de precio) / 900, color comercial |
| Notas legales | 19px, itálica, color apagado |

### Componentes (todos están en `templates/deck-base.html`)
Portada · autoridad con foto lateral + 4 datos · equipo en tarjetas · etapas en columnas ·
modelo en 4 pastillas · lista + captura · testimonio con foto y recorrido · oferta con
entregables + tarjeta de precio · slide de precio sola con cuotas tachadas · bonus uno por
slide (número fantasma) · cierre centrado.

---

## 6. Checklist antes de entregar

- [ ] Orden macro → micro; precio después de los entregables.
- [ ] Ninguna slide con texto corrido; personas con 3 datos duros.
- [ ] Precios y planes confirmados con la fuente vigente (no con un deck viejo).
- [ ] Cuotas tachadas o ausentes; solo pago único + equivalente mensual.
- [ ] Nada "próximamente" sin fecha.
- [ ] Testimonios con foto + recorrido, aclaración de rendimientos pasados, nombres tapados.
- [ ] Sin promesas de rentabilidad.
- [ ] Color comercial solo en precio, plan superior, bonus y CTA.
- [ ] Notas del orador en `data-notas` donde hacen falta (bios, fuentes, cómo mostrar en vivo).
- [ ] Revisaste cada PNG abierto, no supusiste.
- [ ] Lista de huecos y decisiones pendientes entregada aparte.
