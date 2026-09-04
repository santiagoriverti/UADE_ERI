# Unidad VI — Introducción a la Información Asimétrica

**Clase 9 (23/09)** · Notebook `06_unidad_VI_informacion_asimetrica.ipynb`
**Bibliografía**: Macho-Stadler & Pérez Castrillo caps. 1–2; Borch (1962)
**Estado**: ⚠️ **notas de clase pendientes** · notebook pendiente

> ⚠️ **Este documento no reemplaza a las notas de clase.** Es el *alcance previsto*
> de la unidad, reconstruido a partir del programa analítico y la bibliografía. Cuando
> existan las notas en `latex/clase_09_unidad_VI.tex`, ellas pasan a ser la fuente de
> verdad y este archivo debe reescribirse para reflejarlas, como se hizo con I–V.

---

## De qué se trata

Bisagra del curso. Hasta la Unidad V el problema era el **azar**: un decisor (o
varios) frente a estados de la naturaleza exógenos. A partir de acá el problema es la
**información**: los agentes saben cosas distintas, y esa asimetría —no el azar—
genera ineficiencia.

La unidad instala el andamiaje común de las Unidades VII a IX: la relación
agente-principal, el contrato como objeto de elección, y el *benchmark* de
información simétrica contra el cual se miden todas las distorsiones posteriores.

---

## 1. Mercados incompletos e información asimétrica

Recuperar de la Unidad III la noción de mercado completo de derechos contingentes y
el primer teorema del bienestar. La información asimétrica es una fuente de
**incompletitud endógena**: no es que falte el mercado, es que no puede existir porque
el pago prometido depende de algo que una de las partes no puede verificar.

Distinción central que organiza todo el bloque:

| | Qué es privado | Cuándo aparece | Unidad |
|---|---|---|---|
| **Riesgo moral** | Una **acción** del agente, no observable | *Después* de firmar el contrato | VII |
| **Selección adversa** | Un **tipo** o característica del agente | *Antes* de firmar; el principal ofrece el menú | VIII |
| **Señalización** | Un **tipo**, pero el agente puede emitir una señal costosa | *Antes*; mueve primero el informado | IX |

La diferencia entre selección adversa y señalización es **quién mueve primero**: en
selección adversa el principal (no informado) diseña el menú; en señalización el
agente (informado) actúa primero para revelarse.

## 2. La relación agente-principal

**Principal**: diseña el contrato, tiene el poder de proponer.
**Agente**: acepta o rechaza; posee la información o toma la acción.

Elementos del problema:

- resultado verificable $\pi$ (beneficio, producto), sobre el que se puede contratar;
- **contrato** $w(\pi)$, la regla que traduce el resultado observable en pago;
- **restricción de participación** (RP): el agente acepta solo si obtiene al menos su
  utilidad de reserva $\bar U$;
- **restricción de incentivos** (RI): aparece solo bajo asimetría; el agente debe
  preferir la acción o el contrato que el principal quiere que elija.

**El programa del principal:**

$$\max_{w(\cdot)}\ E[B(\pi - w(\pi))] \quad \text{s.a.} \quad \text{RP}, \ \text{RI}$$

Bajo información simétrica la RI no existe: el principal contrata directamente sobre
la acción o el tipo. **La RI es exactamente el costo de la información asimétrica.**

## 3. El modelo básico con información simétrica y el Teorema de Borch

**El punto clave de la unidad, y el más elegante**: el reparto óptimo de riesgo entre
principal y agente bajo información simétrica es **el mismo Teorema de Borch de la
Unidad III**. La condición de eficiencia es

$$\frac{u'(w(\pi))}{B'(\pi - w(\pi))} = \text{constante en todos los estados}$$

es decir, utilidades marginales ponderadas igualadas.

Dos casos límite de enorme valor pedagógico:

- **Principal neutral, agente averso** ⟹ el agente recibe un **salario fijo**: el
  principal, que puede diversificar, absorbe todo el riesgo. Es la organización
  eficiente cuando el esfuerzo es observable.
- **Principal averso, agente neutral** ⟹ el agente recibe el residuo (es «dueño» del
  resultado y le paga al principal una renta fija).

> 💡 Bajo información simétrica, el contrato óptimo resuelve **solo** un problema de
> reparto de riesgo. Todo lo que las Unidades VII a IX agregan es la tensión entre ese
> reparto eficiente y la necesidad de dar incentivos. **Incentivos y seguro tiran para
> lados opuestos**: asegurar al agente destruye sus incentivos, e incentivarlo lo
> obliga a soportar riesgo. Ésa es toda la economía de la información en una frase.

## 4. Contratos lineales

$$w(\pi) = \alpha + \beta\pi$$

con $\alpha$ el componente fijo y $\beta$ la participación en el resultado. Marco de
referencia por su tratabilidad: bajo CARA-Normal (Unidad II) el problema tiene
solución cerrada, y $\beta^*$ resulta ser

$$\beta^* = \frac{1}{1 + a\,\sigma^2\,c''}$$

—decreciente en la aversión del agente $a$, en la varianza del resultado $\sigma^2$ y
en la curvatura del costo del esfuerzo. Los tres términos tienen lectura económica
directa y anticipan la Unidad VII.

Notar la conexión con la Unidad III: $\beta$ es formalmente una **cuota de reparto de
riesgo** exactamente como el $\alpha_i$ de Borch-Wilson, pero distorsionada hacia
arriba por la necesidad de incentivar.

---

## Qué debería hacer el notebook

### Contenido mínimo

1. **Mapa del bloque de información**: una tabla y un diagrama de la secuencia
   temporal de cada uno de los tres problemas, para que quede claro desde el arranque
   qué se está distinguiendo.
2. **Verificación del Teorema de Borch en el marco agente-principal**: resolver
   numéricamente el reparto óptimo con distintas combinaciones de aversión y mostrar
   que el salario fijo emerge cuando el principal es neutral. Reutiliza directamente
   `eri.reparto_borch_cara` de la Unidad III.
3. **Contrato lineal CARA-Normal**: implementar el equivalente cierto de principal y
   agente, resolver $\beta^*$ y hacer estática comparada.
4. **Widget**: deslizadores de $a$ (aversión del agente) y $\sigma^2$ mostrando
   $\beta^*$ caer. Hace tangible el trade-off incentivos-seguro.
5. Un ejemplo de secuencia temporal simulada por agente, para introducir la
   distinción entre acción oculta e información oculta.

### Funciones nuevas que habría que agregar a `eri_utils`

```python
contrato_lineal_cara(a, sigma2, c2)   # beta* optimo bajo CARA-Normal
equivalente_cierto_agente(...)        # EC del agente ante un contrato lineal
reparto_principal_agente(...)         # reparto de Borch con dos utilidades dadas
```

### Datos necesarios

Ninguno: todo paramétrico.
