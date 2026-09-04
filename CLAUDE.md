# UADE_ERI — Instrucciones de proyecto

Repositorio docente de **Economía del Riesgo y de la Información (1.4.010)**, UADE,
Facultad de Ciencias Económicas. A cargo del curso: Santiago Riverti Lavalle
(Jefe de Trabajos Prácticos, 68 h).

## Qué es este proyecto

Un notebook de Jupyter por unidad del programa (I a X) más dos de repaso, pensados
para abrirse **directamente en Google Colab desde los badges del README**. Cada
notebook es autocontenido: contiene toda la teoría de la unidad en markdown/LaTeX,
las figuras de las notas de clase reproducidas con matplotlib, y todos los ejercicios
resueltos y verificados numéricamente.

Doble uso: el alumno lo ejecuta por su cuenta; el docente lo proyecta en clase
compartiendo pantalla.

---

## Arranque de sesión

**Leé estos dos archivos antes de tocar nada:**

1. `docs/ESTADO.md` — qué está hecho, qué falta y cuál es el próximo paso.
2. `docs/CONVENCIONES.md` — notación, estilo y anatomía obligatoria de un notebook.

**Y abrí `notebooks/04_unidad_IV_finanzas.ipynb`**: es el molde. Todo notebook nuevo
debe parecerse a ése en estructura, tono y densidad. No inventes un formato propio.

El resto de la documentación, según la haga falta:

| Archivo | Para qué |
|---|---|
| `docs/COMO_TRABAJAR.md` | Puesta en marcha en una máquina nueva, ciclo de trabajo, troubleshooting |
| `docs/ARQUITECTURA.md` | Estructura del repo y por qué de cada decisión de diseño |
| `docs/CONTEXTO.md` | La materia: cronograma, unidades, bibliografía, régimen |
| `docs/teoria/unidad_*.md` | Resumen técnico de la unidad: qué debe cubrir su notebook, con las figuras, simulaciones y valores esperados de cada ejercicio |
| `tools/README.md` | Qué hace cada script de mantenimiento |

**Al terminar la sesión, actualizá `docs/ESTADO.md`** —estado de lo que tocaste más una
línea en la bitácora— antes de commitear. Es lo que permite retomar el proyecto desde
otra máquina sin contexto previo.

---

## Reglas de trabajo

1. **Idioma**: todo en español rioplatense. Comentarios de código, markdown y nombres
   de variables descriptivos en español, salvo la notación matemática.
2. **Notación**: seguí `docs/CONVENCIONES.md`. Debe coincidir con las notas `.tex`.
   **La notación de las notas manda sobre cualquier convención de Python.** Cuidado
   especial con `π`, que en la materia significa tres cosas distintas.
3. **Fuente de verdad de la teoría**: los `.tex` de `latex/`. Los notebooks los
   transcriben, no los reinterpretan. Para las Unidades VI a X todavía no existen, y
   los `docs/teoria/` correspondientes están marcados como *alcance previsto*.
4. **Código compartido**: cualquier función usada en más de una unidad va a
   `src/eri_utils.py`, nunca duplicada en los notebooks.
5. **Verificación**: todo ejercicio resuelto termina en un `assert` que contrasta el
   resultado numérico contra el valor de la guía de soluciones. Si un `assert` falla,
   el notebook está roto.
6. **Reproducibilidad**: sin descargas de datos en vivo. Los datos van a `data/`
   versionados. Toda simulación aleatoria usa `rng = np.random.default_rng(SEMILLA)`
   con `SEMILLA = 1410`; nunca `np.random.seed`.
7. **Colab primero**: nada de dependencias fuera de las preinstaladas en Colab
   (numpy, pandas, matplotlib, scipy, sympy, ipywidgets). Si hiciera falta otra,
   consultalo antes: cada `pip install` son segundos perdidos al arrancar la clase.
8. **Notebooks limpios**: se commitean siempre con las salidas borradas.
9. **Git**: commits en español, en imperativo. **Nunca** agregar `Co-Authored-By` ni
   ninguna otra atribución de Claude. Todos los commits van únicamente a nombre de
   Santiago Riverti.

---

## Checklist antes de commitear

```bash
python tools/verificar.py          # 55 comprobaciones contra la guía de soluciones
python tools/probar_nb.py --todos  # ejecuta los notebooks; los asserts son el test
python tools/limpiar_notebooks.py  # borra las salidas
```

Después: actualizar `docs/ESTADO.md`, commitear y **`git push origin main`**.

> ⚠️ El push no es opcional. Los badges del README apuntan a `main` en GitHub: un
> notebook que existe solo en local da 404 cuando un alumno lo abre en Colab.

---

## Cuidados particulares de este repositorio

- **`src/eri_utils.py` en `main` es API pública.** Los doce notebooks lo descargan por
  `wget` desde raw.githubusercontent al ejecutarse. Agregar funciones es libre; cambiar
  una firma existente rompe notebooks ya publicados, incluidas las copias que los
  alumnos guardaron en su Drive.
- **No regeneres `data/retornos_ejemplo.csv`.** Los `assert` del notebook de la
  Unidad IV están calibrados contra esos valores exactos.
- **Las decisiones de arquitectura ya están tomadas** (un notebook por unidad, teoría
  completa adentro, datos sintéticos, matplotlib y no Plotly, etc.). Están listadas con
  su fundamento en `docs/ESTADO.md` y `docs/ARQUITECTURA.md`. No las revisites salvo
  que el docente lo pida.
- **Las fechas del cronograma viven en dos lugares y solo dos**: la tabla de mapeo de
  `docs/CONTEXTO.md` y la tabla resumida del `README.md`.
