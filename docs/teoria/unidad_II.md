# Unidad II — Utilidad Esperada y Aversión al Riesgo

**Clase 2 (12/08)** · Notebook `02_unidad_II_utilidad_esperada.ipynb`
**Fuente**: `latex/clase_02_unidad_II.tex` · Varian cap. 11; Gravelle & Rees cap. 17
**Estado**: notas escritas · notebook pendiente

---

## De qué se trata

La Unidad I *usó* la utilidad esperada. Esta unidad la **funda**. Responde la
pregunta que quedó abierta: ¿por qué valuar una lotería por la esperanza de la
utilidad y no por su valor monetario esperado?

Dos niveles de respuesta. Histórico: San Petersburgo muestra que el valor esperado
falla. Axiomático: von Neumann-Morgenstern derivan la representación $E[u]$ de cuatro
axiomas sobre las preferencias. Sobre esa base se construyen las medidas de aversión
al riesgo comparables entre individuos (Arrow-Pratt) y se cierra volviendo a la
crítica, ahora con precisión quirúrgica: **qué axioma exactamente** rompe cada
paradoja.

---

## 1. San Petersburgo y el principio de Bernoulli

Se lanza una moneda hasta la primera cara. Si sale en el lanzamiento $n$, el jugador
cobra $x_n = 2^n$ con probabilidad $p_n = 2^{-n}$. El valor monetario esperado es

$$E[X] = \sum_{n=1}^{\infty} 2^{-n}\,2^{n} = \sum_{n=1}^{\infty} 1 = +\infty$$

Un decisor que valuara por valor esperado pagaría **cualquier** suma finita. Nadie
lo hace: el criterio predice mal.

**Resolución de Bernoulli (1738)**: la utilidad del dinero es creciente y cóncava, y
el decisor evalúa por utilidad esperada. Con $u(w)=\ln w$:

$$E[\ln X] = \ln 2 \sum_{n\ge1} n\,2^{-n} = 2\ln 2 = \ln 4 \quad\Rightarrow\quad \mathrm{CE} = 4 \text{ ducados}$$

Un valor esperado infinito se vuelve una disposición a pagar de 4 ducados.

**El límite de la resolución.** Menger (1934): basta hacer crecer los premios más
rápido ($x_n = e^{2^n}$) para que $E[\ln X]$ vuelva a divergir. La lección definitiva
es más fuerte: **para descartar estas paradojas con cualquier sucesión de premios, la
utilidad debe estar acotada**. Con $u(w)=1-e^{-w}$ se tiene $E[u(X)]<1$ *cualquiera
sea* la distribución de premios.

## 2. Loterías: el marco formal

$$p \circ x \oplus (1-p) \circ y$$

Tres supuestos de percepción: **certeza** ($1\circ x \oplus 0 \circ y = x$),
**irrelevancia del orden**, y **reducción de loterías compuestas** (solo importan las
probabilidades netas sobre premios finales).

> ⚠️ El supuesto de reducción no es inocuo: al colapsar las loterías compuestas en
> simples, borra cualquier valor que el decisor asigne al *proceso* de resolución del
> riesgo por etapas. Es exactamente lo que explota el efecto aislamiento de la Unidad I.

## 3. El teorema de von Neumann-Morgenstern

**Axiomas**: (1) preferencias racionales — completas y transitivas; (2) continuidad;
(3) **independencia**; (4) monotonía.

**Teorema.** Existe $u$ sobre los premios con la propiedad de utilidad esperada:
$U(\sum_i p_i \circ x_i) = \sum_i p_i\,u(x_i)$.

**Construcción de la prueba.** Sean $b$ la mejor lotería y $w$ la peor. Por
*continuidad*, para cada premio $x$ existe $p_x$ con $x \sim p_x \circ b \oplus
(1-p_x)\circ w$; por *monotonía* ese $p_x$ es único. Se **define** $u(x)=p_x$.
Sustituyendo cada premio por su lotería indiferente (lícito por *independencia*) y
reduciendo, la utilidad de una lotería resulta ser la probabilidad total con que
entrega $b$, es decir $q\,u(x)+(1-q)u(y)$.

**Unicidad (cardinalidad).** $u$ es única salvo transformación afín positiva:
$v = a\,u + c$ con $a>0$ representa las mismas preferencias, pero $v = u^3$ **no**.
Diferencia esencial con el consumidor bajo certeza, donde cualquier transformación
monótona sirve. Acá las diferencias de utilidad significan algo, porque están
ancladas a probabilidades de la lotería de referencia $\{b,w\}$.

## 4. Aversión al riesgo

**Definición.** Averso si $u(E[X]) > E[u(X)]$ para toda lotería no degenerada.

**Proposición.** Averso ⟺ $u$ cóncava. Es la desigualdad de Jensen, cuya prueba usa
que una función cóncava queda por debajo de cualquiera de sus tangentes:
$u(x) \le u(\bar x) + u'(\bar x)(x-\bar x)$; tomando $\bar x = E[X]$ y esperanza, el
término lineal se anula.

$$u(\mathrm{CE}(X)) = E[u(X)], \qquad \pi(X) = E[X] - \mathrm{CE}(X) > 0$$

**Conjunto de aceptación** (Varian): el conjunto de apuestas $(x_1,x_2)$ que el
decisor aceptaría a riqueza $w$. Si es averso, ese conjunto es **convexo**, y su
frontera tiene en $(0,0)$ pendiente $-p/(1-p)$. Da un método para **elicitar
probabilidades**: hallar las cuotas a las que el decisor está justo dispuesto a
aceptar una apuesta pequeña.

## 5. Medidas de Arrow-Pratt

**Por qué no basta $u''$**: no es invariante. Reemplazar $u$ por $a\,u+c$ no cambia
la conducta pero multiplica $u''$ por $a$. Dividiendo por $u'$ se normaliza.

$$r_A(w) = -\frac{u''(w)}{u'(w)}, \qquad r_R(w) = -\frac{w\,u''(w)}{u'(w)} = w\,r_A(w)$$

**Aproximación local de Pratt.** Con $\tilde\varepsilon$ de media cero y varianza
$\sigma^2$, de $u(w-\pi)=E[u(w+\tilde\varepsilon)]$, desarrollando el lado derecho a
**segundo** orden (a primer orden el riesgo desaparecería) y el izquierdo a primero:

$$\boxed{\ \pi \approx \tfrac12\, r_A(w)\,\sigma^2\ }$$

Esta fórmula *justifica* la medida y conecta aversión con varianza.

**Familias de referencia:**

| Familia | $u(w)$ | $r_A$ | $r_R$ | Comentario |
|---|---|---|---|---|
| CARA | $-e^{-aw}$ | $a$ constante | $aw$ creciente | Aversión relativa creciente: poco realista |
| CRRA | $\dfrac{w^{1-R}}{1-R}$ | $R/w$ decreciente | $R$ constante | DARA: empíricamente plausible. $R\to1 \Rightarrow \ln w$ |

**Teorema de Pratt (comparación global).** Para $A$ y $B$ crecientes y cóncavas,
son **equivalentes**:

1. $-A''/A' \ge -B''/B'$ para todo $w$;
2. $A = G \circ B$ con $G$ creciente y estrictamente cóncava;
3. $\pi_A(\tilde z) \ge \pi_B(\tilde z)$ para todo riesgo $\tilde z$ de media cero.

La prueba (1)⟹(2) sale de derivar dos veces $A=G(B)$; (2)⟹(3) es Jensen aplicada a
$G$; (3)⟹(1) es la aproximación de Pratt en el límite de riesgos pequeños.

**CARA-Normal y media-varianza.** Con $u(w)=-e^{-aw}$ y $w\sim N(\mu,\sigma^2)$,
usando la generatriz de momentos con $t=-a$:

$$E[u(w)] = -\exp\!\left[-a\left(\mu - \tfrac{a}{2}\sigma^2\right)\right]$$

Maximizar la utilidad esperada equivale a maximizar $\mu - \tfrac{a}{2}\sigma^2$.
**Este es el fundamento microeconómico del criterio media-varianza** que reaparece en
la Unidad IV (Markowitz) y en la V (firma tipo Markowitz). La utilidad cuadrática
también genera preferencias media-varianza, pero con inconvenientes (decreciente en
un tramo, aversión absoluta *creciente*); el par CARA-Normal es la justificación
limpia.

## 6. Aplicación: demanda de seguro

Riqueza $W$, pérdida $L$ con probabilidad $\pi$, cobertura $q$ a tasa de prima $p$:

$$w_1 = W - pq, \qquad w_2 = W - L + (1-p)q$$

CPO: $-p(1-\pi)u'(w_1) + (1-p)\pi u'(w_2) = 0$.

**Proposición.** Con prima actuarialmente justa ($p=\pi$) y aversión estricta, la CPO
se reduce a $u'(w_1)=u'(w_2)$; como $u'$ es estrictamente decreciente (inyectiva),
$w_1=w_2$, y por lo tanto $q^*=L$: **cobertura total**.

Con recargo ($p>\pi$) la cobertura óptima es **parcial**. Es el punto de partida de
toda la economía del seguro y el puente natural hacia el Teorema de Borch (Unidad III).

## 7. Las paradojas, con precisión

**Allais viola independencia.** Con $u(0)=0$:
$A\succ B \Rightarrow 0{,}11\,u_1 > 0{,}10\,u_5$ y
$D\succ C \Rightarrow 0{,}10\,u_5 > 0{,}11\,u_1$. Contradictorias. La raíz es una
«consecuencia común» (probabilidad 0,89 de un mismo premio) que pasa de 1 a 0 entre
los dos problemas y que, por independencia, no debería alterar el orden.

**Ellsberg viola la existencia de probabilidad subjetiva.** Urna con 90 bolas: 30
rojas, 60 negras o amarillas en proporción desconocida. La mayoría elige *roja* en la
apuesta I y *negra o amarilla* en la II. Si existieran $P(R)=1/3$, $P(N)=b$, $P(Y)=y$
con $b+y=2/3$, la primera elección da $1/3 > b$ y la segunda $b > 1/3$. Contradicción.

**La diferencia entre ambas.** Allais mantiene probabilidades *conocidas* y rompe un
axioma dentro del modelo de utilidad esperada. Ellsberg opera bajo *ambigüedad* y
rompe la existencia misma de una distribución subjetiva única. El fenómeno de fondo
es la **aversión a la ambigüedad**, que distingue riesgo de incertidumbre knightiana
y motiva los modelos *maxmin* con probabilidades múltiples.

---

## Qué debe hacer el notebook

### Figuras a reproducir

| Figura | Cómo |
|---|---|
| `fig:aversion` | $u(w)=1{,}85\sqrt w$, cuerda entre $(1,\cdot)$ y $(8,\cdot)$, marcar $E[X]=4{,}5$, CE y llave de $\pi$ en oro |
| Convergencia de San Petersburgo | Media muestral del juego vs. $n$ de repeticiones, en escala log: nunca converge |
| Familias CARA vs CRRA | $r_A(w)$ y $r_R(w)$ para ambas, sobre el mismo eje |
| Seguro | $(w_1,w_2)$ con recta de apuestas justas, presupuesto con recargo, línea de certeza y óptimo |

### Cálculos y simulaciones

- **San Petersburgo por Monte Carlo**: simular $10^6$ partidas y graficar la media
  acumulada. Se ve que no converge —la media muestral salta con cada realización
  extrema—, lo que hace tangible la divergencia teórica.
- Verificar $E[\ln X] = \ln 4$ sumando la serie numéricamente y comparar con
  `sympy.summation`.
- **Cardinalidad**: contraejemplo numérico con $u \in \{0,1,2\}$ y $v=u^3$ mostrando
  que la indiferencia $L\sim x_2$ se vuelve preferencia estricta.
- **Widget**: deslizador del coeficiente de aversión ($a$ de CARA o $R$ de CRRA)
  mostrando cómo se separan $E[X]$ y CE.
- Precisión de la aproximación de Pratt: comparar prima exacta vs. aproximada como
  función de $\sigma$, para ver dónde se rompe.
- Barrido numérico que confirma que ninguna $u$ racionaliza Allais.

### Ejercicios de la guía (10)

1. San Petersburgo: (a) divergencia; (b) $E[\ln X]=\ln 4$, CE $=4$; (c) con
   $u=1-e^{-w}$, $E[u(X)]\approx0{,}928$ y CE $\approx 2{,}63$.
2. Teorema de utilidad esperada: continuidad da existencia de $p_x$, monotonía la
   unicidad; independencia permite la reducción.
3. Cardinalidad: $v=a u+c$ sirve, $v=u^3$ no. Contraejemplo numérico.
4. $u=\sqrt w$, lotería $(0{,}5;\,36,\,100)$: $E[X]=68$, $E[u]=8$, CE $=64$,
   $\pi=4$. Pratt: $r_A(68)=1/136$, $\sigma^2=1024$, $\pi\approx3{,}76$ (94 % de la
   prima exacta; la brecha es porque el riesgo no es pequeño).
5. Derivación de la aproximación de Pratt.
6. $A(w)=-e^{-2w}$, $B(w)=-e^{-w}$: $r_A^A=2 > r_A^B=1$; $G(B)=-B^2$, creciente y
   cóncava sobre $B<0$.
7. CARA-Normal: $E[u]=-\exp[-a(\mu-\tfrac a2\sigma^2)]$; $a$ es el precio del riesgo.
8. Seguro con $u=\ln w$, $W=100$, $L=51$, $\pi=1/3$: con prima justa $q^*=51$ y
   riqueza cierta 83; con $p=0{,}4$, $w_2/w_1=0{,}75$ y $q^*=260/9\approx28{,}9$.
9. Allais: las dos desigualdades y el axioma violado.
10. Ellsberg: las dos desigualdades y la diferencia con Allais.

### Funciones de `eri_utils` que usa

`u_log`, `u_sqrt`, `u_crra`, `u_cara`, `u_lineal`, `utilidad_esperada`,
`equivalente_cierto`, `prima_riesgo`, `arrow_pratt_absoluta`,
`arrow_pratt_relativa`, `prima_pratt`, `riquezas_contingentes`, `cobertura_optima`.

### Conexión con la unidad siguiente

Esta unidad cierra con un decisor aislado que se asegura. La Unidad III abre el
análisis a la **interacción**: cómo el riesgo se reasigna entre agentes generando
mejoras de Pareto. La cobertura total a prima justa, leída en el espacio de rentas
contingentes, es el puente directo al Teorema de Borch.
