# MAYBEWELL BOOKS — Estructura de Manuscritos

Generado localmente con `pdfplumber`/`pypdf` (sin API key ni LLM), como complemento
del grafo de código en `graphify-out/`. Este archivo cubre lo que Graphify no pudo
procesar sin una key de LLM: el contenido de los dos PDFs de libros.

---

## The Impossible Garden

- **Subtítulo:** Sixty prompts to draw the plants that do not exist
- **Autor / Sello:** Maybewell Books
- **Audiencia:** Creative drawing prompts activity book — all ages
- **Páginas:** 73 · **Palabras:** ~2,501 (~34/página, es un libro de actividades, no de texto corrido)
- **Archivo:** `The Impossible Garden/the-impossible-garden_v1.0_letter.pdf`
- **Nota de serie:** "from the makers of Draw What You Imagine"

### Estructura (6 secciones temáticas, 60 prompts)

| # | Sección | Prompts | Páginas |
|---|---------|---------|---------|
| 1 | Impossible Flowers | #1–10 | 6–15 |
| 2 | Strange Seeds | #11–20 | 17–26 |
| 3 | Trees with Secrets | #21–30 | 28–37 |
| 4 | Gardens of Elsewhere | #31–40 | 39–48 |
| 5 | Green Companions | #41–50 | 50–59 |
| 6 | The Gardener's Notebook | #51–60 | 61–70 |

---

## Draw What You Imagine

- **Subtítulo:** Eighty prompts to spark big ideas / "spark the imagination for anyone who still imagines out loud"
- **Autor / Sello:** Maybewell Books
- **Audiencia:** Creative drawing prompts activity book — ages 6–13
- **Páginas:** 94 · **Palabras:** ~3,262 (~35/página)
- **Archivo:** `Draw What You Imagine/draw-what-you-imagine_v1.1_letter.pdf`

### Estructura (8 secciones temáticas, 80 prompts)

| # | Sección | Prompts | Páginas |
|---|---------|---------|---------|
| 1 | Living Emotions | #1–12 | 6–17 |
| 2 | Impossible Objects | #13–24 | 19–30 |
| 3 | Alternate Worlds | #25–36 | 32–43 |
| 4 | Invented Creatures | #37–48 | 45–56 |
| 5 | Strange Conversations | #49–60 | 58–69 |
| 6 | Body & Senses | #61–72 | 71–82 |
| 7 | Time & Space | #73–80 | 84–91 |

---

## Relación entre los libros

Ambos comparten sello editorial (Maybewell Books), formato (activity book de prompts
de dibujo, tamaño carta), productor de PDF (ReportLab, open source) y estructura
narrativa idéntica: bloques de "N PROMPTS · #inicio–#fin" seguidos de una sección
temática ilustrada. *The Impossible Garden* se presenta explícitamente como
continuación/spin-off de *Draw What You Imagine* ("from the makers of...").

Ambos PDFs fueron generados con la misma librería (ReportLab), lo que sugiere un
pipeline de producción común — probablemente generado por script, no diseñado a mano
en herramientas como InDesign. Si el sitio web (`Website - Repos/maybewell-site-dist-v2`)
tiene código que genera o referencia estos PDFs, ese sería el punto de unión natural
entre el grafo de código y el contenido editorial.
