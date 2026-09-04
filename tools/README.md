# Herramientas de mantenimiento

Scripts para trabajar **sobre** el repositorio. Los alumnos no los usan: ellos abren
los notebooks en Colab desde los badges del [README](../README.md).

Requieren las dependencias de mantenimiento:

```bash
pip install -r requirements.txt -r requirements-dev.txt
```

---

## `verificar.py` — el módulo reproduce la guía

```bash
python tools/verificar.py
```

Corre 55 comprobaciones de `src/eri_utils.py` contra los resultados publicados en
`latex/guia_ejercicios_soluciones.tex`. Cada `check` cita el ejercicio del que sale el
valor esperado. Sale con código 1 en la primera falla.

**Cuándo correrlo**: siempre que toques `src/eri_utils.py`.

**Cuando agregues una función** que resuelva un ejercicio de la guía, agregá también su
verificación acá. Es lo que evita que el módulo se desvíe silenciosamente de las notas.

> Nota sobre tolerancias: donde la guía publica un valor redondeado (por ejemplo
> «8,23 %»), el script compara contra el valor **exacto** con tolerancia estrecha y
> deja el número de la guía en un comentario. Comparar contra el redondeo obligaría a
> tolerancias flojas que dejarían pasar errores reales.

---

## `probar_nb.py` — los notebooks corren limpios

```bash
python tools/probar_nb.py notebooks/04_unidad_IV_finanzas.ipynb
python tools/probar_nb.py --todos
python tools/probar_nb.py --todos --saltear-esqueletos
python tools/probar_nb.py notebooks/04_unidad_IV_finanzas.ipynb -v   # con salidas
```

Ejecuta el notebook de punta a punta. **Es el test del repositorio**: como cada
ejercicio cierra con un `assert` contra la solución analítica, «ejecuta limpio»
equivale a «todos los resultados siguen coincidiendo con la guía».

Parchea en memoria la celda de setup para que use `src/` y `data/` locales en lugar de
descargar desde GitHub. Así no necesitás `wget` (que en Windows no viene) y probás la
versión que tenés en el disco, no la ya pusheada.

**Cuándo correrlo**: antes de cada commit que toque un notebook o `eri_utils.py`.

---

## `limpiar_notebooks.py` — borra las salidas

```bash
python tools/limpiar_notebooks.py            # todos los de notebooks/
python tools/limpiar_notebooks.py ruta.ipynb # uno solo
```

Vacía `outputs`, resetea `execution_count` y borra los metadatos que Colab agrega
(`outputId`, `executionInfo`, estado de widgets).

Se versiona el código, no el resultado de ejecutarlo: un notebook con salidas genera
diffs de miles de líneas por un gráfico que cambió un píxel.

**Cuándo correrlo**: siempre, justo antes de commitear.

---

## `nbgen.py` — generar un notebook desde texto plano

```bash
python tools/nbgen.py borrador.nbsrc notebooks/03_unidad_III_reparto_del_riesgo.ipynb --forzar
```

Convierte un archivo de texto con celdas separadas por `#%% md` y `#%% code` en un
`.ipynb`. Cómodo para redactar notebooks largos sin pelear con JSON ni ir y venir del
navegador.

> ⚠️ **El `.ipynb` es la fuente de verdad**, no el `.nbsrc`. Los borradores no se
> versionan (están en `.gitignore`) y regenerar sobre un notebook ya editado pisa esas
> ediciones. Por eso `--forzar` es obligatorio para sobrescribir.

---

## Orden recomendado antes de commitear

```bash
python tools/verificar.py
python tools/probar_nb.py --todos
python tools/limpiar_notebooks.py
```

Después: actualizar `docs/ESTADO.md`, commitear y `git push origin main`.
