# Datos

Datasets versionados que consumen los notebooks. **Ninguno se descarga en vivo**: la
reproducibilidad en clase manda sobre el realismo (ver `docs/ARQUITECTURA.md`, §3.3).

---

## `retornos_ejemplo.csv`

Rendimientos mensuales simulados de cinco carteras sectoriales más un índice de
mercado, 120 meses (enero 2016 a diciembre 2025). Se usa en el **notebook de la
Unidad IV** para el ejemplo empírico de frontera eficiente y estimación de betas.

| Columna | Contenido |
|---|---|
| `fecha` | Mes en formato `AAAA-MM` |
| `Mercado` | Rendimiento mensual del índice de mercado |
| `Energia`, `Banca`, `Consumo`, `Tecnologia`, `Utilities` | Rendimiento mensual de cada cartera sectorial |

Todos los valores son **rendimientos simples mensuales en tanto por uno** (0,0278 =
2,78 % en el mes), no porcentajes ni anualizados.

### Proceso generador

Modelo de un factor, exactamente el que el notebook estima después:

$$r_i = \alpha_i + \beta_i\,r_M + \varepsilon_i, \qquad \varepsilon_i \sim N(0,\sigma_{\varepsilon_i}^2)\ \text{independientes}$$

con $r_M \sim N(0{,}0080,\ 0{,}045^2)$ mensual y semilla `1410`.

| Activo | $\beta$ verdadero | $\alpha$ mensual | $\sigma_\varepsilon$ mensual |
|---|---|---|---|
| Energia | 1,35 | 0,0015 | 0,075 |
| Banca | 1,20 | 0,0000 | 0,065 |
| Consumo | 0,80 | 0,0020 | 0,050 |
| Tecnologia | 1,55 | 0,0010 | 0,095 |
| Utilities | 0,55 | 0,0025 | 0,040 |

### Por qué está simulado y no es real

Tres razones, en orden de importancia:

1. **Se conocen los parámetros verdaderos.** El notebook estima $\beta$ y lo compara
   con el valor que generó los datos. Con datos reales no hay contra qué comparar.
2. **Muestra el error de estimación.** Con 120 meses las betas estimadas se desvían
   visiblemente de las verdaderas (Energía: 1,06 estimada contra 1,35 verdadera). Eso
   **es** el punto pedagógico: el CAPM se estima con ruido, y una muestra de diez años
   no alcanza para pinnear una beta. Enseña más que un ajuste perfecto.
3. **No se rompe nunca.** Sin API, sin red, sin cambios de formato, sin resultados que
   cambien entre la preparación y la clase.

### Cómo regenerarlo

El script generador está documentado arriba y es determinístico: mismos parámetros,
misma semilla, mismo archivo. Si hiciera falta regenerarlo, reproducir el DGP con
`np.random.default_rng(1410)` en el orden indicado (primero `r_M`, después la matriz
de $\varepsilon$).

> ⚠️ **No regenerar sin necesidad.** Los `assert` del notebook de la Unidad IV que
> usan este archivo están calibrados contra estos valores exactos.
