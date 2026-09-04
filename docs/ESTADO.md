# Estado del proyecto

> **Documento de handoff.** Se actualiza al final de cada sesión de trabajo. Es lo
> que permite retomar el proyecto desde otra máquina sin contexto previo.

**Última actualización**: 4 de septiembre de 2026

---

## Resumen en una línea

Andamiaje completo del repositorio, módulo compartido verificado contra la guía de
soluciones, y el notebook de la **Unidad IV** desarrollado de punta a punta como
molde para los once restantes.

---

## Qué está hecho

### Infraestructura ✅

| Componente | Estado |
|---|---|
| Estructura de directorios | Completa |
| `README.md` con badges de Colab para los 12 notebooks | Completo |
| `src/eri_utils.py` — módulo compartido | Completo, v0.1.0 |
| `tools/verificar.py` | 55 verificaciones, todas pasan |
| `tools/limpiar_notebooks.py` | Funcional |
| `data/retornos_ejemplo.csv` + diccionario de datos | Completo |
| `requirements.txt`, `.gitignore` | Completos |

### Documentación ✅

Toda la memoria del proyecto está escrita: `ARQUITECTURA.md`, `CONTEXTO.md`,
`CONVENCIONES.md`, este archivo, y los diez `docs/teoria/unidad_*.md`.

Los documentos de teoría de las **Unidades I a V** están derivados de las notas de
clase del docente y son fieles a ellas. Los de las **Unidades VI a X** son *alcance
previsto*, reconstruido del programa analítico y la bibliografía: cuando existan las
notas `.tex`, hay que reescribirlos para que reflejen esas notas.

### Notebooks

| Notebook | Estado |
|---|---|
| `04_unidad_IV_finanzas.ipynb` | ✅ **Completo.** 71 celdas, 30 `assert`, ejecuta limpio de punta a punta |
| Los otros 11 | 🚧 Esqueleto: portada, celda de setup, secciones previstas y aviso de construcción |

El notebook de la Unidad IV cubre: media y varianza de cartera, por qué domina la
covarianza, frontera de Markowitz (analítica y verificada contra SLSQP), bala de
Markowitz con 20 000 carteras, separación de Tobin y CML, CAPM y SML, descomposición
del riesgo, futuros y cobertura de varianza mínima, el puente con el factor de
descuento estocástico, dos widgets interactivos, un ejemplo empírico con el CSV, y los
nueve ejercicios de la guía resueltos con verificación.

---

## Qué falta

### Bloqueado por el docente

1. **Notas de clase de las Unidades VI a X.** No están redactadas. Sin ellas, los
   notebooks 06 a 10 no pueden desarrollarse con la fidelidad que exigen los de I a V.
   Los `docs/teoria/unidad_VI.md` … `unidad_X.md` dejan documentado el alcance
   previsto, pero **no son la palabra del docente**.
2. **Fuentes `.tex` en `latex/`.** La carpeta tiene solo su `README.md`. Los archivos
   existen en poder del docente (cronograma, clases 1 a 5, guía de soluciones) y hay
   que copiarlos con estos nombres:

   ```
   latex/cronograma.tex
   latex/clase_01_unidad_I.tex
   latex/clase_02_unidad_II.tex
   latex/clase_03_unidad_III.tex
   latex/clase_04_unidad_IV.tex
   latex/clase_05_unidad_V.tex
   latex/guia_ejercicios_soluciones.tex
   ```

### Próximos pasos sugeridos, en orden

1. **Revisar el notebook de la Unidad IV** y ajustar el formato si hace falta. Es el
   molde: cualquier cambio de criterio conviene hacerlo ahora, antes de replicarlo
   once veces.
2. **Desarrollar las Unidades I, II, III y V** siguiendo ese molde y los
   `docs/teoria/unidad_*.md`, que ya tienen listadas las figuras a reproducir, las
   simulaciones a hacer y los valores esperados de cada ejercicio.
3. **Cerrar el primer parcial** con `11_repaso_parcial_1`.
4. Cuando estén las notas VI–X: reescribir los `docs/teoria/` correspondientes y
   desarrollar esos notebooks.

### Funciones a agregar a `eri_utils` cuando se desarrolle cada unidad

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

> ⚠️ `src/eri_utils.py` en `main` es **API pública**: los notebooks ya publicados
> apuntan al archivo crudo de GitHub. Se pueden agregar funciones libremente, pero no
> romper firmas existentes sin revisar los doce notebooks.

---

## Decisiones ya tomadas (no volver a discutirlas)

Las razones completas están en `docs/ARQUITECTURA.md`.

| Decisión | Alternativa descartada |
|---|---|
| Un notebook por **unidad**, no por clase | Un notebook por clase del cronograma |
| Teoría **completa** dentro del notebook | Notebook como *companion* del PDF |
| Un solo notebook **resuelto** por unidad | Versión de alumno en blanco + versión docente |
| Código compartido vía `wget` de `eri_utils.py` | Paquete pip; autonomía total de cada notebook |
| Matplotlib + `ipywidgets` selectivo | Plotly |
| Datos **sintéticos versionados** | Descarga en vivo con `yfinance` |
| Notebooks se commitean **sin salidas** | Versionar los outputs |
| Semilla fija `SEMILLA = 1410` | Aleatoriedad libre |

---

## Notas de mantenimiento

- **Los links de Colab del README requieren que el notebook esté pusheado a `main`.**
  Un archivo que existe solo en local da 404 al abrirlo desde el badge.
- Colab cachea: si un alumno ve una versión vieja, `Archivo → Revertir a la versión
  guardada` o agregar `?flush_cache=true` a la URL.
- Antes de commitear: ejecutar el notebook entero (los `assert` son el test), correr
  `python tools/verificar.py` si se tocó el módulo, y limpiar salidas con
  `python tools/limpiar_notebooks.py`.
- El proceso generador de `data/retornos_ejemplo.csv` es determinístico, pero **no lo
  regeneres**: los
  `assert` del notebook de la Unidad IV están calibrados contra esos valores.

---

## Bitácora

### 4 de septiembre de 2026 — Sesión inicial

- Definida la arquitectura completa del proyecto y documentada en `docs/`.
- Escrito `src/eri_utils.py` con las funciones transversales de las Unidades I a V,
  y validado contra los 55 valores publicados en la guía de soluciones.
- Corregido un problema de precisión numérica en `arrow_pratt_absoluta`: con paso
  absoluto `h = 1e-4`, el numerador de la derivada segunda cae por debajo de la
  resolución del punto flotante y el error llegaba a 6·10⁻⁵ relativo. Se pasó a paso
  **relativo** (`h·max(|y|, 1)`), que baja el error a menos de 10⁻⁷.
- Generado `data/retornos_ejemplo.csv` con un modelo de un factor de parámetros
  conocidos, para poder contrastar las betas estimadas con las verdaderas.
- Desarrollado y verificado el notebook de la Unidad IV.
- Generados los once esqueletos restantes.
