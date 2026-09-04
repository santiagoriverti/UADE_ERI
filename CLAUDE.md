# UADE_ERI — Instrucciones de proyecto

Repositorio docente de **Economía del Riesgo y de la Información (1.4.010)**, UADE,
Facultad de Ciencias Económicas. Titular de cátedra a cargo del curso:
Santiago Riverti Lavalle (JTP, 68 h).

## Qué es este proyecto

Un notebook de Jupyter por unidad del programa (I a X) más dos de repaso, pensados
para abrirse **directamente en Google Colab desde los badges del README**. Cada
notebook es autocontenido: contiene toda la teoría de la unidad en markdown/LaTeX,
las figuras de las notas de clase reproducidas con matplotlib, y todos los
ejercicios resueltos y verificados numéricamente.

Doble uso: el alumno lo ejecuta por su cuenta; el docente lo proyecta en clase
compartiendo pantalla.

## Antes de tocar nada, leé

| Archivo | Para qué |
|---|---|
| `docs/ARQUITECTURA.md` | Estructura del repo, decisiones de diseño y por qué |
| `docs/CONTEXTO.md` | La materia: cronograma, unidades, bibliografía, régimen |
| `docs/CONVENCIONES.md` | Anatomía obligatoria de un notebook, notación, estilo |
| `docs/ESTADO.md` | Qué está hecho, qué falta, próximos pasos (handoff) |
| `docs/teoria/unidad_*.md` | Resumen técnico de cada unidad: qué debe cubrir el notebook |

Al terminar una sesión de trabajo, **actualizá `docs/ESTADO.md`** antes de commitear.
Es el archivo que permite retomar el proyecto desde otra máquina sin contexto previo.

## Reglas de trabajo

1. **Idioma**: todo en español rioplatense. Comentarios de código, markdown, nombres
   de variables descriptivos en español donde no colisione con notación matemática.
2. **Notación**: seguí `docs/CONVENCIONES.md`. Debe coincidir con las notas `.tex`.
   La notación de las notas manda sobre cualquier convención de Python.
3. **Código compartido**: cualquier función usada en más de una unidad va a
   `src/eri_utils.py`, nunca duplicada en los notebooks.
4. **Verificación**: todo ejercicio resuelto en un notebook debe terminar en un
   `assert` que contraste el resultado numérico contra el valor de la guía de
   soluciones. Si un `assert` falla, el notebook está roto.
5. **Reproducibilidad**: sin descargas de datos en vivo. Los datos van a `data/`
   versionados. Cualquier simulación aleatoria fija semilla (`SEMILLA = 1410`).
6. **Colab primero**: nada de dependencias fuera de las preinstaladas en Colab
   (numpy, pandas, matplotlib, scipy, sympy, ipywidgets). Si hace falta una más,
   discutirlo antes: cada `pip install` son segundos perdidos al arrancar la clase.
7. **Git**: commits en español, en imperativo. **Nunca** agregar `Co-Authored-By`
   ni ninguna otra atribución de Claude. Todos los commits van únicamente a nombre
   de Santiago Riverti.
8. **Notebooks limpios**: commitear siempre con las salidas borradas
   (`nbstripout` o `Edit > Clear all outputs`). Los outputs inflan el diff y hacen
   ilegible el historial.

## Comandos útiles

Validar que el módulo compartido sigue dando los valores de la guía:

```bash
python tools/verificar.py
```

Limpiar las salidas de todos los notebooks antes de commitear:

```bash
python tools/limpiar_notebooks.py
```
