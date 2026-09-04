# Arquitectura del proyecto

> Documento de referencia. Explica **cómo está armado** el repositorio y **por qué**
> se tomó cada decisión. Si venís de otra sesión o de otra máquina, leé esto primero
> junto con `ESTADO.md`.

---

## 1. Objetivo

Producir material de cátedra ejecutable para *Economía del Riesgo y de la
Información* (1.4.010, UADE FCE). Un notebook por unidad del programa, abrible en
un clic desde el README de GitHub hacia Google Colab, con:

- **toda la teoría** de la unidad escrita en markdown con LaTeX (Colab renderiza
  MathJax nativamente);
- **las figuras** de las notas de clase reproducidas en matplotlib, algunas con
  controles interactivos;
- **todos los ejercicios** de la guía resueltos paso a paso y verificados
  numéricamente contra la solución analítica.

Dos audiencias simultáneas: el alumno que estudia solo, y el docente que proyecta
el notebook en clase.

---

## 2. Estructura de directorios

```
UADE_ERI/
├── README.md                 Portada: tabla de notebooks con badges de Colab
├── CLAUDE.md                 Instrucciones para agentes de IA que trabajen acá
├── requirements.txt          Dependencias (solo para uso local; Colab ya las trae)
├── .gitignore
│
├── notebooks/                UN NOTEBOOK POR UNIDAD. Es el producto del repo.
│   ├── 01_unidad_I_decisiones_riesgo_incertidumbre.ipynb
│   ├── 02_unidad_II_utilidad_esperada.ipynb
│   ├── 03_unidad_III_reparto_del_riesgo.ipynb
│   ├── 04_unidad_IV_finanzas.ipynb
│   ├── 05_unidad_V_firma_incertidumbre.ipynb
│   ├── 06_unidad_VI_informacion_asimetrica.ipynb
│   ├── 07_unidad_VII_riesgo_moral.ipynb
│   ├── 08_unidad_VIII_seleccion_adversa.ipynb
│   ├── 09_unidad_IX_senalizacion.ipynb
│   ├── 10_unidad_X_subastas.ipynb
│   ├── 11_repaso_parcial_1.ipynb          (Unidades I–V)
│   └── 12_repaso_parcial_2.ipynb          (Unidades VI–X)
│
├── src/
│   └── eri_utils.py          Módulo compartido: estética + funciones transversales
│
├── data/                     Datasets versionados que consumen los notebooks
│   ├── README.md             Diccionario de datos: origen y significado de cada CSV
│   └── retornos_ejemplo.csv
│
├── latex/                    Fuentes .tex de las notas de clase y la guía
│
├── tools/                    Scripts de mantenimiento (no los usa el alumno)
│   ├── verificar.py          Corre eri_utils contra los valores de la guía
│   └── limpiar_notebooks.py  Borra outputs antes de commitear
│
└── docs/                     Memoria del proyecto
    ├── ARQUITECTURA.md       (este archivo)
    ├── CONTEXTO.md           La materia: cronograma, unidades, bibliografía
    ├── CONVENCIONES.md       Anatomía de un notebook, notación, estilo
    ├── ESTADO.md             Handoff: hecho / pendiente / próximos pasos
    └── teoria/
        └── unidad_I.md … unidad_X.md    Resumen técnico por unidad
```

---

## 3. Decisiones de diseño

### 3.1 Un notebook por unidad, no por clase

**Decisión.** Diez notebooks, uno por unidad del programa analítico, más dos de
repaso (uno por parcial). Total: doce.

**Por qué.** El cronograma cambia todos los cuatrimestres (feriados, paros, fechas
de parcial), pero las unidades del programa analítico no. Anclar los archivos a las
unidades hace que el material sobreviva sin renombrar nada. El mapeo a clases del
cronograma vive en `CONTEXTO.md`, que es el único archivo que hay que tocar cuando
cambia el calendario.

Las clases de parcial, recuperatorio y TP no tienen notebook: no hay contenido nuevo
que ejecutar en ellas.

La Unidad X abarca dos clases del cronograma (13 y 14: subastas, y maldición del
ganador más *market design*). Se resuelve con dos secciones dentro del mismo
notebook, no con dos archivos.

### 3.2 Notebooks autocontenidos en teoría, compartidos en código

**Decisión.** La teoría se escribe completa dentro de cada notebook; el código
transversal vive en `src/eri_utils.py` y se descarga en la celda de setup.

**Por qué.** Son dos ejes distintos y conviene tratarlos distinto:

- *La teoría* es lo que el alumno necesita tener delante mientras estudia. Si la
  dejamos afuera, el notebook depende del PDF y deja de servir para estudiar en el
  colectivo. Además, la duplicación teoría-PDF vs teoría-notebook no es un problema
  real: la fuente de verdad es el `.tex` y el notebook lo transcribe una vez.
- *El código* sí sufre con la duplicación: la paleta de colores, la función de
  equivalente cierto o la frontera de Markowitz aparecen en varias unidades. Si se
  copian, un arreglo hay que replicarlo doce veces y las versiones se desincronizan.

**Cómo funciona el setup.** Primera celda de cada notebook:

```python
!wget -q -O eri_utils.py https://raw.githubusercontent.com/santiagoriverti/UADE_ERI/main/src/eri_utils.py
import eri_utils as eri
eri.estilo_uade()
```

Es un `wget` de un archivo de texto, instantáneo, y Colab siempre tiene red. Se
descartó el `pip install git+https://…` porque suma unos veinte segundos al arranque
de cada clase, y se descartó la autonomía total porque multiplica el mantenimiento
por doce.

> **Consecuencia operativa.** `src/eri_utils.py` en `main` es una API pública: los
> notebooks ya publicados apuntan ahí. No se le pueden romper firmas de funciones
> sin revisar los doce notebooks.

### 3.3 Datos sintéticos y versionados, nunca en vivo

**Decisión.** Los números de los ejercicios son los de la guía. El ejemplo empírico
de la Unidad IV usa un CSV versionado en `data/`, no una descarga de mercado.

**Por qué.** Una clase se da una vez y no admite fallas. Una API de precios puede
cambiar de formato, tener *rate limit* o simplemente no responder desde la red de la
facultad; y aunque responda, los resultados cambian cada vez que se ejecuta, lo que
rompe la correspondencia entre lo que dice el notebook y lo que sale en pantalla.
Con datos fijos, el notebook da hoy y en tres años exactamente el mismo número que
la guía de soluciones, y eso es lo que permite el `assert` de verificación.

### 3.4 Verificación por `assert`

Cada ejercicio resuelto cierra con una comprobación explícita:

```python
assert abs(prima - 50.0) < 1e-9, "La prima de riesgo debería ser 50"
```

Es la red de seguridad del repo: si un cambio en `eri_utils.py` rompe un resultado,
el notebook falla al ejecutarse de punta a punta y el error aparece antes de la
clase, no durante. Cumple además una función pedagógica: hace explícito que el
resultado numérico y el analítico deben coincidir.

### 3.5 Interactividad quirúrgica

Matplotlib estático por defecto, con la estética navy/oro de las notas. Se agregan
`ipywidgets` **solo** donde mover un parámetro enseña algo que la figura fija no
puede mostrar:

| Unidad | Widget | Qué se ve al mover |
|---|---|---|
| I | α de Hurwicz | Cómo cambia la acción elegida con el optimismo |
| II | coeficiente de aversión | La brecha entre `E[Y]` y el equivalente cierto |
| III | recargo de la prima `p` | El óptimo alejándose de la línea de certeza |
| IV | correlación ρ | La frontera combándose hacia la izquierda |
| V | σ² y ρ | La oferta rotando y `x*` cayendo bajo `x_c` |

Se descartó Plotly: infla el `.ipynb`, a veces no renderiza en la vista previa de
GitHub, y no aporta nada que la enseñanza necesite.

### 3.6 Los notebooks se commitean sin salidas

Se versiona el código, no el resultado de ejecutarlo. Un notebook con salidas
genera diffs de miles de líneas por un gráfico que cambió un píxel, y vuelve el
historial inservible. `tools/limpiar_notebooks.py` hace la limpieza.

---

## 4. Cómo se abren los notebooks desde el README

Los badges del README apuntan a:

```
https://colab.research.google.com/github/santiagoriverti/UADE_ERI/blob/main/notebooks/<archivo>.ipynb
```

Colab lee el archivo directamente de GitHub y abre una copia efímera en el Drive del
alumno. **No hace falta que el alumno tenga cuenta de GitHub ni clone nada.**

Dos consecuencias a tener presentes:

1. **El notebook tiene que estar pusheado a `main` para que el link funcione.** Un
   notebook que existe solo en local da 404 en Colab.
2. Colab cachea agresivamente. Si un alumno abre el link y ve una versión vieja,
   que use `File > Revert to saved version` o le agregue `?flush_cache=true` a la URL.

---

## 5. Flujo de trabajo típico

```bash
# 1. Editar un notebook (en Colab, o local con Jupyter)
# 2. Verificar que el módulo compartido sigue sano
python tools/verificar.py

# 3. Ejecutar el notebook completo de punta a punta (los asserts son el test)
# 4. Limpiar salidas
python tools/limpiar_notebooks.py

# 5. Actualizar docs/ESTADO.md con lo que se hizo y lo que quedó pendiente
# 6. Commit y push a main (necesario para que los links de Colab anden)
git add -A && git commit -m "Agrega notebook de la Unidad IV" && git push
```
