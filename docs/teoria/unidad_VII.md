# Unidad VII — Riesgo Moral

**Clase 10 (30/09)** · Notebook `07_unidad_VII_riesgo_moral.ipynb`
**Bibliografía**: Macho-Stadler & Pérez Castrillo cap. 3; Holmström (1979)
**Estado**: ⚠️ **notas de clase pendientes** · notebook pendiente

> ⚠️ Alcance previsto, reconstruido del programa y la bibliografía. Cuando existan
> las notas en `latex/clase_10_unidad_VII.tex`, ellas mandan y este archivo se reescribe.

---

## De qué se trata

**Acción oculta.** El agente toma una decisión —esfuerzo, cuidado, diligencia— que el
principal no observa y que afecta la distribución del resultado. Como no se puede
contratar sobre el esfuerzo, hay que contratar sobre el resultado; pero el resultado
es ruidoso, de modo que pagar por resultado obliga al agente a soportar riesgo que,
por el Teorema de Borch, sería eficiente que soportara el principal.

**El conflicto central de la unidad, y de todo el bloque**: asegurar al agente destruye
sus incentivos; incentivarlo le impone riesgo. El contrato óptimo es la resolución de
ese trade-off, y **no** alcanza el primer óptimo.

---

## 1. Secuencia temporal

```
1. El principal ofrece el contrato w(·)
2. El agente acepta o rechaza          ← restricción de participación
3. El agente elige el esfuerzo e       ← no observable: restricción de incentivos
4. Se realiza el estado de la naturaleza
5. Se observa el resultado π y se paga w(π)
```

Lo decisivo es que el esfuerzo se elige **después** de firmar. Por eso la RI existe.

## 2. El modelo con dos esfuerzos

$e \in \{e_L, e_H\}$, con $c(e_H) > c(e_L)$. El esfuerzo alto desplaza la distribución
del resultado en el sentido de dominancia estocástica de primer orden:
$p_i^H$ vs. $p_i^L$ sobre los resultados $\pi_1 < \dots < \pi_n$.

**Primer óptimo (esfuerzo observable).** El principal elige el esfuerzo y solo reparte
riesgo: con principal neutral y agente averso, **salario fijo**. Es el *benchmark*.

**Segundo óptimo (esfuerzo no observable).** Para implementar $e_H$:

$$\min_{\{w_i\}} \sum_i p_i^H w_i \quad \text{s.a.}$$
$$\text{(RP)}\quad \sum_i p_i^H u(w_i) - c(e_H) \ge \bar U$$
$$\text{(RI)}\quad \sum_i p_i^H u(w_i) - c(e_H) \ \ge\ \sum_i p_i^L u(w_i) - c(e_L)$$

**El resultado de Holmström (1979).** Con multiplicadores $\lambda$ (RP) y $\mu$ (RI),
la CPO da la caracterización fundamental:

$$\frac{1}{u'(w_i)} = \lambda + \mu\left(1 - \frac{p_i^L}{p_i^H}\right)$$

**Cociente de verosimilitud y estructura salarial.** El término $p_i^L/p_i^H$ es el
cociente de verosimilitud: mide cuán *informativo* es el resultado $\pi_i$ sobre el
esfuerzo. El salario es alto donde el resultado es evidencia fuerte de esfuerzo alto
(cociente bajo) y bajo donde es evidencia de esfuerzo bajo.

> 💡 **El salario no premia el resultado; premia la evidencia.** Si el cociente de
> verosimilitud fuera constante —el resultado no dijera nada sobre el esfuerzo— el
> salario sería fijo y volveríamos al primer óptimo. La retribución variable existe
> solo en la medida en que el resultado informa.
>
> Corolario contraintuitivo: el salario **no tiene por qué ser monótono creciente en
> el resultado**. Lo es si el cociente de verosimilitud es monótono (condición MLRP),
> pero no en general. Es la mejor manera de mostrar que la lógica del contrato es
> informacional, no distributiva.

**Principio de informatividad (Holmström).** Cualquier señal adicional que aporte
información sobre el esfuerzo —aun ruidosa, aun no correlacionada con el resultado—
**debe** entrar en el contrato. Justifica evaluar por desempeño relativo (comparar con
otros agentes que enfrentan el mismo shock común, para filtrarlo) y es el argumento
teórico detrás de los *benchmarks* sectoriales en la retribución ejecutiva.

## 3. Enfoque de primer orden

Con esfuerzo continuo, se reemplaza la RI por su CPO:

$$\frac{\partial}{\partial e}\left[\int u(w(\pi))f(\pi|e)\,d\pi - c(e)\right] = 0$$

⚠️ Es **válido solo bajo condiciones** (MLRP más convexidad de la función de
distribución, CDFC): sin ellas, la CPO no caracteriza el máximo del agente y la
solución del programa relajado puede no ser implementable. Vale la pena mencionarlo:
es un caso donde el atajo matemático puede engañar.

## 4. Riesgo moral con información oculta

Variante: el agente observa un estado que el principal no ve y elige la acción
*después*. Se resuelve por el **principio de revelación**: sin pérdida de generalidad,
el principal puede restringirse a mecanismos directos en los que el agente reporta
verazmente lo que vio.

## 5. Valor de la información

Cuánto vale para el principal poder monitorear. Se mide como la diferencia entre el
beneficio del primer y del segundo óptimo, y crece con la aversión del agente y con el
ruido del resultado.

## 6. Aplicaciones

Seguros con franquicia y coseguro (el asegurado retiene parte del riesgo justamente
para preservar su incentivo al cuidado — **conecta directo con la Unidad III**), deuda
vs. capital, aparcería agrícola, retribución ejecutiva con opciones, crisis financiera
de 2008 como caso de originar-para-distribuir.

---

## Qué debería hacer el notebook

### Contenido mínimo

1. **Resolver el problema de dos esfuerzos y $n$ resultados numéricamente** con
   `scipy.optimize` y verificar la fórmula del cociente de verosimilitud punto por
   punto. Es el corazón computacional de la unidad.
2. **Gráfico del salario óptimo** $w_i$ contra el resultado $\pi_i$, superpuesto con
   el cociente de verosimilitud. Se debe ver que el salario sigue al cociente, no al
   resultado.
3. **Contraejemplo de no monotonía**: construir distribuciones que violen MLRP y
   mostrar un contrato óptimo con un tramo decreciente. Vale toda la clase.
4. **Comparación primer vs. segundo óptimo**: costo de la asimetría en función de la
   aversión del agente y de la varianza del resultado.
5. **Widget**: deslizador de la aversión del agente mostrando el contrato pasar de
   fuertemente incentivado (agente casi neutral) a casi fijo (agente muy averso).
6. Caso CARA-Normal con contrato lineal: $\beta^*=1/(1+a\sigma^2 c'')$ y su estática
   comparada, que conecta con la Unidad VI.

### Funciones nuevas para `eri_utils`

```python
riesgo_moral_discreto(p_alto, p_bajo, resultados, u, c_alto, c_bajo, U_reserva)
cociente_verosimilitud(p_alto, p_bajo)
primer_optimo(...)   # benchmark con esfuerzo observable
```
