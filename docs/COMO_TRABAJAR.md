# Cómo trabajar en este proyecto

> **Guía de arranque.** Si estás en una máquina nueva, o retomando el proyecto después
> de un tiempo, empezá por acá. Al terminar esta página tenés el entorno andando y
> sabés exactamente cuál es el próximo paso.
>
> Para **usar** los notebooks no hace falta nada de esto: se abren desde el
> [README](../README.md) con un clic. Esto es para *mantener* el repositorio.

---

## 1. Arranque en una máquina nueva

### Requisitos

- **Python 3.10 o superior** (probado en 3.14). Verificá con `python --version`.
- **Git**.
- Opcional: LaTeX (TeX Live o MiKTeX) si vas a compilar los `.tex` de `latex/`.

### Puesta en marcha

```bash
git clone https://github.com/santiagoriverti/UADE_ERI.git
cd UADE_ERI
python -m venv .venv
```

Activar el entorno virtual — en Windows con PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

En macOS o Linux:

```bash
source .venv/bin/activate
```

Instalar dependencias (las de uso y las de mantenimiento):

```bash
pip install -r requirements.txt -r requirements-dev.txt
```

### Verificación de que todo funciona

Tres comandos, en este orden. Si los tres pasan, el entorno está sano.

```bash
python tools/verificar.py
```

Debe terminar con `55 verificaciones, todas correctas.` Contrasta `src/eri_utils.py`
contra los valores publicados en la guía de soluciones.

```bash
python tools/probar_nb.py --todos
```

Debe terminar con `Todos los notebooks ejecutados corren limpios.` Ejecuta cada
notebook de punta a punta; los `assert` de los ejercicios son el test real.

```bash
git config user.name && git config user.email
```

Debe decir `Santiago Riverti` y `santiagoriverti@gmail.com`. Si no, configuralo:

```bash
git config user.name "Santiago Riverti"
```

### Si algo falla

| Síntoma | Causa probable | Solución |
|---|---|---|
| `ModuleNotFoundError: nbclient` | Falta instalar las dependencias de mantenimiento | `pip install -r requirements-dev.txt` |
| `probar_nb.py` cuelga o da timeout | El kernel no arranca | `python -m ipykernel install --user` |
| `verificar.py` falla en Arrow-Pratt | Se tocó el paso de las diferencias finitas | Ver la nota en `arrow_pratt_absoluta`: el paso es **relativo**, no absoluto |
| Diffs enormes en `.ipynb` sin haber cambiado nada | Finales de línea, o salidas sin limpiar | `.gitattributes` normaliza a LF; correr `python tools/limpiar_notebooks.py` |
| Un badge de Colab da 404 | El notebook no está pusheado a `main` | `git push origin main` |

---

## 2. Orientación: qué leer y en qué orden

Si es tu primera vez —o la primera vez de un agente de IA— en este repositorio:

| Orden | Documento | Qué te da |
|---|---|---|
| 1 | [`ESTADO.md`](ESTADO.md) | Qué está hecho, qué falta, cuál es el próximo paso |
| 2 | [`ARQUITECTURA.md`](ARQUITECTURA.md) | Cómo está armado el repo y **por qué** cada decisión |
| 3 | [`CONTEXTO.md`](CONTEXTO.md) | La materia: cronograma, unidades, bibliografía |
| 4 | [`CONVENCIONES.md`](CONVENCIONES.md) | Notación, estilo y anatomía de un notebook |
| 5 | `teoria/unidad_*.md` | Resumen técnico de la unidad sobre la que vayas a trabajar |
| 6 | [`../CLAUDE.md`](../CLAUDE.md) | Reglas de trabajo, si vas a usar un agente de IA |

Y sobre todo: **abrí `notebooks/04_unidad_IV_finanzas.ipynb`**. Es el molde. Cualquier
notebook nuevo debe parecerse a ése en estructura, tono y densidad.

---

## 3. El ciclo de trabajo

### Desarrollar un notebook nuevo

El caso típico: tomar una unidad que está en esqueleto y desarrollarla.

**Paso 1 — Leer la fuente.** El `docs/teoria/unidad_*.md` correspondiente ya tiene
listadas las figuras a reproducir, las simulaciones a hacer, los ejercicios con sus
valores esperados, y las funciones que habría que agregar a `eri_utils`. La nota
`.tex` de `latex/` es la fuente de verdad de la teoría.

**Paso 2 — Agregar a `eri_utils` lo que falte.** Cualquier función que vaya a usarse
en más de una unidad va al módulo compartido, no al notebook. Agregar también su
verificación en `tools/verificar.py`.

**Paso 3 — Escribir el notebook.** Dos caminos, ambos válidos:

- *Directo en Colab*: abrís el esqueleto desde el badge del README, lo desarrollás y
  después `Archivo → Descargar → .ipynb`, lo reemplazás en `notebooks/`.
- *Local con `nbgen`*: escribís un borrador `.nbsrc` en texto plano (celdas separadas
  por `#%% md` y `#%% code`) y lo convertís. Es más cómodo para notebooks largos:

  ```bash
  python tools/nbgen.py borrador.nbsrc notebooks/03_unidad_III_reparto_del_riesgo.ipynb --forzar
  ```

  Los `.nbsrc` **no se versionan**: una vez generado, el `.ipynb` es el archivo canónico.

**Paso 4 — Probarlo.**

```bash
python tools/probar_nb.py notebooks/03_unidad_III_reparto_del_riesgo.ipynb -v
```

**Paso 5 — Checklist previo al commit.** Los cinco siempre:

```bash
python tools/verificar.py                  # 1. el módulo sigue reproduciendo la guía
python tools/probar_nb.py --todos          # 2. ningún notebook se rompió
python tools/limpiar_notebooks.py          # 3. borrar las salidas
```

4. Actualizar [`ESTADO.md`](ESTADO.md): el estado del notebook y una línea en la bitácora.
5. Commit en español, en imperativo, **sin atribución de IA**, y `git push origin main`.

> ⚠️ El push no es opcional. Los badges del README apuntan a `main` en GitHub: un
> notebook que existe solo en tu disco da 404 cuando un alumno lo abre.

### Modificar `eri_utils.py`

`src/eri_utils.py` en `main` es **API pública**: los doce notebooks lo descargan desde
raw.githubusercontent al ejecutarse en Colab. Consecuencias:

- Agregar funciones es libre.
- **Cambiar la firma o el comportamiento de una función existente rompe notebooks ya
  publicados**, incluida la copia que un alumno guardó en su Drive. Antes de hacerlo,
  corré `python tools/probar_nb.py --todos`.
- Cada función nueva que resuelva un ejercicio de la guía debería tener su
  verificación en `tools/verificar.py`.

### Actualizar el cronograma para un cuatrimestre nuevo

Las fechas están en **dos lugares y solo dos**: la tabla de mapeo de
[`CONTEXTO.md`](CONTEXTO.md) y la tabla resumida del [README](../README.md). Los
nombres de archivo están anclados a las unidades del programa analítico justamente
para que un cambio de calendario no obligue a renombrar nada.

---

## 4. Cómo pedirle esto a un agente de IA

El repositorio está preparado para que una sesión de Claude Code (u otro agente) lo
retome sin contexto previo. [`CLAUDE.md`](../CLAUDE.md) en la raíz se carga solo.

Un arranque de sesión que funciona:

> Leé `docs/ESTADO.md` y `docs/CONVENCIONES.md`, y después desarrollá el notebook de
> la Unidad III siguiendo `docs/teoria/unidad_III.md` y usando
> `notebooks/04_unidad_IV_finanzas.ipynb` como molde. Verificá con
> `python tools/probar_nb.py` antes de commitear.

Lo que **no** hace falta explicarle: la estructura del repo, las convenciones de
notación, qué decisiones ya se tomaron, ni cuáles son los valores esperados de cada
ejercicio. Todo eso está en `docs/`.

---

## 5. Mapa rápido de archivos

```
README.md                  Portada para alumnos: badges de Colab
CLAUDE.md                  Reglas para agentes de IA
requirements.txt           Dependencias de uso
requirements-dev.txt       Dependencias de mantenimiento
.gitattributes             Normaliza finales de línea entre sistemas operativos

notebooks/                 El producto. Un .ipynb por unidad + 2 de repaso
src/eri_utils.py           Módulo compartido (API pública: no romper firmas)
data/                      Datasets versionados + diccionario de datos
latex/                     Fuentes .tex: la verdad de la teoría
tools/                     verificar · probar_nb · limpiar_notebooks · nbgen
docs/                      Esta documentación
docs/teoria/               Resumen técnico por unidad
```
