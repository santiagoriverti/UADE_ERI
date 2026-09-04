# Unidad IX — Señalización

**Clase 12 (14/10)** · Notebook `09_unidad_IX_senalizacion.ipynb`
**Bibliografía**: Macho-Stadler & Pérez Castrillo cap. 5; Spence (1973)
**Estado**: ⚠️ **notas de clase pendientes** · notebook pendiente

> ⚠️ Alcance previsto, reconstruido del programa y la bibliografía. Cuando existan
> las notas en `latex/clase_12_unidad_IX.tex`, ellas mandan y este archivo se reescribe.

---

## De qué se trata

Mismo problema informacional que la Unidad VIII —el agente conoce su tipo, el
principal no— pero **invertido el orden de juego**: mueve primero el **informado**,
emitiendo una señal costosa y observable antes de contratar.

La pregunta es cuándo una señal puede ser creíble. La respuesta de Spence (1973) es
elegante y algo perturbadora: la señal es creíble **si y solo si es más barata para
los buenos tipos**, y esto funciona aunque la señal no produzca absolutamente nada de
valor.

---

## 1. Secuencia temporal

```
1. La naturaleza asigna el tipo θ (solo el agente lo observa)
2. El agente elige la señal s (educación), observable y costosa
3. Las empresas observan s, forman creencias μ(θ|s) y compiten ofreciendo salarios
4. El agente acepta y produce
```

Es un juego dinámico con información incompleta. El concepto de solución es el
**equilibrio bayesiano perfecto**: estrategias óptimas dadas las creencias, y creencias
consistentes con las estrategias vía Bayes en los caminos que se juegan.

## 2. El modelo de Spence

Dos tipos con productividades $\theta_H > \theta_L$, en proporciones $q$ y $1-q$. El
costo de la señal es $c(s,\theta) = s/\theta$: **decreciente en el tipo**. La educación
**no aumenta la productividad**: no es capital humano, es puro señalizador.

**Condición de cruce único (Spence-Mirrlees)**: $\partial^2 c/\partial s\,\partial\theta < 0$.
Al tipo alto le cuesta menos cada unidad de señal. Es la condición que hace posible la
separación, y es la misma que en la Unidad VIII.

## 3. Equilibrio separador

Cada tipo elige una señal distinta y el mercado los distingue perfectamente:
$s_L^* = 0$, $s_H^* = s^*$, con salarios $w = \theta_L$ y $w = \theta_H$.

El nivel $s^*$ debe satisfacer **dos** condiciones simultáneas:

$$\theta_L \ \ge\ \theta_H - \frac{s^*}{\theta_L} \qquad \text{(al tipo bajo no le conviene imitar)}$$
$$\theta_H - \frac{s^*}{\theta_H} \ \ge\ \theta_L \qquad \text{(al tipo alto le conviene señalizar)}$$

lo que define un **intervalo** $[\underline s, \overline s]$ de niveles de señal
compatibles con equilibrio separador. **Hay un continuo de equilibrios**: es un
problema, no un detalle.

> 💡 **El resultado incómodo.** En el equilibrio separador se gasta en educación un
> costo real, y esa educación **no produce nada**. Es puro desperdicio social: el tipo
> alto está peor que bajo información completa (donde cobraría $\theta_H$ sin gastar
> nada), y el bajo está igual. La señalización resuelve el problema informacional
> **quemando recursos**. Discutir esto honestamente en clase es lo que hace valiosa la
> unidad; también conviene contrastarlo con la visión de capital humano, donde la
> educación sí es productiva, y señalar que empíricamente separar ambos efectos es una
> agenda de investigación abierta (Altonji-Pierret, efecto *sheepskin*).

## 4. Equilibrio agrupador

Todos eligen la misma señal (típicamente $s=0$) y cobran el salario correspondiente a
la productividad media $\bar\theta = q\theta_H + (1-q)\theta_L$. También es un
equilibrio bayesiano perfecto, sostenido por **creencias fuera del equilibrio**
suficientemente pesimistas (por ejemplo, «quien se desvíe es de tipo bajo»).

## 5. Refinamientos

La multiplicidad es el problema central de los modelos de señalización, y hay que
mostrarlo, no esconderlo. **Criterio intuitivo (Cho-Kreps)**: elimina los equilibrios
sostenidos por creencias que asignan probabilidad positiva a que se desvíe un tipo para
el que ese desvío **nunca** podría ser rentable. Aplicado al modelo de Spence,
selecciona el equilibrio separador **menos costoso** ($s^* = \underline s$) y elimina
los agrupadores.

Vale la pena presentarlo como lo que es: un criterio razonable pero no incontrovertible,
y un ejemplo de cómo la teoría de juegos disciplina la multiplicidad a costa de sumar
supuestos.

## 6. Aplicaciones

- **Dividendos** como señal de calidad de la firma (costosos por vía impositiva).
- **Estructura de capital**: la deuda señaliza confianza porque quebrar es costoso.
- **Garantías**: solo el fabricante de un producto bueno puede ofrecerlas barato.
- **Publicidad disipativa**: gastar mucho señaliza que se espera vender mucho.
- **Señalización costosa en biología**: la cola del pavo real (Zahavi) — el mismo
  principio matemático, y una buena manera de mostrar la generalidad del argumento.

---

## Qué debería hacer el notebook

### Contenido mínimo

1. **Gráfico canónico de Spence**: plano $(s, w)$ con las curvas de indiferencia de
   ambos tipos, la recta de salario separador y el intervalo $[\underline s,
   \overline s]$ sombreado. Es la figura que hay que saber dibujar en el parcial.
2. **Cálculo del intervalo de equilibrios separadores** y verificación numérica de las
   dos desigualdades.
3. **Comparación de bienestar**: separador vs. agrupador vs. información completa, por
   tipo y agregado. Debe verse el desperdicio.
4. **Widget**: deslizadores de $q$ (proporción de tipos altos) y de la brecha
   $\theta_H-\theta_L$, mostrando cómo se mueven el intervalo separador y el atractivo
   relativo del agrupador. Con $q$ alto el agrupador puede dominar en bienestar, lo
   cual es un buen disparador de discusión.
5. **Violación del cruce único**: mostrar que si el costo no es decreciente en el tipo,
   la separación es imposible. Aísla cuál es exactamente el supuesto que hace funcionar
   todo.
6. **Aplicación del criterio intuitivo** paso a paso sobre un equilibrio agrupador
   concreto, mostrando qué desvío lo rompe.

### Funciones nuevas para `eri_utils`

```python
spence_intervalo_separador(theta_L, theta_H)
spence_bienestar(...)      # compara separador, agrupador e informacion completa
cruce_unico(...)           # verifica la condicion de Spence-Mirrlees
```
