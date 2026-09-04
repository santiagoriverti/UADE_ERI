# Unidad I — Decisiones bajo Riesgo e Incertidumbre

**Clase 1 (05/08)** · Notebook `01_unidad_I_decisiones_riesgo_incertidumbre.ipynb`
**Fuente**: `latex/clase_01_unidad_I.tex` · Gravelle & Rees cap. 17; Kahneman & Tversky (1979)
**Estado**: notas escritas · notebook pendiente

---

## De qué se trata

Es la clase que instala la tensión que recorre toda la materia: **el modelo
normativo frente a la evidencia descriptiva**. Empieza sin probabilidades (criterios
de decisión bajo incertidumbre estricta), pasa al modelo normativo con probabilidades
conocidas (utilidad esperada), lo confronta con la evidencia experimental (Teoría de
las Perspectivas) y termina cuestionando el propio supuesto de que las
probabilidades existen y son conocidas (cisnes negros, sesgos de optimismo).

El recorrido es deliberadamente incómodo: cada bloque derriba al anterior.

---

## 1. La distinción de Knight

**Riesgo**: el decisor conoce el conjunto de resultados y puede asignarles una
distribución de probabilidad. Incertidumbre *mensurable*.

**Incertidumbre** (knightiana, en sentido estricto): ni siquiera se conocen las
probabilidades. Situación única, irrepetible, sin frecuencia. Incertidumbre *no
mensurable*.

No es un tecnicismo: para Knight (1921) el beneficio empresario nace de la
incertidumbre **no asegurable**. Si todo riesgo fuese mensurable, se transferiría
vía seguros y desaparecería como fuente de renta. Reaparece en la Unidad V con
Sandmo (beneficio positivo en el largo plazo competitivo) y en la Unidad II con
Ellsberg (aversión a la ambigüedad).

## 2. Estados del mundo y prospectos

Un **estado del mundo** $s \in \{1,\dots,S\}$ es una especificación completa de las
variables ambientales fuera del control del decisor. El conjunto de estados es:

- **exhaustivo** — contiene todo lo que puede ocurrir;
- **mutuamente excluyente** — uno descarta a los demás;
- **exógeno** — ningún agente influye sobre cuál ocurre.

Un **prospecto** (o lotería) es el objeto de elección de la teoría:

$$\mathbf{P} = (\pi_1,\dots,\pi_S;\, y_1,\dots,y_S), \qquad \pi_s \ge 0,\ \sum_s \pi_s = 1$$

Notación abreviada: $(x, p)$ paga $x$ con probabilidad $p$ y $0$ con $1-p$.

> 💡 Toda la teoría de la decisión consiste en construir una relación de preferencias
> sobre prospectos y encontrar una función simple que la represente.

## 3. Criterios sin probabilidades

Matriz de pagos $\{x_{ij}\}$: filas = acciones, columnas = estados.

| Criterio | Regla | Filosofía | Debilidad |
|---|---|---|---|
| **Maximin** (Wald) | $\max_i \min_j x_{ij}$ | Pesimismo puro | Ignora todo el potencial de ganancia |
| **Maximax** | $\max_i \max_j x_{ij}$ | Optimismo puro | Ignora el riesgo de ruina |
| **Hurwicz** | $\max_i [\alpha \max_j x_{ij} + (1-\alpha)\min_j x_{ij}]$ | Optimismo parcial | $\alpha$ es subjetivo; usa solo los extremos |
| **Laplace** | $\max_i \frac{1}{S}\sum_j x_{ij}$ | Razón insuficiente | Depende de cómo se agrupen los estados |
| **Minimax-arrepentimiento** (Savage) | $\min_i \max_j r_{ij}$, con $r_{ij}=\max_k x_{kj}-x_{ij}$ | Minimizar el remordimiento | Puede violar independencia de alternativas irrelevantes |

**Ejemplo del texto** (pagos en millones):

| | $s_1$ recesión | $s_2$ estable | $s_3$ expansión |
|---|---|---|---|
| $a_1$ bono seguro | 50 | 50 | 50 |
| $a_2$ proyecto moderado | 20 | 60 | 90 |
| $a_3$ proyecto agresivo | −30 | 40 | 150 |

Resultados: maximin → $a_1$; maximax → $a_3$; Hurwicz($\alpha=0{,}5$) → $a_3$;
Laplace → $a_2$; minimax-arrepentimiento → $a_2$.

**Cinco criterios, tres respuestas distintas sobre la misma matriz.** Milnor (1954)
mostró que ningún criterio satisface simultáneamente un conjunto natural de axiomas
deseables. En ausencia de probabilidades, la elección exige un juicio adicional
sobre la actitud frente a lo desconocido.

## 4. El modelo normativo: utilidad esperada

Axiomas de von Neumann-Morgenstern (versión de esta clase; se desarrollan en la
Unidad II): **orden completo**, **continuidad**, **independencia**.

**Teorema de representación.** Si $\succsim$ satisface los axiomas, existe $v(\cdot)$,
única salvo transformación afín positiva, tal que
$\mathbf{P} \succsim \mathbf{Q} \iff U(\mathbf{P}) \ge U(\mathbf{Q})$, con
$U(\mathbf{P}) = \sum_s \pi_s v(y_s) = E[v(y)]$.

Utilidad **cardinal**, no ordinal: las diferencias de utilidad tienen sentido.

**Equivalente cierto** $y_c$: $v(y_c) = E[v(y)]$.
**Prima de riesgo**: $\rho = \bar y - y_c$.

| | Relación | Actitud |
|---|---|---|
| $y_c < \bar y$, $\rho > 0$ | $v$ estrictamente cóncava | Aversión al riesgo |
| $y_c = \bar y$, $\rho = 0$ | $v$ lineal | Neutralidad |
| $y_c > \bar y$, $\rho < 0$ | $v$ convexa | Propensión |

La equivalencia concavidad ⟺ aversión es la desigualdad de Jensen.

**Arrow-Pratt** (se profundiza en la Unidad II):
$A(y) = -v''(y)/v'(y)$ y $R(y) = y\,A(y)$. Para riesgos pequeños,
$\rho \approx \tfrac12 A(\bar y)\sigma^2$.

## 5. La crítica descriptiva: Teoría de las Perspectivas

Kahneman & Tversky (1979) documentan tres efectos sistemáticos que violan los
axiomas.

**Efecto certeza.** Se sobreponderan los resultados ciertos frente a los meramente
probables. Contraejemplo de Allais:

| Problema 1 | Problema 2 |
|---|---|
| $A:(2500,\,0{,}33;\ 2400,\,0{,}66;\ 0,\,0{,}01)$ | $C:(2500,\,0{,}33;\ 0,\,0{,}67)$ |
| $B:(2400)$ — elegida por el 82 % | $D:(2400,\,0{,}34;\ 0,\,0{,}66)$ — 83 % elige $C$ |

Elegir $B$ implica $0{,}34\,v(2400) > 0{,}33\,v(2500)$; elegir $C$ implica lo
contrario. **Ninguna** $v$ racionaliza ambas. Se viola **independencia**.

**Efecto reflejo.** Al invertir el signo de los resultados, las preferencias se
reflejan como en un espejo: aversión al riesgo en ganancias convive con **búsqueda**
de riesgo en pérdidas. Frente a perder 3000 seguro, el 92 % prefiere arriesgarse a
perder 4000 con probabilidad 0,80 —aunque esa apuesta tiene *peor* valor esperado.
Incompatible con una $v$ globalmente cóncava.

**Efecto aislamiento (framing).** La gente descarta los componentes comunes y se
concentra en lo distintivo. Como un mismo par de prospectos admite más de una
descomposición en común + distintivo, distintas presentaciones del **mismo**
problema generan preferencias distintas. Problemas 11 y 12: idénticos en riqueza
final, opuestos en la elección observada.

**El modelo.** Dos fases: *edición* (codificación, combinación, segregación,
cancelación, simplificación, detección de dominancia) y *evaluación*:

$$V(x,p;\,y,q) = \pi(p)\,v(x) + \pi(q)\,v(y)$$

Dos diferencias con la utilidad esperada: (i) $v$ se define sobre **cambios**
respecto de un punto de referencia, no sobre riqueza final; (ii) las probabilidades
se reemplazan por **pesos de decisión** $\pi(p)$.

**Función de valor $v$**: cóncava en ganancias, convexa en pérdidas, y **más
empinada** en pérdidas ($v'(x) < v'(-x)$ para $x>0$). Forma de S con quiebre en la
referencia. Eso es la **aversión a las pérdidas**.

**Función de ponderación $\pi$**: creciente, $\pi(0)=0$, $\pi(1)=1$, con
sobreponderación de probabilidades bajas ($\pi(p)>p$ para $p$ chico), subcertidumbre
($\pi(p)+\pi(1-p)<1$), subaditividad y subproporcionalidad.

> 💡 La sobreponderación de probabilidades bajas explica de un solo golpe la compra
> de loterías y la compra de seguros. Combinada con la función de valor en S, produce
> el «patrón cuádruple» de actitudes al riesgo.

> ⚠️ **Colisión de notación.** En Gravelle $\pi_s$ es la *probabilidad* del estado
> $s$; en Kahneman-Tversky $\pi(p)$ es el *peso de decisión*. No son lo mismo:
> $\pi(p)$ no es una medida de probabilidad. En el notebook: `probs` vs
> `peso_decision`.

## 6. Cisnes negros y sesgos de optimismo

**Cisne negro** (Taleb, 2007): evento (i) atípico, fuera de las expectativas
ordinarias; (ii) de impacto extremo; (iii) retrospectivamente predecible. La crítica
apunta a la sobreconfianza en distribuciones de colas finas. Reconecta con la
incertidumbre knightiana: cuando la distribución misma es desconocida o inestable,
ni la utilidad esperada ni la Teoría de las Perspectivas —que operan sobre
probabilidades dadas— son plenamente aplicables. La respuesta sensata pasa menos por
afinar el cálculo y más por la **robustez**.

**Sesgos de optimismo**: optimismo comparativo (Weinstein, 1980 — la mayoría se cree
por encima del promedio) y falacia de la planificación (Kahneman, 2011 — los planes
se construyen sobre escenarios cercanos al mejor caso). Combinados con las colas
gruesas ignoradas, explican por qué agentes y organizaciones quedan reiteradamente
mal preparados.

---

## Qué debe hacer el notebook

### Figuras a reproducir

| Figura de las notas | Cómo hacerla en Python |
|---|---|
| `fig:concava` — aversión al riesgo | $v(y)=2\sqrt y$ sobre $[0,10]$, cuerda entre $(1,2)$ y $(9,6)$, marcar $y_c=4$, $\bar y=5$, llave para $\rho=1$ |
| `fig:valor` — función de valor en S | $v(x)=1{,}5\sqrt x$ para $x\ge0$ y $-2{,}5\sqrt{-x}$ para $x<0$; anotar la asimetría en $x=\pm2$ |
| `fig:pond` — ponderación de probabilidades | Curva inversa en S sobre $[0,1]$ con la diagonal de referencia; usar la Prelec $\pi(p)=\exp(-(-\ln p)^{\gamma})$ con $\gamma\approx0{,}65$ |

### Cálculos y simulaciones

- Tabla comparativa de los cinco criterios con `eri.tabla_criterios`.
- **Widget**: deslizador de $\alpha$ de Hurwicz mostrando cómo cambia la acción
  elegida — hace visible que la recomendación depende de un parámetro subjetivo.
- Verificación numérica de la incompatibilidad de Allais: barrer un espacio de
  funciones $v$ (CRRA con distintos $R$) y mostrar que **ninguna** satisface las dos
  desigualdades a la vez.
- Simulación del efecto reflejo comparando valor esperado y elección modal.
- Comparación de colas: normal vs. Pareto/Student-t con la misma varianza, y qué
  fracción del total aportan los peores eventos. Ilustra el cisne negro sin
  metáforas.

### Ejercicios de la guía (6)

1. Criterios de decisión sobre la matriz $[[10,40,70],[30,30,30],[60,20,5]]$ con
   $\alpha=0{,}6$. **Respuestas**: maximin → $a_2$; maximax, Hurwicz y Laplace →
   $a_1$; minimax-arrepentimiento → $a_2$. Agregar una acción **dominada** no cambia
   ninguna recomendación (demostrarlo en código con $a_4=(5,30,60)$).
2. Equivalente cierto con $v(y)=\ln y$ y $(0{,}5;\,100,\,400)$. $\bar y=250$,
   $E[v]=\ln 200$, $y_c=200$ (media geométrica), $\rho=50$.
3. Arrow-Pratt: verificar que CARA da $A(y)=a$ constante y CRRA da $R(y)=R$
   constante; mostrar el límite $R\to1 \Rightarrow \ln y$ por L'Hôpital (usar sympy).
4. Allais: incompatibilidad de las dos desigualdades. Axioma violado: independencia.
5. Efecto aislamiento: reescribir Problemas 11 y 12 en riqueza final y mostrar que
   son idénticos ($A=C=(2000,\,0{,}5;\,1000,\,0{,}5)$, $B=D=(1500)$).
6. Subaditividad de $\pi$: de $(6000,\,0{,}001)\succ(3000,\,0{,}002)$ y $v$ cóncava
   se sigue $\pi(0{,}001)/\pi(0{,}002) > 1/2$.

### Funciones de `eri_utils` que usa

`maximin`, `maximax`, `hurwicz`, `laplace`, `minimax_arrepentimiento`,
`matriz_arrepentimiento`, `tabla_criterios`, `u_log`, `u_sqrt`, `u_crra`, `u_cara`,
`utilidad_esperada`, `equivalente_cierto`, `prima_riesgo`, `arrow_pratt_absoluta`,
`arrow_pratt_relativa`.

**Podría hacer falta agregar**: `peso_decision_prelec(p, gamma)` y
`valor_prospect(x, alpha, beta, lambda_)` para la función de valor de
Kahneman-Tversky. No están todavía en el módulo.

### Conexión con la unidad siguiente

La Unidad I *usa* la utilidad esperada como herramienta. La Unidad II la **deriva**
de axiomas y explica por qué el valor esperado no puede ser el criterio (San
Petersburgo).
