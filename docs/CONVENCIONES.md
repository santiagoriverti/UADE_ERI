# Convenciones

> Reglas concretas para que los doce notebooks se vean y se lean como un solo
> material, y no como doce trabajos distintos. Si vas a escribir o modificar un
> notebook, seguí esto al pie de la letra.
>
> **El ejemplo canónico es [`notebooks/04_unidad_IV_finanzas.ipynb`](../notebooks/04_unidad_IV_finanzas.ipynb).**
> Ante cualquier duda que este documento no resuelva, mirá cómo está resuelto ahí y
> replicalo. Un notebook nuevo que no se parezca a ése está mal, aunque respete cada
> regla de esta página por separado.

---

## 1. Anatomía obligatoria de un notebook

Todo notebook tiene exactamente esta secuencia de secciones. No se saltea ninguna,
no se reordenan.

| # | Sección | Tipo | Contenido |
|---|---|---|---|
| 0 | **Portada** | markdown | Encabezado UADE, número y título de unidad, bibliografía, badge de Colab |
| 1 | **Qué vas a encontrar acá** | markdown | Índice con anclas + un párrafo de hoja de ruta |
| 2 | **Setup** | código | `wget` de `eri_utils`, imports, `estilo_uade()`, `SEMILLA` |
| 3 | **Desarrollo teórico** | md + código | Una sección por tema, alternando teoría y código |
| 4 | **Figuras interactivas** | código | Los widgets de la unidad (pueden ir intercalados en 3) |
| 5 | **Ejercicios resueltos** | md + código | Uno por ejercicio de la guía, con `assert` final |
| 6 | **Síntesis** | markdown | Los cinco o seis resultados que hay que llevarse |
| 7 | **Para seguir** | markdown | Qué se conecta con la unidad siguiente |
| 8 | **Referencias** | markdown | Bibliografía citada, formato APA |

### Portada — plantilla exacta

```markdown
<div align="center">

**UADE — Facultad de Ciencias Económicas**
**Economía del Riesgo y de la Información (1.4.010) — 2.º cuatrimestre 2026**

# Unidad IV — Aplicaciones a las Finanzas

*Notas de Clase 4 · Decisiones de portafolio, Markowitz, CAPM y futuros*

---

Bibliografía: Markowitz (1952) · Sharpe (1964)

</div>
```

### Setup — plantilla exacta

```python
# @title Setup — ejecutá esta celda primero  { display-mode: "form" }
!wget -q -O eri_utils.py https://raw.githubusercontent.com/santiagoriverti/UADE_ERI/main/src/eri_utils.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import eri_utils as eri

eri.estilo_uade()
SEMILLA = 1410
rng = np.random.default_rng(SEMILLA)

print("Listo. eri_utils", eri.__version__)
```

---

## 2. Notación

**La notación de las notas `.tex` manda.** Si hay conflicto entre lo que es prolijo
en Python y lo que dice la nota de clase, gana la nota: el alumno tiene que poder
seguir el notebook con el PDF al lado.

### Símbolos

| Concepto | Notas LaTeX | Python | Observación |
|---|---|---|---|
| Ingreso / riqueza | `y`, `w`, `W` | `y`, `w`, `W` | |
| Utilidad vNM | `v(·)`, `u(·)`, `U(·)` | `u`, `v` | `U` mayúscula solo para utilidad de la firma (U-V) |
| Probabilidad de estado | `π_s` | `pi_s`, `probs` | |
| Peso de decisión (Prospect Theory) | `π(p)` | `peso_decision` | **No** es una probabilidad; nombrarlo distinto |
| Equivalente cierto | `y_c`, `CE` | `CE` | |
| Prima de riesgo | `ρ`, `π(X)` | `prima` | Evitar `pi` acá: colisiona con probabilidad |
| Aversión absoluta | `A(y)`, `r_A` | `r_A` | |
| Aversión relativa | `R(y)`, `r_R` | `r_R` | |
| Media / desvío | `μ`, `σ` | `mu`, `sigma` | |
| Cobertura de seguro | `q` | `q` | |
| Tasa de prima | `p` | `p` | |
| Ponderaciones de cartera | `w` | `w` | Vector numpy |
| Matriz de covarianzas | `Σ` | `Sigma` | Mayúscula |
| Aversión media-varianza | `ρ`, `a` | `rho`, `a` | |

### Colisión a vigilar

`π` se usa en la materia con **tres** significados distintos:

1. probabilidad de un estado (Unidades I–V, Gravelle);
2. peso de decisión de la Teoría de las Perspectivas (Unidad I, Kahneman-Tversky);
3. prima de riesgo (Unidad II, Varian) y beneficio de la firma (Unidad V, Sandmo).

En Python **hay que desambiguar siempre**: `probs`, `peso_decision`, `prima`,
`beneficio`. Nunca `pi` a secas salvo para la probabilidad de siniestro, donde la
nota lo usa sin ambigüedad.

---

## 3. Estilo de markdown

- **Títulos**: `##` para sección, `###` para subsección. El `#` está reservado para
  el título del notebook en la portada.
- **Teoremas, definiciones y proposiciones**: en negrita al inicio del párrafo, sin
  numeración automática. `**Definición (Prospecto).** Un prospecto es…`
- **Cajas «Idea clave»** de las notas → *blockquote* con emoji fijo:
  ```markdown
  > 💡 **Idea clave.** El riesgo agregado de una economía no puede eliminarse,
  > solo repartirse.
  ```
- **Advertencias** → `> ⚠️ **Cuidado.** …`
- **Matemática**: `$…$` en línea y `$$…$$` en bloque. Colab renderiza MathJax sin
  configuración. **No usar** entornos `align`/`equation` con etiquetas: MathJax en
  Colab no numera ecuaciones de forma confiable. Si hay que referenciar una
  expresión, nombrarla en prosa.
- **Tablas**: markdown nativo cuando son estáticas; `pd.DataFrame` cuando salen de
  un cálculo.

---

## 4. Estilo de código

- **PEP 8**, líneas de hasta 88 caracteres.
- **Nombres en español**, salvo la notación matemática de la tabla de arriba.
- **Comentarios que expliquen la economía, no la sintaxis.** Mal:
  `# calcula la media`. Bien: `# valor esperado del prospecto, antes de aplicar u(·)`.
- **Una celda = una idea.** Si una celda hace un cálculo y además grafica, partirla.
- **Salidas legibles**: usar `eri.resaltar("Prima de riesgo", prima)` en vez de
  `print(prima)`, y `eri.tabla(...)` para cualquier cosa tabular.
- **Aleatoriedad**: siempre `rng = np.random.default_rng(SEMILLA)` con
  `SEMILLA = 1410` (por el código de la materia, 1.4.010). Nunca `np.random.seed`.

### Gráficos

```python
fig, ax = eri.figura("Aversión al riesgo", "riqueza $y$", "$v(y)$")
ax.plot(y, v, color=eri.NAVY, label="$v(y)$")
ax.plot([y1, y2], [v1, v2], color=eri.ORO, label="cuerda")
ax.legend()
plt.show()
```

- Curva principal en `eri.NAVY`, elemento contrastado en `eri.ORO`, guías en
  `eri.GRIS` con `linestyle="--"`.
- Rótulos de ejes **siempre**, con notación matemática entre `$…$`.
- Cerrar con `plt.show()` explícito.
- Anotar los puntos que la teoría nombra (`CE`, `E[Y]`, `x*`, `x_c`) con
  `ax.annotate`, no dejarlos implícitos.

---

## 5. Ejercicios

Un ejercicio = un bloque markdown con el enunciado + una o más celdas de código +
un `assert`.

````markdown
### Ejercicio 4 — Equivalente cierto y prima de riesgo

Un individuo con $u(w)=\sqrt{w}$ y riqueza inicial nula enfrenta la lotería
$(0{,}5;\,36,\,100)$.

**(a)** Calcule $E[X]$, $E[u(X)]$, el equivalente cierto y la prima de riesgo.
**(b)** Compare la prima exacta con la aproximación de Pratt.
````

```python
resultados, probs = np.array([36.0, 100.0]), np.array([0.5, 0.5])

E_X = float(probs @ resultados)
EU = eri.utilidad_esperada(eri.u_sqrt, resultados, probs)
CE = eri.equivalente_cierto(eri.u_sqrt, resultados, probs)
prima = E_X - CE

eri.resaltar("E[X]", E_X)
eri.resaltar("E[u(X)]", EU)
eri.resaltar("Equivalente cierto", CE)
eri.resaltar("Prima de riesgo", prima)

assert abs(CE - 64.0) < 1e-6, "El CE debería ser 64"
assert abs(prima - 4.0) < 1e-6, "La prima debería ser 4"
```

Después del cálculo, **siempre** un párrafo de lectura económica del resultado. El
número solo no enseña nada.

---

## 6. Antes de commitear

```bash
python tools/verificar.py          # el módulo sigue reproduciendo la guía (55 checks)
python tools/probar_nb.py --todos  # los notebooks corren limpios; los asserts son el test
python tools/limpiar_notebooks.py  # borrar las salidas
```

Después:

4. Actualizar `docs/ESTADO.md`: el estado de lo que tocaste más una línea en la bitácora.
5. Commit en español, imperativo, **sin atribución de IA**.
6. **`git push origin main`** — sin push, el badge de Colab de ese notebook da 404.

> Si preferís verificar desde Colab en lugar de local, `Entorno de ejecución →
> Reiniciar y ejecutar todo` hace lo mismo que `probar_nb.py` para ese notebook.
> El detalle del ciclo completo está en [`COMO_TRABAJAR.md`](COMO_TRABAJAR.md).
