# Kit creativo

Tres skills de Claude para producir creativos **por código** con el sistema visual de cada marca:

| Skill | Qué hace | Sale |
|---|---|---|
| **carruseles** | Carruseles de Instagram con el sistema de "datos visuales" (número héroe, gráficos minimalistas, una idea por slide, CTA por comentario). Incluye el formato tweet. | PNG 1080×1350 |
| **presentaciones** | Decks 16:9 para closers, oferta y clases, con el orden y el criterio de la presentación de ventas. | PNG 1920×1080 + PDF + PPTX con notas del orador |
| **vsl-chat** | Slides narradas para un VSL o un webinar: el guion frase por frase, muchas slides, sin bullets, con metáforas dibujadas (iceberg, puntos, pictogramas), objeciones con testimonios y CTA por chat. Se generan con un `build.py`. | PDF + PNG 1920×1080 |

Las tres traen la identidad de **Método FBC** (paleta, tipografía, logo, reglas de copy) y una
plantilla para sumar otras marcas.

---

## Instalación

### Opción A · Claude Code (recomendada)

En Claude Code (terminal, app de escritorio o VS Code), escribí:

```
/plugin marketplace add martingiovanazzi0-code/kit-creativo
/plugin install creativos@kit-creativo
```

Reiniciá la sesión. Para traer las mejoras que se vayan subiendo:

```
/plugin marketplace update kit-creativo
```

### Opción B · Claude en la web o en la app de escritorio (chat)

1. Bajá los zips de `dist/` (`carruseles.zip`, `presentaciones.zip`, `vsl-chat.zip`).
2. En claude.ai, en **Configuración**, buscá la sección **Skills** (dentro de Capacidades) y
   subí cada zip. Activalas.

Necesitan la ejecución de código activada. En planes Team/Enterprise, un admin puede
habilitarlas para toda la organización. Cuando haya una versión nueva, se vuelven a subir los zips.

---

## Qué necesita tu compu

- **Python 3.8+** y **Google Chrome** (o Edge). Con eso salen los PNG y el PDF.
- Solo para el PPTX: `pip install python-pptx pillow`. Para aplanar fotos de fondo del VSL: `pip install pillow`.
- Internet al renderizar (la tipografía Inter baja de Google Fonts).
- Si Chrome está instalado en una ruta rara: definí la variable `CHROME_PATH`.

Funciona en Mac y Windows (en Windows el comando es `python` o `py` en vez de `python3`).

---

## Cómo se usa

Pedíselo a Claude normalmente; la skill se activa sola. Ejemplos:

- *"Armame un carrusel para FBC con este copy: …"*
- *"Necesito un carrusel de captación para la clase del domingo, 6 slides, CTA Comentá MAPA."*
- *"Pasá este Miro a una presentación de ventas para closers, con notas para cada slide."*
- *"Pasame este guion de VSL a slides narradas, como el VSL Chat."*
- *"Retocá la slide 3 del carrusel H y volvé a renderizarla."*

Cómo trabaja: lee la ficha de la marca → verifica los datos → te propone la estructura slide
por slide → arma el HTML → renderiza → revisa cada imagen contra el checklist → te entrega
los archivos y la lista de cambios que hizo sobre tu copy.

**Lo que tenés que darle vos:** el copy (o el tema), las fotos y, para presentaciones de
venta, la oferta vigente (precios, planes, bonus). Nada de eso está en este repo a propósito.

---

## Sumar o actualizar una marca

1. Copiá `compartido/marcas/_plantilla/` como `compartido/marcas/<marca>/`.
2. Completá `marca.md` y armá un `tokens.css` con las mismas variables que el de `metodo-fbc`
   (así las plantillas funcionan sin tocarlas). Sumá el logo.
3. Corré `python3 tools/build.py` (copia las marcas dentro de cada skill y regenera los zips).
4. Commit + push. El equipo actualiza con `/plugin marketplace update kit-creativo`.

Hoy solo está cargada **Método FBC**. Sin Límites falta: no hay paleta ni tipografía
documentadas todavía.

---

## Estructura

```
.claude-plugin/marketplace.json     ← catálogo (lo lee /plugin marketplace add)
plugins/creativos/
  .claude-plugin/plugin.json
  skills/
    carruseles/      SKILL.md · references/ · templates/ · scripts/ · marcas/
    presentaciones/  SKILL.md · references/ · templates/ · scripts/ · marcas/
    vsl-chat/        SKILL.md · references/ · templates/build.py · scripts/ · marcas/
compartido/          ← FUENTE de los scripts (render, aplanar_foto) y de las marcas (editá acá, no adentro de las skills)
tools/build.py       ← sincroniza compartido/ → skills y arma dist/*.zip
dist/                ← zips para subir en claude.ai
```

**Regla de mantenimiento:** `scripts/` y `marcas/` adentro de cada skill son copias. Se edita
en `compartido/` y se corre `tools/build.py` antes de commitear.

---

## Qué NO hay en este repo (a propósito)

- Fotos de las personas de las marcas.
- Precios, planes y bonus: cambian seguido y se toman siempre de la fuente vigente.
- Presentaciones, carruseles o VSL terminados de clientes (guiones, testimonios, capturas).
