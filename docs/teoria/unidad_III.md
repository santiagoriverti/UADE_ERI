# Unidad III — Reparto Óptimo del Riesgo

**Clase 3 (19/08)** · Notebook `03_unidad_III_reparto_del_riesgo.ipynb`
**Fuente**: `latex/clase_03_unidad_III.tex` · Borch (1962); Gravelle & Rees cap. 19; Varian cap. 11
**Estado**: notas escritas · notebook pendiente

---

## De qué se trata

Cambio de punto de vista. En las Unidades I y II el riesgo era un problema
**individual**: un decisor aislado elegía entre prospectos. Acá el riesgo se
**reasigna entre agentes** mediante mercados e instituciones, generando mejoras de
Pareto.

La observación de partida es simple y fértil: si dos personas aversas enfrentan
riesgos no perfectamente correlacionados, ambas pueden mejorar redistribuyéndolos. El
riesgo no se destruye, pero se **reasigna** hacia quien está en mejores condiciones
de soportarlo, o se **reparte** de modo que a cada uno le toque una porción menos
temible. Es la lógica común del seguro, el reaseguro, la sociedad anónima, el mercado
accionario y el fondo de inversión.

> 💡 **El hilo conductor.** El riesgo agregado de una economía no puede eliminarse,
> solo repartirse; el riesgo puramente idiosincrático sí puede volverse despreciable
> si se lo reparte entre suficientes personas. Distinguir ambos tipos es toda la clase.

---

## 1. Estados de la naturaleza e ingresos contingentes

Un **plan de ingreso contingente** es $y=(y_1,\dots,y_S) \in \mathbb{R}^S_+$. La
**línea de certeza** es el lugar donde $y_1=\cdots=y_S$.

$$V(y) = \sum_{s} \pi_s\, v(y_s)$$

La misma utilidad esperada de siempre, pero mirada como función sobre el espacio de
**bienes contingentes**: «un peso en el estado $s$» es un bien distinto de «un peso
en el estado $s'$».

**Pendiente de las curvas de indiferencia:**

$$\left.\frac{dy_2}{dy_1}\right|_{V=\text{cte}} = -\frac{\pi_1 v'(y_1)}{\pi_2 v'(y_2)}$$

Sobre la línea de certeza $v'(y_1)=v'(y_2)$, de modo que **todas** las curvas la
cortan con la misma pendiente $-\pi_1/\pi_2$: la recta de apuestas justas. La
concavidad de $v$ las hace convexas hacia el origen.

**Utilidad dependiente del estado.** El supuesto de que la misma $v$ valora el
ingreso en todos los estados no siempre es inocuo: un paraguas vale distinto con
lluvia, y «¿cuánto vale un millón si uno está en coma?» es una pregunta legítima para
diseñar un seguro de salud. En general $V(y)=\sum_s \pi_s u(s, y_s)$.

## 2. El seguro como intercambio de derechos contingentes

$$y_1 = y - pq, \qquad y_2 = y - L + (1-p)q$$

Eliminando $q$ se obtiene la restricción presupuestaria en forma simétrica:

$$(1-p)\,y_1 + p\,y_2 = (1-p)\,y + p\,(y-L)$$

**Ésta es la lectura central de toda la unidad**: $(1-p)$ y $p$ son los **precios de
sendos derechos contingentes**. Comprar seguro es vender derechos sobre el estado
donde uno tiene «de más» para comprar derechos sobre el estado donde tiene «de menos».

Prima **actuarialmente justa**: $p=\pi_2$ (no altera el ingreso esperado). Entonces
la recta presupuestaria coincide con la de apuestas justas y el óptimo es cobertura
completa. Con recargo ($p>\pi_2$) la recta se aplana y el óptimo cae por debajo de la
línea de certeza: cobertura parcial.

**Mercados incompletos.** Si el individuo enfrenta *dos* fuentes de riesgo pero solo
puede asegurar una, aparecen cuatro estados y no existen todos los activos que
permitirían transferir ingreso a cada uno por separado. Resultado: la asignación
óptima **retiene** riesgo que con mercados completos sería eliminable. Motiva la
pregunta por la completitud.

## 3. Precios de estado y núcleo estocástico

Un **valor de Arrow** paga un peso si ocurre $s$ y cero si no; su precio es $q_s$.
Mercados **completos**: existe uno para cada estado.

De la CPO del agente:

$$\pi_s v'(c_s) = \lambda q_s \quad\Longrightarrow\quad q_s = \frac{\pi_s v'(c_s)}{\lambda}$$

El precio del derecho sobre $s$ es proporcional a la probabilidad **ponderada por la
utilidad marginal**. Y el precio de cualquier activo:

$$P(x) = \sum_s q_s x_s = E[m\,\tilde x], \qquad m_s = \frac{v'(c_s)}{\lambda}$$

con $m$ el **núcleo estocástico de descuento**. Lectura financiera: un activo
positivamente correlacionado con la riqueza (y por tanto negativamente con la
utilidad marginal) es poco valioso para diluir riesgo y debe ofrecer un rendimiento
esperado **mayor**; uno que cubre riesgo se paga caro y rinde menos. **Semilla
directa del CAPM.**

> 💡 Los precios de estado aparecen en tres disfraces que son el mismo objeto: la
> tasa de prima del seguro, el precio del valor de Arrow, y el núcleo estocástico de
> descuento de las finanzas. En un óptimo son proporcionales a $\pi_s v'(c_s)$.

## 4. Difusión del riesgo: Arrow-Lind

Un sindicato de $n$ miembros idénticos reparte un proyecto por partes iguales
($k=1/n$), con el pago del proyecto **independiente** del ingreso previo:
$\mathrm{Cov}(y_s,z_s)=0$.

**Teorema (Arrow-Lind, 1970).** $\lim_{n\to\infty} n\,\theta(1/n) = 0$, y por lo
tanto $P \to E[z]$: un sindicato suficientemente grande contrata **como si fuera
neutral al riesgo**, aunque todos sus miembros sean aversos.

**Por qué.** Por la aproximación de Pratt, $\theta(1/n) \approx \tfrac12 r\,
\mathrm{Var}(kz) = \tfrac12 r\,\sigma^2/n^2$. El recargo de cada miembro cae como
$1/n^2$ pero hay solo $n$ miembros, de modo que el total cae como $1/n$.

**La independencia es esencial.** Con correlación positiva el recargo no se anula:
ese riesgo es sistemático y alguien debe soportarlo.

## 5. Fondo común (pooling) y diversificación

Dos individuos con ingresos iid ($y'$ con probabilidad $\pi$, $y''$ si no) que
ponen todo en una bolsa y se llevan la mitad:

$$V(2)-V(1) = 2\pi(1-\pi)\left[v\!\left(\tfrac{y'+y''}{2}\right) - \tfrac12 v(y') - \tfrac12 v(y'')\right] > 0$$

positivo por concavidad (Jensen). **Mejora a ambos.** El pooling **no altera el
ingreso esperado**; lo que hace es reducir la varianza.

**Optimalidad del reparto igualitario.** Con $n$ agentes iid, el arreglo óptimo es el
fondo común en partes iguales. Idea: cualquier otro esquema equivale a «ingreso
igualitario + ruido de media cero», o sea un aumento del riesgo conservando la media
en el sentido de Rothschild-Stiglitz, que todo averso rechaza.

**Ley de Grandes Números.** $\bar y_n \to \mu$ en probabilidad (Chebyshev:
$P(|\bar y_n - \mu| \ge \varepsilon) \le \sigma^2/(n\varepsilon^2)$).

> ⚠️ **La falacia de la cancelación del riesgo.** La LGN estabiliza el **promedio**,
> no el **total**. El siniestro agregado $S_n=\sum_i \tilde x_i$ tiene
> $\mathrm{Var}(S_n)=n\sigma^2$, que **crece** con $n$; su desvío crece como
> $\sqrt n$. Una aseguradora no elimina el riesgo vendiendo muchas pólizas: hace
> pequeño el riesgo *por peso asegurado*, pero **aumenta** el riesgo agregado que
> debe respaldar con capital. Por eso el seguro necesita, además del pooling,
> reservas y reaseguro. Confundir ambas cosas es el error conceptual más frecuente
> de la unidad.

## 6. El Teorema de Borch

Con $n$ agentes, riqueza agregada aleatoria $W(s)=\sum_i w_i(s)$ y factibilidad
estado por estado $\sum_i c_i(s)=W(s)$:

**Teorema (Borch, 1962).** Un reparto es Pareto-óptimo si y solo si existen pesos
$\lambda_i>0$ tales que, **en cada estado**,

$$\lambda_i\,u_i'(c_i(s)) = \lambda_j\,u_j'(c_j(s)) \quad \forall i,j$$

Las utilidades marginales ponderadas se igualan entre todos los agentes en todos los
estados.

**Principio de mutualidad.** El multiplicador depende del estado **solo a través de
$W(s)$**. Por lo tanto $c_i(s) = c_i(W(s))$: dos estados con la misma riqueza
agregada reciben idéntico reparto individual, cualquiera sea la «causa» de esa
riqueza. Es la justificación teórica del fondo común: todo reparto eficiente equivale
a volcar los riesgos a una bolsa y repartir el total según una regla que depende solo
del total. **El riesgo idiosincrático desaparece del reparto; solo importa el agregado.**

**Regla marginal de reparto.** Con tolerancia al riesgo $T_i(c)=-u_i'(c)/u_i''(c)$:

$$\frac{dc_i}{dW} = \frac{T_i(c_i)}{\sum_j T_j(c_j)} \in (0,1), \qquad \sum_i \frac{dc_i}{dW}=1$$

Cada agente absorbe una porción del riesgo agregado **proporcional a su tolerancia**.

**Caso CARA — reparto lineal (Wilson, 1968).** Con $u_i(c)=-e^{-a_i c}$, la
tolerancia es constante ($T_i = 1/a_i$) y el reparto es **afín**:

$$c_i(W) = \alpha_i W + \beta_i, \qquad \alpha_i = \frac{1/a_i}{\sum_j 1/a_j}, \qquad \sum_i \alpha_i = 1,\ \sum_i \beta_i = 0$$

La más aversa carga con la fracción **menor** del riesgo y recibe a cambio una
transferencia cierta $\beta_i$ positiva.

**Riesgo idiosincrático vs. agregado.** Si $W$ es cierta (todo el riesgo se cancela
en la suma), cada $c_i(W)$ es constante: **todos alcanzan la línea de certeza**,
seguro mutuo completo. Si hay riesgo agregado, no puede asegurarse; lo único que la
eficiencia determina es cómo repartirlo.

## 7. Anexos de las notas

- **Arrow-Debreu**: bienes contingentes, equilibrio de Walras-Arrow, primer teorema
  del bienestar en el espacio de estados. Eliminando $q_s$ entre dos agentes se
  recupera exactamente la condición de Borch.
- **Ley de Grandes Números**: Markov, Chebyshev, LGN débil, y la advertencia sobre
  promedio vs. agregado.
- **Caja de Edgeworth de estados**: la curva de contrato es el lugar de tangencias,
  que es la condición de Borch para dos agentes. Sin riesgo agregado ($W_1=W_2$) la
  curva de contrato **es** la diagonal y el óptimo da ingreso cierto a ambos.

---

## Qué debe hacer el notebook

### Figuras a reproducir

| Figura | Cómo |
|---|---|
| `fig:seguro` | Plano $(y_1,y_2)$: línea de certeza a 45°, recta de apuestas justas, presupuesto con recargo, dotación, óptimo completo y parcial |
| `fig:edgeworth` | Caja de Edgeworth con curva de contrato, dotación fuera de ella y la lente de mejora |
| Arrow-Lind | Recargo total $n\theta(1/n)$ vs. $n$, mostrando la caída $O(1/n)$ |
| Promedio vs. agregado | Dos paneles: $\mathrm{Var}(\bar x_n)=\sigma^2/n$ cayendo y $\mathrm{Var}(S_n)=n\sigma^2$ subiendo. **La figura más importante de la unidad** |

### Cálculos y simulaciones

- **Monte Carlo del pooling**: simular $n$ agentes iid y graficar la distribución del
  ingreso por persona para $n=1,2,5,20,100$. Se ve la concentración alrededor de $\mu$.
- Verificación numérica del teorema de Borch: resolver el problema del planificador
  con `scipy.optimize` y comprobar que la solución numérica coincide con la fórmula
  analítica del reparto lineal CARA.
- **Widget**: deslizador de la tasa de prima $p$ mostrando el óptimo desplazándose
  de la línea de certeza hacia abajo a medida que crece el recargo.
- Equilibrio Arrow-Debreu con dos agentes: resolver los precios de estado por vaciado
  de mercado y verificar que satisfacen la condición de Borch.
- Chebyshev: comparar la cota con la probabilidad real simulada, para ver cuán
  conservadora es.

### Ejercicios de la guía (9)

1. Seguro con prima justa, $v=\sqrt y$, dotación $(100,36)$, $\pi=(0{,}75,0{,}25)$:
   $E[y]=84$, presupuesto $3y_1+y_2=336$, óptimo $y_1=y_2=84$, $q^*=64=L$, prima
   pagada 16. CE con seguro 84, sin seguro 81.
2. Recargo $p=0{,}40$ con $v=\ln y$: $y_2/y_1=0{,}5$, $q^*=17{,}5$, $y=(93,\,46{,}5)$.
3. Consumidor Arrow-Debreu con $\ln$, dotación $(10,20)$, $q=(0{,}5,\,0{,}4)$:
   $m=13$, $c^*=(13,\ 16{,}25)$. $q_1+q_2=0{,}9 \Rightarrow R_f\approx1{,}111$.
4. Valuación con precios de estado: bono $(1,1)$ rinde $R_f$; activo $(2,0)$ rinde
   1,00 (menos, cubre riesgo); activo $(0,2)$ rinde 1,25 (más, agrega riesgo).
5. Arrow-Lind CARA-Normal: $\theta(1/n)=\tfrac a2 \sigma^2/n^2$, total
   $\tfrac a2\sigma^2/n$, $P=1000-20/n$. Tabla para $n=1,10,100$.
6. Pooling con dos individuos, $v=\sqrt y$, $(100$ o $0)$ al 50 %: sin pool CE $=25$;
   con pool $V(2)=6{,}036$ y CE $\approx36{,}4$; varianza cae de 2500 a 1250.
7. Chebyshev: con $\mu=500$, $\sigma=1500$, $\varepsilon=100$ al 99 %, hace falta
   $n \ge 22\,500$. Con ese $n$, $\sigma_{S_n}=225\,000$.
8. Borch CARA: $a=(0{,}01,\ 0{,}02) \Rightarrow \alpha=(2/3,\ 1/3)$,
   $\beta \approx (-23{,}1,\ +23{,}1)$.
9. Edgeworth: (I) sin riesgo agregado, $q=(1,1)$, ambos con $(10,10)$ ciertos;
   (II) con riesgo agregado, $c_A=c_B=(16,4)$ y $q_2/q_1=4$.

### Funciones de `eri_utils` que usa

`riquezas_contingentes`, `cobertura_optima`, `pooling_iid`, `reparto_borch_cara`,
`u_log`, `u_sqrt`, `u_cara`, `utilidad_esperada`, `equivalente_cierto`.

**Podría hacer falta agregar**: `precios_estado_equilibrio(...)` para el equilibrio
Arrow-Debreu con dos agentes, y `curva_contrato(...)` para la caja de Edgeworth.

### Conexión con la unidad siguiente

Queda pendiente el **riesgo agregado o sistemático**, que ningún reparto elimina.
Formalizar su prima vía el núcleo estocástico conduce directamente a Markowitz y al
CAPM: son el mismo aparato de derechos contingentes, leído en el plano media-varianza.
