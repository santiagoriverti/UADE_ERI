# Estado del proyecto

> **Documento de handoff.** Se actualiza al final de cada sesión de trabajo. Es lo que
> permite retomar el proyecto desde otra máquina sin contexto previo.
>
> Si es tu primera vez en este repositorio, leé también
> [`COMO_TRABAJAR.md`](COMO_TRABAJAR.md) para poner el entorno en marcha.

**Última actualización**: 4 de septiembre de 2026
**Rama**: `main` · **Remoto**: https://github.com/santiagoriverti/UADE_ERI

---

## Resumen en tres líneas

Andamiaje completo del repositorio y documentación de proyecto terminada. El módulo
compartido `eri_utils` cubre las Unidades I a V y está verificado contra 55 valores de
la guía de soluciones. El notebook de la **Unidad IV** está desarrollado de punta a
punta y sirve de molde para los once restantes, que están en esqueleto.

**Próximo paso**: revisar el notebook de la Unidad IV y, si el formato convence,
desarrollar las Unidades I, II, III y V para cerrar el primer parcial.

---

## Qué está hecho

### Infraestructura ✅

| Componente | Estado |
|---|---|
| Estructura de directorios | Completa |
| `README.md` con badges de Colab para los 12 notebooks | Completo |
| `src/eri_utils.py` — módulo compartido | Completo, v0.1.0 |
| `tools/verificar.py` | 55 comprobaciones, todas pasan |
| `tools/probar_nb.py` | Ejecuta los 12 notebooks; todos corren limpios |
| `tools/limpiar_notebooks.py` | Funcional |
| `tools/nbgen.py` | Funcional |
| `data/retornos_ejemplo.csv` + diccionario de datos | Completo |
| `requirements.txt`, `requirements-dev.txt` | Completos |
| `.gitignore`, `.gitattributes` | Completos |
| Push a `main` y URLs crudas verificadas (HTTP 200) | ✅ |

### Documentación ✅

Toda la memoria del proyecto está escrita:

| Archivo | Contenido |
|---|---|
| `CLAUDE.md` | Reglas de trabajo y arranque de sesión para agentes de IA |
| `docs/COMO_TRABAJAR.md` | Puesta en marcha en máquina nueva, ciclo de trabajo, troubleshooting |
| `docs/ARQUITECTURA.md` | Estructura y fundamento de cada decisión de diseño |
| `docs/CONTEXTO.md` | La materia: cronograma, unidades, bibliografía |
| `docs/CONVENCIONES.md` | Notación, estilo y anatomía obligatoria de un notebook |
| `docs/ESTADO.md` | Este archivo |
| `docs/teoria/unidad_I.md` … `unidad_X.md` | Resumen técnico de las diez unidades |
| `tools/README.md`, `data/README.md`, `latex/README.md` | Documentación local de cada carpeta |

Los documentos de teoría de las **Unidades I a V** están derivados de las notas de
clase del docente y son fieles a ellas. Los de las **Unidades VI a X** son *alcance
previsto*, reconstruido del programa analítico y la bibliografía: cuando existan las
notas `.tex`, hay que reescribirlos para que reflejen esas notas.

### Notebooks

| Notebook | Estado |
|---|---|
| `04_unidad_IV_finanzas.ipynb` | ✅ **Completo.** 71 celdas, 30 `assert`, ejecuta limpio |
| Los otros 11 | 🚧 Esqueleto: portada, celda de setup, secciones previstas y aviso de obra |

El de la Unidad IV cubre: media y varianza de cartera, por qué domina la covarianza,
frontera de Markowitz (analítica y contrastada contra SLSQP), bala de Markowitz con
20 000 carteras, separación de Tobin y CML, CAPM y SML, descomposición del riesgo,
futuros y cobertura de varianza mínima, el puente con el factor de descuento
estocástico, dos widgets interactivos, un ejemplo empírico con el CSV, y los nueve
ejercicios de la guía resueltos con verificación.

---

## Qué falta

### Bloqueado: hace falta material del docente

1. **Notas de clase de las Unidades VI a X.** No están redactadas. Sin ellas, los
   notebooks 06 a 10 no pueden desarrollarse con la fidelidad que tienen los de I a V.
   Los `docs/teoria/unidad_VI.md` … `unidad_X.md` dejan documentado el alcance
   previsto, pero **no son la palabra del docente**.

2. **Fuentes `.tex` en `latex/`.** La carpeta tiene solo su `README.md`. Los archivos
   existen en poder del docente y hay que copiarlos con estos nombres exactos, que son
   los que citan `CONTEXTO.md` y los `docs/teoria/`:

   ```
   latex/cronograma.tex
   latex/clase_01_unidad_I.tex
   latex/clase_02_unidad_II.tex
   latex/clase_03_unidad_III.tex
   latex/clase_04_unidad_IV.tex
   latex/clase_05_unidad_V.tex
   latex/guia_ejercicios_soluciones.tex
   ```

   El repositorio funciona sin ellos —los `docs/teoria/` tienen la sustancia—, pero son
   la fuente de verdad y conviene versionarlos.

### Próximos pasos, en orden

1. **Revisar el notebook de la Unidad IV.** Es el molde: cualquier cambio de criterio
   sobre nivel de detalle teórico, tono, densidad de gráficos o presentación de los
   ejercicios conviene decidirlo antes de replicarlo once veces.
2. **Desarrollar las Unidades I, II, III y V.** Cada `docs/teoria/unidad_*.md` ya tiene
   listadas las figuras a reproducir, las simulaciones a hacer y los valores esperados
   de cada ejercicio, así que el trabajo es mecánico.
3. **Cerrar el primer parcial** con `11_repaso_parcial_1`.
4. Cuando estén las notas VI–X: reescribir los `docs/teoria/` correspondientes y
   desarrollar esos notebooks, más `12_repaso_parcial_2`.

### Funciones a agregar a `eri_utils`

Están anotadas al final de cada `docs/teoria/unidad_*.md`. Las principales:

| Unidad | Funciones |
|---|---|
| I | `peso_decision_prelec`, `valor_prospect` |
| III | `precios_estado_equilibrio`, `curva_contrato` |
| V | `sandmo_optimo_numerico` |
| VI | `contrato_lineal_cara`, `reparto_principal_agente` |
| VII | `riesgo_moral_discreto`, `cociente_verosimilitud` |
| VIII | `mercado_limones`, `espiral_seleccion_adversa`, `virtual_surplus` |
| IX | `spence_intervalo_separador`, `spence_bienestar` |
| X | `simular_subastas`, `maldicion_ganador` |

Cada una que resuelva un ejercicio de la guía debería sumar su comprobación en
`tools/verificar.py`.

---

## Decisiones ya tomadas (no volver a discutirlas)

El fundamento completo está en [`ARQUITECTURA.md`](ARQUITECTURA.md).

| Decisión | Alternativa descartada | Motivo en una línea |
|---|---|---|
| Un notebook por **unidad**, no por clase | Uno por clase del cronograma | El cronograma cambia cada cuatrimestre; el programa analítico no |
| Teoría **completa** dentro del notebook | Notebook como *companion* del PDF | Que sirva para estudiar sin tener el PDF al lado |
| Un solo notebook **resuelto** por unidad | Versión de alumno en blanco + docente | Evita mantener dos archivos que se desincronizan |
| Código compartido vía `wget` de `eri_utils.py` | Paquete pip; autonomía total | Instantáneo al arrancar la clase y un solo lugar donde arreglar |
| Matplotlib + `ipywidgets` selectivo | Plotly | Peso del `.ipynb` y render en la vista previa de GitHub |
| Datos **sintéticos versionados** | Descarga en vivo con `yfinance` | Una clase se da una vez y no admite que falle la red |
| Notebooks **sin salidas** en el repo | Versionar los outputs | Diffs de miles de líneas por un píxel |
| Semilla fija `SEMILLA = 1410` | Aleatoriedad libre | Los `assert` tienen que dar siempre lo mismo |

---

## Notas de mantenimiento

- **Los badges de Colab exigen que el notebook esté pusheado a `main`.** Un archivo
  que existe solo en local da 404 al abrirlo desde el README.
- **Colab cachea.** Si un alumno ve una versión vieja: `Archivo → Revertir a la versión
  guardada`, o agregar `?flush_cache=true` a la URL.
- **`src/eri_utils.py` es API pública.** Agregar funciones es libre; cambiar firmas
  existentes rompe notebooks ya publicados. Correr `python tools/probar_nb.py --todos`
  antes de tocarlo.
- **No regenerar `data/retornos_ejemplo.csv`.** Su proceso generador es determinístico
  y está documentado en `data/README.md`, pero los `assert` de la Unidad IV están
  calibrados contra esos valores exactos.
- **`.gitattributes` normaliza los finales de línea a LF.** Sin eso, editar el mismo
  archivo en Windows y en otra máquina produce diffs de «cambió todo el archivo».
- Checklist previo a cada commit: `verificar.py` → `probar_nb.py --todos` →
  `limpiar_notebooks.py` → actualizar este archivo → commit → `git push origin main`.

---

## Bitácora

### 4 de septiembre de 2026 — Sesión 2: preparación del handoff

- Rescatadas al repositorio las herramientas de autoría y prueba que hasta ahora vivían
  fuera de él: **`tools/probar_nb.py`** (ejecuta los notebooks de punta a punta
  parcheando la descarga de Colab por rutas locales — es el test del repo) y
  **`tools/nbgen.py`** (genera un `.ipynb` desde texto plano). Sin esto, otra sesión no
  tenía con qué verificar un notebook.
- Escrito **`docs/COMO_TRABAJAR.md`**: puesta en marcha en una máquina nueva, tres
  comandos de verificación, tabla de troubleshooting, ciclo de trabajo y cómo pedirle
  el trabajo a un agente de IA.
- Escrito **`tools/README.md`** con la función de cada script.
- Agregados **`.gitattributes`** (normaliza finales de línea a LF entre sistemas
  operativos) y **`requirements-dev.txt`** (nbformat, nbclient, ipykernel).
- Reescrito `CLAUDE.md` con la secuencia de arranque de sesión y los cuidados
  particulares del repositorio.
- `.gitignore`: se ignoran los borradores `.nbsrc`.
- Verificado que los 12 notebooks ejecutan limpios con la herramienta nueva.

### 4 de septiembre de 2026 — Sesión 1: estructura inicial

- Definida la arquitectura completa del proyecto y documentada en `docs/`.
- Escrito `src/eri_utils.py` con las funciones transversales de las Unidades I a V,
  validado contra los 55 valores publicados en la guía de soluciones.
- Corregido un problema de precisión numérica en `arrow_pratt_absoluta`: con paso
  absoluto `h = 1e-4`, el numerador de la derivada segunda cae por debajo de la
  resolución del punto flotante y el error llegaba a 6·10⁻⁵ relativo. Se pasó a paso
  **relativo** (`h·max(|y|, 1)`), que lo baja a menos de 10⁻⁷.
- Generado `data/retornos_ejemplo.csv` con un modelo de un factor de parámetros
  conocidos, para poder contrastar las betas estimadas con las verdaderas. Con 120
  meses el error de estimación es visible (Energía: 1,06 estimada contra 1,35
  verdadera), y eso se usa en el notebook como advertencia sobre el CAPM aplicado.
- Desarrollado y verificado el notebook de la Unidad IV.
- Generados los once esqueletos restantes; primer push a `main`.
