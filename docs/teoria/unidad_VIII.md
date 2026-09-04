# Unidad VIII — Selección Adversa

**Clase 11 (07/10)** · Notebook `08_unidad_VIII_seleccion_adversa.ipynb`
**Bibliografía**: Macho-Stadler & Pérez Castrillo cap. 4; Akerlof (1970)
**Estado**: ⚠️ **notas de clase pendientes** · notebook pendiente

> ⚠️ Alcance previsto, reconstruido del programa y la bibliografía. Cuando existan
> las notas en `latex/clase_11_unidad_VIII.tex`, ellas mandan y este archivo se reescribe.

---

## De qué se trata

**Información oculta anterior al contrato.** El agente conoce su propio **tipo** —su
productividad, su riesgo de siniestro, la calidad de lo que vende— antes de firmar. El
principal no. La asimetría existe ya al momento de contratar, y el principal no puede
más que ofrecer un **menú** y dejar que cada tipo se autoseleccione.

Diferencia clave con el riesgo moral: allá el problema era una acción futura; acá es
una característica preexistente. Y a diferencia de la Unidad IX, acá **mueve primero el
no informado**.

---

## 1. El mercado de limones (Akerlof, 1970)

El punto de entrada, por su potencia narrativa. Autos usados de calidad
$q \sim U[0,1]$ conocida por el vendedor. El comprador valora $\tfrac32 q$ pero solo
observa la calidad **media** de lo que se ofrece. A un precio $p$, solo se ofrecen los
autos con $q \le p$, de calidad media $p/2$; el comprador está dispuesto a pagar
$\tfrac32 \cdot \tfrac p2 = \tfrac34 p < p$.

**Ningún precio positivo sostiene el mercado: colapsa por completo.** Y hay ganancias
del comercio no realizadas para *todas* las calidades, porque el comprador valora más
que el vendedor en todo el rango. La ineficiencia no es una fricción de segundo orden:
es la desaparición del mercado.

> 💡 **Lección general.** La información asimétrica no distorsiona los precios: puede
> destruir el mercado. Y el mecanismo es una externalidad informacional —los malos
> tipos imponen un costo a los buenos, que terminan expulsados.

Aplicaciones inmediatas: seguros de salud (los sanos se van, sube la prima, se van más
sanos — *espiral de la muerte*), crédito (Stiglitz-Weiss: racionamiento en vez de suba
de tasa, porque subir la tasa empeora la cartera), mercado laboral.

## 2. El modelo con dos tipos

Tipos $\theta \in \{\theta_L, \theta_H\}$ con probabilidades $q$ y $1-q$. El principal
ofrece un menú $\{(x_L, t_L), (x_H, t_H)\}$ de cantidad y transferencia.

**Primer óptimo (tipos observables).** El principal extrae todo el excedente de cada
tipo por separado: eficiencia en cantidades y renta informacional nula.

**Segundo óptimo.** Restricciones:

- **RP** para cada tipo: $U_\theta \ge \bar U$;
- **RI** para cada tipo: $U_\theta(\text{contrato de }\theta) \ge U_\theta(\text{contrato del otro})$.

**Los dos resultados canónicos de la unidad:**

1. **«No distortion at the top»**: el tipo eficiente produce la cantidad de primer
   óptimo.
2. **Distorsión hacia abajo del tipo ineficiente**: su cantidad se reduce por debajo
   del primer óptimo, deliberadamente, para abaratar la renta informacional que hay
   que pagarle al eficiente.

**Renta informacional.** El tipo eficiente obtiene utilidad estrictamente por encima
de su reserva, no por generosidad sino porque podría hacerse pasar por el otro. El
principal *paga* por que no lo haga. Y el trade-off que resuelve es: **eficiencia
frente a extracción de renta**. Distorsionar al ineficiente cuesta excedente pero
ahorra renta; el óptimo iguala ambos márgenes.

**Cuáles restricciones son activas.** Un punto técnico que conviene explicitar: en el
óptimo son activas la RI del tipo eficiente y la RP del ineficiente; las otras dos son
redundantes. Reconocerlo simplifica enormemente la resolución y es lo que hace el
problema abordable a mano.

## 3. Análisis gráfico

En el plano (cantidad, transferencia), con curvas de indiferencia de cada tipo. La
**condición de cruce único** (*single crossing* / Spence-Mirrlees): las curvas de
indiferencia de los dos tipos se cruzan una sola vez, y el tipo eficiente tiene curvas
más planas. Es la condición que hace posible separar; sin ella, no hay menú que
autoseleccione.

## 4. Continuo de tipos

$\theta \sim F$ sobre $[\underline\theta, \overline\theta]$. Se resuelve por control
óptimo, con la fórmula del *virtual surplus*:

$$\theta - \frac{1-F(\theta)}{f(\theta)}$$

El segundo término es el **hazard rate inverso**: cuánto cuesta en renta informacional
atender a ese tipo. Bajo la condición de monotonía del hazard rate, la solución es
implementable. Es el mismo objeto que aparecerá en la Unidad X como *virtual valuation*
de Myerson en el diseño de subastas óptimas — vale la pena señalar la conexión.

## 5. Instituciones correctoras

- **Señalización** (Unidad IX): el informado actúa primero.
- **Screening**: menús de contratos, franquicias en seguros, planes tarifarios.
- **Garantías** y reputación.
- **Certificación** y auditoría por terceros.
- **Obligatoriedad**: el seguro de salud universal o el obligatorio de autos elimina la
  selección adversa por decreto, eliminando la opción de salir del pool. Buen cierre
  porque conecta la teoría con una discusión de política real.

---

## Qué debería hacer el notebook

### Contenido mínimo

1. **Simulación del mercado de limones**: iterar el proceso precio → calidad media
   ofrecida → disposición a pagar → nuevo precio, y graficar la convergencia al
   colapso. Ver el mercado apagarse en pantalla es más convincente que la demostración.
2. **Espiral de la muerte en seguros**: simular una población con riesgos heterogéneos
   y prima única; en cada ronda salen los de menor riesgo y la prima sube. Graficar
   prima y tamaño del pool contra la ronda.
3. **Resolver el menú óptimo con dos tipos** numéricamente y verificar los dos
   resultados canónicos: sin distorsión arriba, distorsión abajo.
4. **Gráfico de cruce único** con las curvas de indiferencia de ambos tipos y los dos
   contratos del menú marcados.
5. **Widget**: deslizador de la proporción de tipos eficientes $q$, mostrando cómo
   crece la distorsión del ineficiente a medida que hay más eficientes a quienes pagar
   renta.
6. **Continuo de tipos**: implementar el virtual surplus para $\theta$ uniforme y
   comparar la asignación de primer y segundo óptimo.

### Funciones nuevas para `eri_utils`

```python
mercado_limones(...)                 # itera hasta el equilibrio (o el colapso)
espiral_seleccion_adversa(...)       # simulacion del pool de seguros
menu_seleccion_adversa_2tipos(...)   # resuelve el segundo optimo
virtual_surplus(theta, F, f)         # theta - (1-F)/f
```
