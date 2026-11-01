---
marca: Método FBC
handle: "@NicoPassini_"
actualizado: 2026-10-30
---

# Método FBC: identidad visual y reglas de marca

**Esto está decidido. No se reinventa en cada pieza.** Si algo de acá choca con lo que pide
el copy, avisá la diferencia y preguntá; no lo resuelvas en silencio.

Los valores para copiar al HTML están en `tokens.css` (misma carpeta). El logo es
`logo-fbc-horizontal.png`.

## Paleta premium (vigente desde 2026-09-11)

| Rol | Hex |
|---|---|
| Fondo base | `#03060D` |
| Tarjeta | `#0C1729` → `#0A1224` (en carrusel: `rgba(12,23,41,.75)`), borde `1px rgba(111,155,255,.18)`, radio 22px |
| Acento zafiro (glow) | `#1B3471` |
| Acento medio (bordes activos) | `#2F58B0` / `#4477DC` |
| Resaltado de texto / ítem activo | `#6F9BFF` |
| Titulares y números | `#FFFFFF` |
| Texto secundario | `#9FB0CC` (nunca blanco al 60%) |
| Dorado, **solo comercial** | `#F0B429` |
| Ganancia (solo en datos) | `#34D399` |
| Pérdida (solo en datos) | `#F87171` |

**Regla del dorado:** únicamente en lo comercial: el CTA ("Comentá…", "Seguime…"), el precio,
el plan más caro, los bonus. Nunca como decoración ni en gráficos. Si aparece en todos lados,
deja de señalar dónde está la oferta.

**Paleta vieja (low ticket, hasta 2026-09):** navy `#0A1526` / royal `#2257F5`. Solo si
alguien la pide para una pieza de entrada.

## Tipografía

**Inter**, de 400 a 900. Titulares 700–900, cuerpo 400–500, datos y labels 600.

## Recursos visuales que siempre van

- Glow radial zafiro **suave** (cambio de temperatura, no una luz): `rgba(27,52,113,.55)`
  arriba a la derecha y `.28` abajo a la izquierda.
- Viñeta interior (`inset 0 0 220px rgba(0,0,0,.7)`).
- Grano al 6%.
- Sin esto la pieza queda plana, con cara de plantilla.

## Fotos

- Siempre Nico Passini, nunca stock. Para este avatar (40–70 años, con capital) la cara es
  la prueba de que "no es humo".
- Las fotos no están en este repo. Pedíselas a quien te encarga la pieza.
- Foto con sol o fondo muy claro: `filter: brightness(.82) saturate(.85)`.

## Carruseles de Instagram

- Formato 1080×1350. Pie: `@NicoPassini_` a la izquierda y `Deslizá →` a la derecha, en
  todas menos la última.
- **Portada:** solo el hook, sin label y sin logo. Nico **con el cuerpo visible** (torso,
  manos), no solo la cara.
- **Slide de autoridad:** foto de Nico en escenario/conferencia a sangre +
  "Soy Nico y hace más de 10 años **estoy dentro de la industria financiera.**" +
  "Trabajando en instituciones como:" + pills.
  - Instituciones confirmadas (2026-10-22): **Banco BBVA · Citibank · Binance · Mercado Libre.**
  - **HSBC NO**: Nico no trabajó ahí.
  - Nunca agregues una institución que no esté en esta lista sin confirmarla.
- **Disclaimer fijo** en contenido de inversión: "Esto no es una recomendación de inversión.
  Depende de tus objetivos, de tus ahorros y de tu factor de riesgo."
- Cierre sin CTA por comentario → "**Seguime para aprender a invertir**" en dorado.

## Copy

- Español rioplatense, de vos. Frases cortas.
- **Nunca prometer rentabilidad.** Un caso real puede ir, siempre con la aclaración de que
  rendimientos pasados no garantizan futuros.
- En presentaciones: **nunca "curso", es "formación".** Si algo no tiene fecha de entrega,
  no se muestra ("próximamente" se borra).

## Chequeo de marca antes de entregar

- [ ] Paleta premium (`#03060D` / `#1B3471`), no la navy/royal vieja.
- [ ] Dorado solo en lo comercial.
- [ ] Secundario en `#9FB0CC`.
- [ ] Glow, viñeta y grano presentes.
- [ ] Los pesos de la tipografía separan las jerarquías.
