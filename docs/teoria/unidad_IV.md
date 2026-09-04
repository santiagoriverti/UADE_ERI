# Unidad IV — Aplicaciones a las Finanzas

**Clase 4 (26/08)** · Notebook `04_unidad_IV_finanzas.ipynb`
**Fuente**: `latex/clase_04_unidad_IV.tex` · Markowitz (1952); Sharpe (1964)
**Estado**: notas escritas · **notebook desarrollado (piloto de referencia)**

> Este notebook es el **molde** del repositorio. Cualquier otro notebook debe
> replicar su estructura, su estética y su forma de resolver y verificar ejercicios.

---

## De qué se trata

Traslada el problema del reparto del riesgo de la Unidad III al mercado de capitales.
Un activo financiero es, en el fondo, un **paquete de derechos contingentes**: paga
distinto en distintos estados. Cuando el inversor evalúa cada inversión solo por su
media y su varianza, el problema de elegir cartera se vuelve una optimización
cuadrática con solución geométrica transparente.

El aporte de Markowitz y Sharpe: si el inversor solo mira media y varianza, todo el
problema se ordena en el plano $(\sigma,\mu)$ y admite una teoría de equilibrio con
implicancias contrastables.

---

## 1. El supuesto media-varianza

El inversor evalúa $r_p$ por $V(\mu_p,\sigma_p)$, creciente en la media y decreciente
en el desvío. Es **exacto** en dos casos (vistos en la Unidad II): preferencias
cuadráticas, o rendimientos normales (o elípticos) con aversión al riesgo. En otros
casos es una aproximación de segundo orden.

## 2. Rendimiento y riesgo de una cartera

$$\mu_p = \mathbf{w}^\top\boldsymbol{\mu}, \qquad \sigma_p^2 = \mathbf{w}^\top\boldsymbol{\Sigma}\,\mathbf{w}$$

> 💡 La media de la cartera es un promedio ponderado **simple**; la varianza **no**.
> En $\sigma_p^2$ hay $N$ términos de varianza propia y $N(N-1)$ de covarianza. El
> riesgo de una cartera bien diversificada está gobernado por las covarianzas, no por
> las varianzas individuales. Ahí nace la diversificación.

**Por qué la covarianza domina.** Con $w_i=1/N$, varianza media $\bar\sigma^2$ y
covarianza media $\bar c$:

$$\sigma_p^2 = \frac{1}{N}\bar\sigma^2 + \left(1-\frac1N\right)\bar c \;\xrightarrow[N\to\infty]{}\; \bar c$$

El riesgo propio se desvanece; el de covarianza sobrevive. Si los activos fueran
independientes ($\bar c=0$) el riesgo tendería a cero: es exactamente la LGN y el
pooling de la Unidad III. Pero los rendimientos están positivamente correlacionados
(dependen del ciclo), de modo que $\bar c>0$ y queda un piso **no diversificable**.
Germen del riesgo sistemático.

## 3. Markowitz: la frontera eficiente

**Rechazo de la regla del valor presente esperado.** Si el inversor solo maximizara
el rendimiento esperado descontado, pondría **toda** su riqueza en el activo de mayor
valor esperado. Esa regla **nunca implica diversificar**; como la diversificación es
observada y sensata, la regla debe rechazarse tanto como hipótesis descriptiva como
norma de conducta. La covarianza —ausente en esa regla— es lo que hace deseable
repartir.

**Caso de dos activos y el papel de la correlación:**

| $\rho_{12}$ | $\sigma_p$ | Interpretación |
|---|---|---|
| $+1$ | $\lvert w\sigma_1+(1-w)\sigma_2\rvert$ — recta | Sin ganancia por diversificar |
| $-1$ | $\lvert w\sigma_1-(1-w)\sigma_2\rvert$ — se anula en $w=\sigma_2/(\sigma_1+\sigma_2)$ | Cobertura perfecta: cartera sin riesgo |
| $-1<\rho<1$ | Hipérbola combada hacia la izquierda | Riesgo menor que el de cualquier activo solo |

**Frontera con $N$ activos.** Con $A=\mathbf 1^\top\Sigma^{-1}\mu$,
$B=\mu^\top\Sigma^{-1}\mu$, $C=\mathbf 1^\top\Sigma^{-1}\mathbf 1$, $D=BC-A^2>0$:

$$\sigma_p^2 = \frac{C\mu_p^2 - 2A\mu_p + B}{D}$$

Una **hipérbola** en el plano $(\sigma,\mu)$. Su vértice es la cartera de mínima
varianza global:

$$\mu_{\rm GMV} = \frac AC, \qquad \sigma_{\rm GMV}^2 = \frac1C, \qquad \mathbf w_{\rm GMV} = \frac{\Sigma^{-1}\mathbf 1}{C}$$

La rama superior ($\mu_p \ge \mu_{\rm GMV}$) es la frontera eficiente.

**Derivación** (Anexo A de las notas): Lagrangiano con las restricciones de
presupuesto y rendimiento objetivo; $\mathbf w = \Sigma^{-1}(\lambda\mu+\gamma\mathbf 1)$
con $\lambda=(C\mu_p-A)/D$ y $\gamma=(B-A\mu_p)/D$.

## 4. Activo libre de riesgo y separación de Tobin

Combinando el activo seguro con una cartera riesgosa $T$:

$$\mu_p = r_f + \frac{\mu_T-r_f}{\sigma_T}\,\sigma_p$$

una **recta**. El inversor quiere la de mayor pendiente: la tangente a la frontera.

**Teorema de separación (Tobin, 1958).** Todo inversor media-varianza elige una
combinación del **mismo** portafolio riesgoso tangente $T$ y del activo seguro. La
composición de la parte riesgosa es igual para todos; solo cambia la proporción según
la aversión.

$$\mathbf w_T \propto \Sigma^{-1}(\boldsymbol\mu - r_f\mathbf 1)$$

> 💡 La decisión se dicotomiza: primero **qué** cartera riesgosa (problema técnico,
> igual para todos), después **cuánto** arriesgar (problema de gustos). La aversión al
> riesgo no afecta la composición, solo la proporción.

**Línea del Mercado de Capitales (CML)**, válida solo para carteras eficientes:

$$\mu_p = r_f + \frac{\mu_M-r_f}{\sigma_M}\,\sigma_p$$

Ordenada al origen $r_f$ = precio del tiempo; pendiente (ratio de Sharpe del mercado)
= precio del riesgo.

## 5. El CAPM de Sharpe

**Supuestos**: (i) inversores media-varianza aversos, horizonte común de un período;
(ii) **expectativas homogéneas**; (iii) existe $r_f$ para prestar y pedir prestado;
(iv) mercados competitivos sin fricciones.

Bajo expectativas homogéneas todos calculan la misma frontera y el mismo tangente. Si
todos compran $T$, en el agregado $T$ debe contener todos los activos en proporción a
su valor de mercado: **el tangente es el portafolio de mercado $M$**.

$$\boxed{\ \mu_i = r_f + \beta_i(\mu_M - r_f)\ }, \qquad \beta_i = \frac{\mathrm{Cov}(r_i,r_M)}{\mathrm{Var}(r_M)}$$

La **Línea del Mercado de Títulos (SML)** es esta recta en el plano $(\beta,\mu)$.

**Derivación** (Anexo B): carteras que combinan $i$ con $M$; se evalúan
$d\mu/da$ y $d\sigma/da$ en $a=0$ y se iguala la pendiente resultante con la de la CML.

**Descomposición del riesgo.** De $r_i = \alpha_i + \beta_i r_M + \varepsilon_i$ con
$\mathrm{Cov}(r_M,\varepsilon_i)=0$:

$$\underbrace{\sigma_i^2}_{\text{total}} = \underbrace{\beta_i^2\sigma_M^2}_{\text{sistemático}} + \underbrace{\sigma_{\varepsilon_i}^2}_{\text{no sistemático}}$$

> 💡 **Solo se paga el riesgo que no se puede evitar.** Como el mercado no recompensa
> un riesgo que el inversor puede anular gratis diversificando, el premio depende
> únicamente de $\beta_i$, no del riesgo total $\sigma_i$. Ésta es la respuesta de
> Sharpe a la pregunta que la teoría dejaba abierta: *cuál* componente del riesgo
> determina el precio de un activo.

**Nota sobre la notación original de Sharpe (1964).** Llama $P$ a la tasa pura de
interés, escribe la CML como $\sigma_R=S(E_R-P)$, no habla de «portafolio de mercado»
sino de una combinación eficiente cualquiera $g$, y denota $B_{ig}$ a nuestro
$\beta_i$. Un resultado central de su paper es que **todas** las combinaciones
eficientes están perfectamente correlacionadas entre sí, lo que justifica tomar
cualquiera —en particular el mercado— como referencia. La forma moderna se consolidó
con Lintner (1965) y Mossin (1966).

## 6. Mercados de futuros

No cubiertos por Markowitz ni Sharpe; se desarrollan con Hull (2018) y Varian (1992).
Son un segundo instrumento para transferir riesgo.

**Contrato de futuros**: acuerdo estandarizado y negociado en mercado organizado para
comprar (posición **larga**) o vender (**corta**) un subyacente en $T$ a un precio
$F_0$ pactado hoy. A diferencia del *forward*, se ajusta a mercado diariamente y
tiene cámara compensadora.

**Dos funciones económicas**: *cobertura* (el expuesto toma posición de signo opuesto
y fija su precio) y *especulación* (el no expuesto absorbe el riesgo que el
coberturista cede y aporta liquidez). Son las dos caras del reparto del riesgo.

**Cost-of-carry**: $F_0 = S_0 e^{(r+u-y)T}$, con $u$ costo de almacenamiento y $y$
rendimiento de conveniencia. **Contango** si $F_0>S_0$; ***backwardation*** si
$F_0<S_0$. La *normal backwardation* de Keynes: si los coberturistas están netos
cortos, los especuladores largos exigen prima y $F_0$ queda por debajo de $E[S_T]$.

**Cobertura de varianza mínima**:

$$h^\star = \rho_{SF}\,\frac{\sigma_S}{\sigma_F} = \frac{\mathrm{Cov}(\Delta S,\Delta F)}{\mathrm{Var}(\Delta F)}$$

que es formalmente el $\beta$ del spot respecto del futuro. Con $\rho_{SF}=1$ se
reproduce el caso $\rho=-1$ de dos activos: cancelación perfecta.

## 7. Puente con los derechos contingentes

Un activo con pagos $d_i(s)$ es una combinación de valores de Arrow. Con tantos
activos linealmente independientes como estados, el mercado es **completo**
(*spanning*) y reaparecen los precios de estado de la Unidad III.

De $q=E[m\,x]$, reescrito en rendimientos:

$$\mu_i - r_f = -\,r_f\,\mathrm{Cov}(m, r_i)$$

El CAPM es el caso en que el factor de descuento es lineal en el mercado,
$m = a - b\,r_M$: entonces la covarianza con $m$ se traduce en covarianza con el
mercado. **Markowitz-Sharpe y Arrow-Borch son dos lecturas del mismo problema.**

---

## Qué hace el notebook

### Figuras

| Figura | Contenido |
|---|---|
| `fig:dosactivos` | Tres curvas $(\sigma_p,\mu_p)$ para $\rho=+1,0,-1$ con $\mu=(8,15)\%$, $\sigma=(12,25)\%$ |
| Bala de Markowitz | Nube de carteras aleatorias + frontera analítica + GMV |
| CML | Frontera, activo seguro, recta tangente y portafolio tangente marcado |
| `fig:sml` | SML con $r_f=4\%$, $\mu_M=10\%$, más un activo infravalorado y uno sobrevalorado |
| Diversificación | $\sigma_p$ vs. $N$ para varios niveles de correlación media, mostrando el piso $\sqrt{\bar c}$ |
| Cobertura | Distribución del resultado con y sin futuros, para ver la reducción de varianza |

### Simulaciones

- **Monte Carlo de carteras**: 20 000 carteras aleatorias (Dirichlet) sobre la nube
  factible, coloreadas por ratio de Sharpe, con la frontera analítica encima. Verifica
  visualmente que ninguna cartera queda a la izquierda de la frontera.
- **Verificación numérica de la frontera**: resolver el problema con
  `scipy.optimize.minimize` para varios $\mu_p$ objetivo y comprobar que coincide con
  la fórmula cerrada $A,B,C,D$ hasta $10^{-8}$.
- **Widget**: deslizador de $\rho_{12}$ mostrando la frontera combarse.
- **Widget**: deslizador de $N$ y de correlación media mostrando el piso no
  diversificable.
- Ejemplo empírico con `data/retornos_ejemplo.csv`: estimar $\mu$ y $\Sigma$,
  construir la frontera y comparar con la teórica.

### Ejercicios de la guía (9)

1. Dos activos, $\rho=0{,}2$: $\mu_p=13{,}2\%$, $\sigma_p=16{,}38\%$ frente al
   promedio ponderado de desvíos, 21 %.
2. GMV de dos activos: $w_A^*=0{,}857$, $\mu=11{,}14\%$, $\sigma=14{,}34\%$ (menor que
   el activo menos riesgoso).
3. $\rho=-1$: $w_1=0{,}625$, $\sigma_p=0$, $\mu_p=10{,}25\%$, que por no arbitraje
   debe ser $r_f$.
4. Tres activos independientes: $\mathbf w_{\rm GMV}=(0{,}590,\ 0{,}262,\ 0{,}148)$,
   $\mu=8{,}23\%$, $\sigma=15{,}37\%$.
5. Tangente con $r_f=3\%$: $\mathbf w_T=(0{,}339,\ 0{,}351,\ 0{,}310)$,
   $\mu_T=9{,}89\%$, $\sigma_T=17{,}63\%$, Sharpe $=0{,}391$, CML $\mu_p=3\%+0{,}391\sigma_p$.
6. CAPM: $\beta=0{,}75$, $\mu_i=8{,}25\%$; proyección de 9 % ⟹ $\alpha=+0{,}75\%$,
   infravalorado.
7. Descomposición con $\beta=1{,}2$, $\sigma_i=28\%$, $\sigma_M=18\%$:
   sistemático $0{,}046656$, idiosincrático $0{,}031744$, $R^2=59{,}5\%$.
8. Cobertura: $h^*=0{,}964$, 10 contratos cortos, $\sigma$ cae de 3 % a 1,31 %
   (reducción de varianza del 81 % $=\rho^2$).
9. Del SDF al CAPM: $E[R_i]-R_f = -R_f\mathrm{Cov}(m,R_i)$; con $m=a-bR_M$ se recupera
   la beta. Verificación numérica: $\beta=0{,}75 \Rightarrow 8{,}25\%$, idéntico al
   ejercicio 6.

### Funciones de `eri_utils` que usa

`momentos_cartera`, `frontera_abcd`, `frontera_sigma`, `cartera_gmv`,
`cartera_tangente`, `ratio_sharpe`, `beta_capm`, `capm`, `descomposicion_riesgo`,
`hedge_ratio`.

### Conexión con la unidad siguiente

La Unidad V lleva la incertidumbre al lado de la **producción**: cómo una firma
neutral, una aversa y una con función tipo Markowitz eligen su nivel de producción
cuando el precio es aleatorio, y cómo se rompe la regla «precio igual a costo
marginal».
