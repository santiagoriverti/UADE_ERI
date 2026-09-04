# Unidad V — La Firma Competitiva bajo Incertidumbre

**Clase 5 (02/09)** · Notebook `05_unidad_V_firma_incertidumbre.ipynb`
**Fuente**: `latex/clase_05_unidad_V.tex` · Sandmo (1971)
**Estado**: notas escritas · notebook pendiente

---

## De qué se trata

Cierra el bloque de riesgo llevando la incertidumbre al lado de la **producción**.
Bajo certeza, la teoría del productor competitivo se resume en «producir hasta que el
precio iguale al costo marginal». Esta unidad muestra cómo esa regla **se disuelve**
cuando el precio de venta es incierto y la firma es aversa.

La alteración es mínima pero de consecuencias profundas: cambia el **orden temporal**.
La firma fija su producción *antes* de que el precio se realice —el agricultor decide
cuánto sembrar meses antes de la cosecha—, de modo que al decidir, $p$ es una variable
aleatoria.

> 💡 Casi todas las «neutralidades» cómodas de la teoría del productor —la
> irrelevancia de los costos fijos, la del impuesto proporcional, la anulación del
> beneficio en el largo plazo— son propiedades del mundo de certeza. La incertidumbre,
> mediada por la aversión al riesgo, las convierte en predicciones sustantivas y
> contrastables.

---

## 1. El modelo

$$\max_{x\ge0}\ E\!\left[U\!\left(p\,x - C(x) - B\right)\right]$$

con $C(0)=0$, $C'(x)>0$ (**no** se exige costo marginal creciente), $p\ge0$ aleatorio
con $E[p]=\mu$, y $U'>0$, $U''<0$.

La firma sigue siendo **precio-aceptante en sentido probabilístico**: no influye sobre
la distribución de $p$, solo la toma como dada.

**Producto de certeza** $x_c$, la vara de comparación permanente: $C'(x_c)=\mu$.

## 2. Firma neutral al riesgo

Con $U$ lineal, maximizar utilidad esperada equivale a maximizar beneficio esperado:

$$C'(x) = \mu = E[p] \quad\Longrightarrow\quad x^* = x_c$$

**La neutralidad colapsa el problema estocástico en su promedio.** La regla de
certeza sobrevive intacta, con $\mu$ en lugar del precio conocido, y la varianza del
precio es **irrelevante**. Toda la acción aparece recién con la aversión.

## 3. El resultado central de Sandmo

**CPO y CSO:**

$$E[U'(\pi)(p-C'(x))] = 0, \qquad D \equiv E[U''(\pi)(p-C'(x))^2 - U'(\pi)C''(x)] < 0$$

> ⚠️ Notable: como $U''<0$, el primer término de la CSO ya es negativo, de modo que
> **no hace falta suponer costo marginal creciente** para que la condición se cumpla.
> La aversión al riesgo, por sí sola, «convexifica» el problema.

**Teorema.** Si la firma es aversa y el óptimo es interior, entonces

$$\boxed{\ C'(x^*) < \mu\ }$$

y con costo marginal creciente, $x^* < x_c$.

**La demostración** (que el notebook debe reproducir paso a paso). De la CPO, restando
$E[U'(\pi)\mu]$:

$$E[U'(\pi)(p-\mu)] = E[U'(\pi)]\,(C'(x)-\mu)$$

Como $\pi = E[\pi] + (p-\mu)x$ con $x\ge0$ y $U'$ decreciente, se cumple
$p \gtrless \mu \Rightarrow U'(\pi) \lessgtr U'(E[\pi])$. Multiplicando por $(p-\mu)$
se obtiene, **para todo** $p$ (los dos signos se compensan):

$$U'(\pi)(p-\mu) \le U'(E[\pi])(p-\mu)$$

Tomando esperanza, el lado derecho se anula porque $E[p-\mu]=0$. Luego el lado
izquierdo de la primera igualdad es negativo y, como $E[U'(\pi)]>0$, resulta
$C'(x^*)<\mu$.

**Interpretación.** Las últimas unidades producidas son las que más exponen a la
firma: cada unidad adicional multiplica el impacto de la sorpresa de precio sobre el
beneficio. La firma aversa **se autocubre recortando producción**. La brecha
$\mu - C'(x^*) > 0$ es una **prima marginal de riesgo**: el margen esperado extra que
exige sobre el costo marginal para compensar el riesgo que soporta en el margen.

La incertidumbre de precios opera como un **impuesto implícito a la producción**.

## 4. CARA-Normal: el caso resoluble

Con $U(\pi)=-e^{-a\pi}$ y $p\sim N(\mu,\sigma^2)$, el beneficio es normal y

$$\mathrm{EC}(x) = E[\pi] - \frac a2\mathrm{Var}(\pi) = \mu x - C(x) - B - \frac a2 x^2\sigma^2$$

CPO: $C'(x) = \mu - a\sigma^2 x < \mu$. Con $C(x)=\tfrac c2 x^2$:

$$x^* = \frac{\mu}{c + a\sigma^2} \;<\; \frac\mu c = x_c$$

Con $\mu=10$, $c=1$, $a=1$, $\sigma^2=1$: $x_c=10$ y $x^*=5$. **La incertidumbre
reduce el producto a la mitad**, y la prima marginal es $a\sigma^2 x^*=5$.

> ⚠️ CARA-Normal es una aproximación tratable: la normal asigna probabilidad positiva
> a precios negativos, en tensión con $p\ge0$ y con el acotamiento de $U$. Se usa por
> su transparencia analítica.

## 5. Firma tipo Markowitz (media-varianza)

$$V(x) = E[\pi] - \frac\rho2\mathrm{Var}(\pi) = \mu x - C(x) - B - \frac\rho2\sigma^2 x^2$$

$$\boxed{\ C'(x) = \mu - \rho\,\sigma^2 x\ }$$

El término $\rho\sigma^2 x$ es el **costo marginal de riesgo**. La firma iguala el
precio esperado a la suma del costo marginal de producción y el costo marginal de
riesgo. Con costo cuadrático, $x^* = \mu/(c+\rho\sigma^2)$.

**No es un supuesto ad hoc**: bajo CARA-Normal el criterio media-varianza coincide
*exactamente* con la utilidad esperada, con $\rho = a$.

**Estática comparada:**

$$\frac{\partial x^*}{\partial\sigma^2} < 0, \qquad \frac{\partial x^*}{\partial\rho} < 0, \qquad \frac{\partial x^*}{\partial\mu} > 0$$

En el límite $\rho\to0$ se recupera $x^*\to x_c$.

**Utilidad cuadrática y oferta que se dobla hacia atrás.** Sandmo señala (nota 6) que
con $U(\pi)=\pi-\tfrac b2\pi^2$ y costo marginal constante, la oferta puede doblarse
hacia atrás para precios esperados altos: la utilidad cuadrática genera aversión
absoluta *creciente*, de modo que el $\rho$ efectivo aumenta con el beneficio
esperado. Recordatorio de que la constancia de $\rho$ es cómoda pero no inocua.

## 6. Estática comparada de la firma aversa general

Se necesita restringir cómo varía la aversión con la riqueza. El supuesto
empíricamente razonable es **DARA** (aversión absoluta decreciente).

**Los costos fijos sí importan.**

$$\frac{\partial x^*}{\partial B} = \frac1D\,E[U''(\pi)(p-C'(x))]$$

**Proposición.** DARA es condición necesaria y suficiente para que
$\partial x^*/\partial B < 0$: un aumento del costo fijo **reduce** el producto.
Lectura de política: bajo DARA, un subsidio de suma fija aumenta el producto, porque
enriquece a la firma y baja su aversión efectiva en el margen.

> En el modelo media-varianza $\partial x^*/\partial B = 0$, y es **coherente**: el
> criterio media-varianza equivale a CARA (aversión absoluta *constante*), el caso
> frontera entre DARA e IARA. Los costos fijos importan solo cuando la aversión
> *cambia* con la riqueza.

**Ecuación tipo Slutsky.** Desplazando la distribución del precio ($p+\theta$):

$$\frac{\partial x^*}{\partial\theta} = \underbrace{-x^*\frac{\partial x^*}{\partial B}}_{\text{«riqueza»}} \;\underbrace{-\frac1D E[U'(\pi)]}_{\text{sustitución} > 0}$$

Bajo DARA ambos términos son positivos ⟹ **oferta con pendiente positiva**.

**Impuesto proporcional a las ganancias.** Con compensación plena de pérdidas,
$\pi_t=(px-C(x)-B)(1-t)$ y el factor $(1-t)$ se cancela: la CPO es *invariante en su
forma*. Pero $t$ reescala todos los beneficios y desplaza a la firma a otro tramo de
su función de aversión. **Proposición**: un aumento de $t$ aumenta, deja constante o
reduce el producto según que la aversión **relativa** $R_R$ sea creciente, constante o
decreciente.

## 7. Beneficios, entrada y equilibrio de largo plazo

**Existencia.** Bajo certeza el costo marginal creciente es necesario para que exista
óptimo competitivo; bajo incertidumbre no lo es (la concavidad y el acotamiento de $U$
bastan aun con $C''=0$). El caso delicado es costo marginal siempre decreciente.

**Solución interior vs. esquina.** La firma produce si
$E[U(\pi(x^*))] > U(-B)$. Desarrollando en Taylor:

$$\frac{U(E[\pi])-U(-B)}{U'(E[\pi])} \ \ge\ \frac12 R_A(E[\pi])\,(x^*)^2\sigma^2$$

El lado derecho es positivo, luego el izquierdo también, luego $E[\pi] > -B$, es decir

$$\boxed{\ \mu > \frac{C(x^*)}{x^*}\ }$$

**el precio esperado debe superar al costo medio**: la firma exige un beneficio
esperado **estrictamente positivo** para producir.

**Teorema.** Bajo incertidumbre de precios y aversión al riesgo, el equilibrio
competitivo requiere beneficios esperados positivos.

**Entrada y concentración.** Una firma casi neutral entra ante cualquier beneficio
esperado positivo; una muy aversa no entra o es marginal. El beneficio es mayor para
las firmas más cercanas a la neutralidad, que además producen más: **el beneficio es
retribución al riesgo asumido**. Y si el costo marginal es constante o decreciente y
unas pocas firmas son mucho menos aversas, pueden elegir producciones muy grandes,
deprimir el precio esperado y expulsar al resto: **la distribución desigual de la
aversión al riesgo es, por sí sola, una fuente de concentración oligopólica.**

## 8. El cuadro de síntesis

| Rasgo | Certeza | Neutral | Aversa / Markowitz |
|---|---|---|---|
| Objetivo | $\max\pi$ | $\max E[\pi]$ | $\max E[U(\pi)]$ |
| Condición óptima | $p=C'(x)$ | $\mu=C'(x)$ | $C'(x)=\mu-\text{prima}<\mu$ |
| Producto vs. $x_c$ | $x_c$ | $x_c$ | $x^*<x_c$ |
| Costo fijo $B$ | irrelevante | irrelevante | $\partial x/\partial B<0$ (DARA) |
| Impuesto proporcional | neutral | neutral | signo de $R_R$ |
| Beneficio de largo plazo | 0 | 0 | $>0$ |

---

## Qué debe hacer el notebook

### Figuras a reproducir

| Figura | Cómo |
|---|---|
| `fig:reduccion` | $C'(x)$ creciente, línea horizontal en $\mu$, marcar $x_c$ y $x^*$, llave para la prima marginal |
| `fig:oferta` | Oferta inversa de certeza ($\mu=cx$) vs. aversa ($\mu=(c+\rho\sigma^2)x$), más empinada |
| Equivalente cierto | $\mathrm{EC}(x)$, $E[\pi(x)]$ y el descuento por riesgo, los tres sobre el mismo eje, mostrando dónde cae cada máximo |
| Oferta hacia atrás | Con utilidad cuadrática y costo marginal constante, la curva doblándose |

### Cálculos y simulaciones

- **Verificación Monte Carlo del teorema**: simular $p$ (normal, lognormal, uniforme,
  bimodal), resolver $\max E[U(\pi)]$ numéricamente con `scipy.optimize` para varias
  $U$ y comprobar que **siempre** $C'(x^*)<\mu$. Que se cumpla con distribuciones muy
  distintas hace ver que el resultado no depende de la normalidad.
- Comparar el óptimo CARA-Normal analítico con el numérico: deben coincidir.
- **Widget**: deslizadores de $\sigma^2$ y $\rho$ mostrando $x^*$ cayendo y la oferta
  rotando.
- **Costos fijos**: comparar numéricamente $\partial x^*/\partial B$ bajo CARA (cero),
  CRRA/DARA (negativo) e IARA (positivo). Es la mejor manera de que se entienda que el
  signo depende de la *forma* de la aversión, no de su nivel.
- Impuesto proporcional: barrer $t$ para utilidades con $R_R$ creciente, constante y
  decreciente, mostrando los tres signos.

### Ejercicios de la guía (6)

1. Firma neutral, $C=\tfrac12x^2$, $p\in\{6,14\}$: $\mu=10$, $x^*=10=x_c$,
   $E[\pi]=50-B$. La varianza (16) no interviene.
2. Demostración del resultado central.
3. CARA-Normal con $\mu=12$, $c=1$, $a=2$, $\sigma^2=1$: $x_c=12$, $x^*=4$, prima
   marginal 8.
4. Media-varianza: $x^*=\mu/(c+\rho\sigma^2)$, los tres signos, límite $\rho\to0$.
5. $\partial x^*/\partial B = 0$ en media-varianza y por qué es consistente con
   Sandmo (CARA es el caso frontera).
6. Impuesto proporcional e invariancia de la CPO; con $B=0$, $\mu=10$, $c=1$,
   $\rho=1$, $\sigma^2=1$: $x^*=5$, $E[\pi]=37{,}5$, descuento 12,5, $V=25>0$.

### Funciones de `eri_utils` que usa

`sandmo_media_varianza`, `producto_certeza`, `u_cara`, `u_crra`,
`arrow_pratt_absoluta`, `arrow_pratt_relativa`.

**Podría hacer falta agregar**: `sandmo_optimo_numerico(u, dist_precio, C, Cp)` para
resolver el caso general por integración numérica, que es lo que permite la
verificación Monte Carlo del teorema.

### Conexión con la unidad siguiente

Cierra el bloque de riesgo y el temario del primer parcial. La Unidad VI abre el
bloque de información: de un decisor solo frente al azar, a **varios agentes con
información distinta**.
