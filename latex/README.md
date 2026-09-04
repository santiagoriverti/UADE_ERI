# Fuentes LaTeX

Notas de clase y guías de ejercicios de la materia, en su formato original. **Son la
fuente de verdad de la teoría**: los notebooks las transcriben, no las reinterpretan.

## Archivos esperados

| Archivo | Contenido | Estado |
|---|---|---|
| `cronograma.tex` | Cronograma y programa analítico 2.º C 2026 | ⏳ falta copiar |
| `clase_01_unidad_I.tex` | Unidad I — Decisiones bajo riesgo e incertidumbre | ⏳ falta copiar |
| `clase_02_unidad_II.tex` | Unidad II — Utilidad esperada y aversión al riesgo | ⏳ falta copiar |
| `clase_03_unidad_III.tex` | Unidad III — Reparto óptimo del riesgo | ⏳ falta copiar |
| `clase_04_unidad_IV.tex` | Unidad IV — Aplicaciones a las finanzas | ⏳ falta copiar |
| `clase_05_unidad_V.tex` | Unidad V — La firma competitiva bajo incertidumbre | ⏳ falta copiar |
| `guia_ejercicios_soluciones.tex` | Guía de ejercicios resueltos, Clases 1 a 5 | ⏳ falta copiar |
| `clase_09_unidad_VI.tex` … `clase_13_unidad_X.tex` | Unidades VI a X | ❌ sin redactar |

## Cómo compilar

Todos los documentos compilan con **pdfLaTeX** sin paquetes externos ni imágenes: las
figuras son TikZ/pgfplots. Dos pasadas si el documento tiene índice.

```bash
pdflatex clase_01_unidad_I.tex
```

La única excepción es `cronograma.tex`, que incluye `logo_uade.png`.

## Convención de estilo

Color `NavyBlue` RGB(0,64,128) para títulos y curvas principales, `Gold`
RGB(176,132,28) para el elemento contrastado, y cajas `\ideaclave{}` sobre fondo gris.
Los notebooks replican esa paleta vía `eri.NAVY` y `eri.ORO`.

> Los productos de compilación (`.aux`, `.log`, `.pdf`, etc.) están en `.gitignore`.
> Solo se versionan los `.tex`.
