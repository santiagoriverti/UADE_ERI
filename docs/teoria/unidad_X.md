# Unidad X — Teoría de Juegos, Subastas y Diseño de Mercados

**Clases 13 y 14 (21/10 y 28/10)** · Notebook `10_unidad_X_subastas.ipynb`
**Bibliografía**: Vickrey (1961); Wilson (1969); Milgrom & Weber (1982)
**Estado**: ⚠️ **notas de clase pendientes** · notebook pendiente

> ⚠️ Alcance previsto, reconstruido del programa y la bibliografía. Cuando existan
> las notas en `latex/clase_13_unidad_X.tex`, ellas mandan y este archivo se reescribe.
>
> **Esta unidad abarca dos clases del cronograma.** Se resuelve con dos partes dentro
> del mismo notebook, no con dos archivos: Parte A (clase 13) subastas clásicas y
> equivalencia de recaudación; Parte B (clase 14) maldición del ganador y *market design*.

---

## De qué se trata

Cierre del curso. Las subastas son el laboratorio donde todo lo anterior se junta:
información privada (Unidad VIII), competencia estratégica, y diseño de reglas que
inducen revelación. Y son, además, el caso de éxito más visible de la teoría económica
aplicada: del espectro radioeléctrico a la publicidad online.

---

## Parte A — Clase 13

### 1. Elementos de teoría de juegos

Lo mínimo necesario, no un curso completo: forma normal y extensiva, estrategias
dominantes, **equilibrio de Nash**, información incompleta, tipos y **equilibrio
bayesiano de Nash** (Harsanyi). Si ya se vio en la Unidad IX el equilibrio bayesiano
perfecto, acá se retoma con lo puesto.

### 2. Los cuatro formatos clásicos

| Formato | Regla | Estrategia de equilibrio (valores privados) |
|---|---|---|
| **Inglesa** (ascendente) | Precio sube hasta que queda uno | Permanecer hasta el propio valor. **Dominante** |
| **Holandesa** (descendente) | Precio baja hasta que alguien acepta | Estratégicamente **equivalente** a primer precio |
| **Primer precio**, sobre cerrado | Gana el mayor, paga su oferta | Ofertar **menos** que el valor: *bid shading* |
| **Segundo precio** (Vickrey) | Gana el mayor, paga la **segunda** oferta | Ofertar el valor propio. **Dominante** |

### 3. Vickrey (1961): veracidad en estrategia dominante

**El resultado más elegante de la unidad.** En la subasta de segundo precio, ofertar el
valor verdadero es dominante, y la demostración es de dos casos y cabe en una
transparencia: si uno sube su oferta por encima del valor, solo cambia algo cuando gana
pagando más que su valor (mala noticia); si la baja, solo cambia algo cuando pierde una
subasta que le convenía ganar. En ningún caso mejora.

**Por qué importa:** hace que el resultado no dependa de creencias sobre los rivales.
El agente no necesita saber nada de los demás, ni siquiera ser sofisticado. Es el
antecedente del mecanismo VCG y de todo el diseño de mecanismos.

### 4. Primer precio y equilibrio bayesiano

Con $n$ postores y valores iid $\sim U[0,1]$, el equilibrio simétrico es

$$b(v) = \frac{n-1}{n}\,v$$

El *shading* se reduce a medida que crece la competencia. La derivación (CPO de la
maximización del pago esperado) debe hacerse en clase: es el ejercicio estándar.

### 5. Teorema de equivalencia de recaudación

**Enunciado.** Bajo valores privados independientes, postores neutrales al riesgo y
simétricos, cualquier mecanismo que (i) asigne el objeto al de mayor valor y (ii) dé
utilidad nula al tipo más bajo, genera **la misma recaudación esperada** para el
vendedor.

**Consecuencia sorprendente**: los cuatro formatos recaudan lo mismo en promedio, pese
a verse tan distintos. Con $U[0,1]$ y $n$ postores, la recaudación esperada es
$\frac{n-1}{n+1}$ en todos.

**Cuándo se rompe** —y esto es lo interesante, porque explica por qué el diseño importa
en la práctica—: aversión al riesgo de los postores (favorece el primer precio),
asimetría entre postores, valores interdependientes, colusión, entrada endógena,
restricciones presupuestarias.

## Parte B — Clase 14

### 6. Valores comunes y maldición del ganador

**Valores comunes**: el objeto vale lo mismo para todos (una concesión petrolera), pero
cada uno tiene una **estimación** ruidosa. Wilson (1969) es la referencia.

**La maldición del ganador.** Ganar es mala noticia: significa que uno tuvo la
estimación **más optimista** de todas, y por lo tanto probablemente sobreestimó. El
postor ingenuo que ofrece su estimación insesgada pierde plata sistemáticamente.

$$E[V \mid x_i,\ \text{ganar}] \ <\ E[V \mid x_i]$$

**Corrección**: hay que condicionar a ganar, no solo a la propia señal, y el *shading*
necesario **crece con $n$** —al revés que en valores privados, donde más competencia
lleva a ofertar más agresivamente. Contraste que vale la pena subrayar: es la
intuición que más falla.

Evidencia experimental (Bazerman-Samuelson, el frasco de monedas) y de campo
(licitaciones petroleras del Golfo de México en los años 70).

### 7. Milgrom & Weber (1982): afiliación

Marco general con valores **afiliados** (señales positivamente dependientes). Dos
resultados centrales:

- **Ranking de recaudación**: inglesa $\ge$ segundo precio $\ge$ primer precio
  $=$ holandesa. La equivalencia de recaudación se rompe, y el orden no es arbitrario.
- **Principio de vinculación (*linkage principle*)**: al vendedor le conviene
  **comprometerse a revelar** públicamente toda la información que tenga. Revelar reduce
  la incertidumbre de los postores, mitiga la maldición del ganador y les permite
  ofertar más agresivamente. Explica por qué la subasta inglesa recauda más: al ver
  retirarse a los demás, cada postor va incorporando su información.

### 8. Diseño de mercados

- **Subastas de espectro**: la *Simultaneous Multiple Round Auction* diseñada por
  Milgrom, Wilson y McAfee para la FCC (1994) y el problema de la **exposición** con
  bienes complementarios; subastas combinatorias como respuesta. Premio Nobel 2020 a
  Milgrom y Wilson.
- **Publicidad online**: *Generalized Second Price* de Google frente a VCG. Caso
  perfecto para mostrar que el mecanismo teóricamente superior no siempre es el que se
  adopta, y por qué.
- **Mecanismos de reputación online**: eBay, Airbnb, Mercado Libre. La reputación como
  solución descentralizada a la selección adversa de la Unidad VIII —cierra el círculo
  del bloque de información.
- Mención breve a *matching* (Gale-Shapley, asignación de residencias médicas y
  escuelas) como la otra rama del *market design*.

---

## Qué debería hacer el notebook

**Es el notebook con más potencial computacional de la materia.** La simulación acá no
ilustra la teoría: la descubre.

### Contenido mínimo

1. **Simulación Monte Carlo de los cuatro formatos** con $n$ postores y valores
   $U[0,1]$: verificar numéricamente la **equivalencia de recaudación** promediando
   $10^5$ subastas. Que salgan los cuatro números iguales es el mejor argumento posible
   a favor del teorema.
2. **Verificar $b(v)=\frac{n-1}{n} v$** por *best response*: fijar la estrategia de los
   rivales y buscar numéricamente la mejor respuesta; debe coincidir con la fórmula.
3. **Ruptura de la equivalencia**: repetir la simulación con postores aversos al riesgo
   y mostrar que el primer precio pasa a recaudar más. Y con postores asimétricos.
4. **Maldición del ganador**: simular valores comunes con señales ruidosas y comparar
   el beneficio del postor ingenuo (oferta su señal) contra el sofisticado (condiciona a
   ganar). Graficar el beneficio del ingenuo contra $n$: se hace **más negativo**.
   Es la simulación más didáctica de toda la materia.
5. **Widget**: deslizadores de $n$ y del ruido de la señal, mostrando la corrección
   necesaria.
6. **Experimento en vivo con la clase**: dejar preparada una celda donde el docente
   cargue las ofertas reales de los alumnos por un frasco de monedas (o similar) y el
   notebook calcule ganador, pago y pérdida. Con el aula haciendo de laboratorio, la
   maldición del ganador se demuestra sola.
7. **Ranking de Milgrom-Weber** con señales afiliadas: simular con correlación positiva
   y verificar el orden inglesa ≥ segundo precio ≥ primer precio.

### Funciones nuevas para `eri_utils`

```python
subasta_primer_precio(valores, n)
subasta_segundo_precio(valores)
simular_subastas(formato, n, n_sim, distribucion, aversion=0)
maldicion_ganador(valor_comun, ruido, n, ingenuo=True)
recaudacion_esperada_teorica(n)     # (n-1)/(n+1) para U[0,1]
```

### Cierre del curso

El notebook debería terminar señalando el arco completo: de Knight y la
imposibilidad de asignar probabilidades (Unidad I) al diseño de instituciones que
extraen información privada y la convierten en asignaciones eficientes (Unidad X). La
materia empieza mostrando que no sabemos, y termina mostrando cómo diseñar reglas para
que la información que está dispersa aflore.
