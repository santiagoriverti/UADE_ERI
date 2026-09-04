# -*- coding: utf-8 -*-
"""
eri_utils - Utilidades compartidas
==================================

Economia del Riesgo y de la Informacion (1.4.010)
UADE - Facultad de Ciencias Economicas

Modulo de apoyo para los notebooks de la materia. Concentra en un solo lugar:

* la estetica institucional de los graficos (paleta navy/oro de las notas LaTeX);
* las funciones numericas que se usan en mas de una unidad (utilidades vNM,
  equivalente cierto, prima de riesgo, Arrow-Pratt, frontera de Markowitz,
  CAPM, modelo de Sandmo, criterios de decision bajo incertidumbre);
* helpers de presentacion de tablas.

Uso tipico dentro de un notebook de Colab (celda de setup)::

    !wget -q -O eri_utils.py https://raw.githubusercontent.com/santiagoriverti/UADE_ERI/main/src/eri_utils.py
    import eri_utils as eri
    eri.estilo_uade()

Convenciones de notacion (consistentes con las notas de clase)::

    y, w   riqueza / ingreso              u, v   utilidad vNM
    pi     probabilidad (Unidades I-V)    rho    prima de riesgo o aversion m-v
    CE     equivalente cierto             r_A    aversion absoluta (Arrow-Pratt)
    mu     media                          r_R    aversion relativa
    sigma  desvio                         beta   sensibilidad al mercado

Todas las funciones son puras y sin efectos colaterales, salvo las de graficos,
que dibujan sobre el Axes que reciban (o sobre uno nuevo si no reciben ninguno).
"""

from __future__ import annotations

__version__ = "0.1.0"
__all__ = [
    # estilo
    "NAVY", "ORO", "GRIS", "ROJO", "VERDE", "PALETA", "estilo_uade", "figura",
    # unidad I
    "maximin", "maximax", "hurwicz", "laplace", "minimax_arrepentimiento",
    "matriz_arrepentimiento", "tabla_criterios",
    # unidad II
    "u_log", "u_sqrt", "u_crra", "u_cara", "u_lineal",
    "utilidad_esperada", "equivalente_cierto", "prima_riesgo",
    "arrow_pratt_absoluta", "arrow_pratt_relativa", "prima_pratt",
    # unidad III
    "riquezas_contingentes", "cobertura_optima", "pooling_iid", "reparto_borch_cara",
    # unidad IV
    "momentos_cartera", "frontera_abcd", "frontera_sigma", "cartera_gmv",
    "cartera_tangente", "ratio_sharpe", "beta_capm", "capm",
    "descomposicion_riesgo", "hedge_ratio",
    # unidad V
    "sandmo_media_varianza", "producto_certeza",
    # helpers
    "tabla", "resaltar",
]

import numpy as np

try:  # pandas y matplotlib estan siempre en Colab; el modulo no debe romperse sin ellos
    import pandas as pd
except ImportError:  # pragma: no cover
    pd = None

try:
    import matplotlib.pyplot as plt
    from matplotlib import rcParams
except ImportError:  # pragma: no cover
    plt = None
    rcParams = {}


# ==========================================================================
#  0. Estetica institucional
# ==========================================================================

NAVY = "#004080"   # NavyBlue RGB(0,64,128) de las notas LaTeX
ORO = "#B0841C"    # Gold RGB(176,132,28)
GRIS = "#8A94A0"
ROJO = "#B3271E"
VERDE = "#1E7A4B"

#: Paleta categorica por defecto (pensada para series de 2 a 5 elementos).
PALETA = [NAVY, ORO, GRIS, ROJO, VERDE]


def estilo_uade(escala: float = 1.0) -> None:
    """Aplica la estetica de las notas de clase a los graficos posteriores.

    Parametros
    ----------
    escala : float
        Multiplicador del tamano de fuente. Usar ~1.3 al compartir pantalla en
        el aula para que se lea desde el fondo.
    """
    if plt is None:  # pragma: no cover
        return
    rcParams.update({
        "figure.figsize": (8.0, 5.0),
        "figure.dpi": 110,
        "savefig.dpi": 160,
        "font.size": 11 * escala,
        "axes.titlesize": 13 * escala,
        "axes.labelsize": 11.5 * escala,
        "axes.titleweight": "bold",
        "axes.titlecolor": NAVY,
        "axes.labelcolor": "#1a1a1a",
        "axes.edgecolor": "#4a4a4a",
        "axes.linewidth": 0.9,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "axes.prop_cycle": plt.cycler(color=PALETA),
        "grid.color": "#D8DEE6",
        "grid.linewidth": 0.7,
        "legend.frameon": False,
        "legend.fontsize": 10 * escala,
        "lines.linewidth": 2.1,
        "xtick.labelsize": 10 * escala,
        "ytick.labelsize": 10 * escala,
        "xtick.color": "#4a4a4a",
        "ytick.color": "#4a4a4a",
        "mathtext.fontset": "cm",
    })


def figura(titulo: str = "", xlabel: str = "", ylabel: str = "", figsize=None):
    """Devuelve (fig, ax) con titulo y ejes ya rotulados. Azucar sintactica."""
    fig, ax = plt.subplots(figsize=figsize)
    if titulo:
        ax.set_title(titulo)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    return fig, ax


# ==========================================================================
#  1. Unidad I - Criterios de decision bajo incertidumbre (sin probabilidades)
# ==========================================================================
#
#  Entrada comun: matriz de pagos X de forma (n_acciones, n_estados).
#  Cada criterio devuelve (indice_accion_elegida, vector_de_indices).

def _X(pagos) -> np.ndarray:
    X = np.asarray(pagos, dtype=float)
    if X.ndim != 2:
        raise ValueError("La matriz de pagos debe ser bidimensional (acciones x estados).")
    return X


def maximin(pagos):
    """Criterio de Wald (pesimismo puro): maximiza el peor resultado de cada accion."""
    X = _X(pagos)
    v = X.min(axis=1)
    return int(np.argmax(v)), v


def maximax(pagos):
    """Optimismo puro: maximiza el mejor resultado de cada accion."""
    X = _X(pagos)
    v = X.max(axis=1)
    return int(np.argmax(v)), v


def hurwicz(pagos, alpha: float = 0.5):
    """Criterio de Hurwicz: H_i = alpha*max_j x_ij + (1-alpha)*min_j x_ij.

    alpha es el coeficiente de optimismo: alpha=1 reproduce maximax y alpha=0
    reproduce maximin.
    """
    if not 0.0 <= alpha <= 1.0:
        raise ValueError("alpha debe estar en [0, 1].")
    X = _X(pagos)
    v = alpha * X.max(axis=1) + (1.0 - alpha) * X.min(axis=1)
    return int(np.argmax(v)), v


def laplace(pagos, probs=None):
    """Criterio de Laplace (razon insuficiente): promedio simple de los pagos.

    Si se pasa probs, calcula el valor esperado con esas probabilidades, lo que
    permite contrastar el criterio con el caso de riesgo.
    """
    X = _X(pagos)
    if probs is None:
        v = X.mean(axis=1)
    else:
        p = np.asarray(probs, dtype=float)
        if not np.isclose(p.sum(), 1.0):
            raise ValueError("Las probabilidades deben sumar 1.")
        v = X @ p
    return int(np.argmax(v)), v


def matriz_arrepentimiento(pagos) -> np.ndarray:
    """Matriz de regret r_ij = max_k x_kj - x_ij."""
    X = _X(pagos)
    return X.max(axis=0) - X


def minimax_arrepentimiento(pagos):
    """Criterio de Savage: minimiza el maximo arrepentimiento."""
    R = matriz_arrepentimiento(pagos)
    v = R.max(axis=1)
    return int(np.argmin(v)), v


def tabla_criterios(pagos, alpha: float = 0.5, acciones=None, probs=None):
    """Tabla comparativa con los cinco criterios de la Unidad I.

    Devuelve un DataFrame con una fila por accion y una columna por criterio,
    mas una fila final que indica la accion elegida por cada uno.
    """
    X = _X(pagos)
    if acciones is None:
        acciones = ["a%d" % (i + 1) for i in range(X.shape[0])]
    i_mn, v_mn = maximin(X)
    i_mx, v_mx = maximax(X)
    i_hz, v_hz = hurwicz(X, alpha)
    i_lp, v_lp = laplace(X, probs)
    i_mr, v_mr = minimax_arrepentimiento(X)
    cols = {
        "Maximin": v_mn,
        "Maximax": v_mx,
        "Hurwicz (a=%.2f)" % alpha: v_hz,
        "Laplace": v_lp,
        "Max. arrepentimiento": v_mr,
    }
    elegidas = [acciones[i] for i in (i_mn, i_mx, i_hz, i_lp, i_mr)]
    if pd is None:  # pragma: no cover
        return cols, elegidas
    df = pd.DataFrame(cols, index=acciones)
    df.loc["--> elige"] = elegidas
    df.index.name = "Accion"
    return df


# ==========================================================================
#  2. Unidad II - Utilidad esperada, equivalente cierto y Arrow-Pratt
# ==========================================================================

def u_log(y):
    """u(y) = ln(y). CRRA con R = 1."""
    return np.log(y)


def u_sqrt(y):
    """u(y) = sqrt(y). CRRA con R = 1/2 salvo escala."""
    return np.sqrt(y)


def u_crra(y, R: float):
    """Utilidad CRRA: u(y) = y^(1-R)/(1-R), con el caso limite ln(y) en R = 1."""
    y = np.asarray(y, dtype=float)
    if np.isclose(R, 1.0):
        return np.log(y)
    return y ** (1.0 - R) / (1.0 - R)


def u_cara(y, a: float):
    """Utilidad CARA (exponencial negativa): u(y) = -exp(-a*y), con a > 0."""
    if a <= 0:
        raise ValueError("El coeficiente a de la CARA debe ser positivo.")
    return -np.exp(-a * np.asarray(y, dtype=float))


def u_lineal(y, alpha: float = 0.0, beta: float = 1.0):
    """Utilidad lineal (neutralidad al riesgo): u(y) = alpha + beta*y."""
    return alpha + beta * np.asarray(y, dtype=float)


def utilidad_esperada(u, resultados, probs):
    """E[u(Y)] para una loteria discreta.

    Parametros
    ----------
    u : callable
        Funcion de utilidad vNM.
    resultados, probs : array_like
        Premios y probabilidades (deben sumar 1).
    """
    y = np.asarray(resultados, dtype=float)
    p = np.asarray(probs, dtype=float)
    if y.shape != p.shape:
        raise ValueError("resultados y probs deben tener la misma forma.")
    if not np.isclose(p.sum(), 1.0):
        raise ValueError("Las probabilidades deben sumar 1.")
    return float(np.dot(p, u(y)))


def equivalente_cierto(u, resultados, probs, rango=None, tol: float = 1e-10):
    """Equivalente cierto CE tal que u(CE) = E[u(Y)], por biseccion.

    Se supone u estrictamente creciente en el rango. Si no se especifica, se
    toma [min(resultados), max(resultados)], que contiene al CE por monotonia.
    """
    EU = utilidad_esperada(u, resultados, probs)
    y = np.asarray(resultados, dtype=float)
    lo, hi = (float(y.min()), float(y.max())) if rango is None else rango
    if hi - lo < tol:
        return lo
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if u(mid) < EU:
            lo = mid
        else:
            hi = mid
        if hi - lo < tol:
            break
    return 0.5 * (lo + hi)


def prima_riesgo(u, resultados, probs, rango=None):
    """Prima de riesgo rho = E[Y] - CE. Positiva si el agente es averso."""
    y = np.asarray(resultados, dtype=float)
    p = np.asarray(probs, dtype=float)
    return float(np.dot(p, y)) - equivalente_cierto(u, resultados, probs, rango)


def arrow_pratt_absoluta(u, y, h: float = 1e-4):
    """r_A(y) = -u''(y)/u'(y), por diferencias finitas centradas.

    `h` es un paso **relativo**: el paso efectivo es h*max(|y|, 1). La derivada
    segunda es muy sensible al tamano del paso —con un h absoluto chico el
    numerador cae por debajo de la resolucion del punto flotante y el resultado
    se degrada—, de modo que escalarlo con el punto de evaluacion es lo que
    mantiene el error por debajo de 1e-7 en el rango habitual de riquezas.
    """
    y = np.asarray(y, dtype=float)
    paso = h * np.maximum(np.abs(y), 1.0)
    d1 = (u(y + paso) - u(y - paso)) / (2 * paso)
    d2 = (u(y + paso) - 2 * u(y) + u(y - paso)) / (paso ** 2)
    return -d2 / d1


def arrow_pratt_relativa(u, y, h: float = 1e-4):
    """r_R(y) = y * r_A(y)."""
    return np.asarray(y, dtype=float) * arrow_pratt_absoluta(u, y, h)


def prima_pratt(u, y, varianza: float, h: float = 1e-4):
    """Aproximacion local de Pratt: rho ~= (1/2) * r_A(y) * sigma^2."""
    return 0.5 * arrow_pratt_absoluta(u, y, h) * varianza


# ==========================================================================
#  3. Unidad III - Seguro, fondo comun y reparto de Borch
# ==========================================================================

def riquezas_contingentes(W: float, L: float, p: float, q):
    """Riquezas contingentes de un contrato de seguro.

    Con riqueza inicial W, perdida L, tasa de prima p y cobertura q::

        w1 = W - p*q                   (estado sin siniestro)
        w2 = W - L + (1 - p)*q         (estado con siniestro)
    """
    return W - p * q, W - L + (1.0 - p) * q


def cobertura_optima(u, W: float, L: float, pi: float, p: float, n: int = 200001):
    """Cobertura q* que maximiza (1-pi)*u(w1) + pi*u(w2), por busqueda en grilla.

    pi es la probabilidad de siniestro y p la tasa de prima. Con p = pi (prima
    actuarialmente justa) el optimo es cobertura total, q* = L.
    Devuelve (q_opt, w1, w2, EU).
    """
    q = np.linspace(0.0, L, n)
    w1, w2 = riquezas_contingentes(W, L, p, q)
    valido = (w1 > 0) & (w2 > 0)
    EU = np.full_like(q, -np.inf)
    EU[valido] = (1.0 - pi) * u(w1[valido]) + pi * u(w2[valido])
    k = int(np.argmax(EU))
    return float(q[k]), float(w1[k]), float(w2[k]), float(EU[k])


def pooling_iid(u, resultados, probs, n: int):
    """Utilidad esperada de un miembro de un fondo comun de n agentes iid.

    Cada agente aporta una realizacion de la loteria y se reparte el total en
    partes iguales. Devuelve (EU, distribucion), donde distribucion es la lista
    ordenada de pares (ingreso_por_persona, probabilidad).
    """
    from itertools import product
    y = np.asarray(resultados, dtype=float)
    p = np.asarray(probs, dtype=float)
    acum = {}
    for idx in product(range(len(y)), repeat=n):
        prob = float(np.prod(p[list(idx)]))
        ing = float(np.mean(y[list(idx)]))
        acum[ing] = acum.get(ing, 0.0) + prob
    dist = sorted(acum.items())
    EU = sum(pr * float(u(ing)) for ing, pr in dist)
    return EU, dist


def reparto_borch_cara(a, W, lambdas=None):
    """Reparto Pareto-optimo con utilidades CARA: c_i(W) = alpha_i*W + beta_i.

    Bajo CARA la tolerancia al riesgo T_i = 1/a_i es constante, de modo que la
    cuota de riesgo agregado de cada agente es su tolerancia relativa.

    Parametros
    ----------
    a : array_like
        Coeficientes de aversion absoluta a_i de cada agente.
    W : float o array_like
        Riqueza agregada (puede ser un vector de estados).
    lambdas : array_like, opcional
        Pesos de bienestar. Por defecto todos iguales.

    Devuelve (alpha, beta, C) con C de forma (n_agentes, n_estados).
    """
    a = np.asarray(a, dtype=float)
    T = 1.0 / a
    alpha = T / T.sum()
    if lambdas is None:
        lambdas = np.ones_like(a)
    lambdas = np.asarray(lambdas, dtype=float)
    # De lambda_i * u_i'(c_i) = mu con sum(c_i) = W se despeja el termino
    # constante; se centra para que sum(beta_i) = 0 (factibilidad).
    k = np.log(lambdas * a) / a
    beta = k - alpha * k.sum()
    W = np.atleast_1d(np.asarray(W, dtype=float))
    C = np.outer(alpha, W) + beta[:, None]
    return alpha, beta, C


# ==========================================================================
#  4. Unidad IV - Markowitz, CAPM y futuros
# ==========================================================================

def momentos_cartera(w, mu, Sigma):
    """Media y desvio de una cartera: (w'mu, sqrt(w' Sigma w))."""
    w = np.asarray(w, dtype=float)
    mu = np.asarray(mu, dtype=float)
    Sigma = np.asarray(Sigma, dtype=float)
    m = float(w @ mu)
    v = float(w @ Sigma @ w)
    return m, float(np.sqrt(max(v, 0.0)))


def frontera_abcd(mu, Sigma):
    """Escalares A, B, C, D de la frontera de minima varianza.

        A = 1' S^-1 mu,   B = mu' S^-1 mu,   C = 1' S^-1 1,   D = B*C - A^2
    """
    mu = np.asarray(mu, dtype=float)
    Sigma = np.asarray(Sigma, dtype=float)
    Si = np.linalg.inv(Sigma)
    uno = np.ones_like(mu)
    A = float(uno @ Si @ mu)
    B = float(mu @ Si @ mu)
    C = float(uno @ Si @ uno)
    D = B * C - A ** 2
    return A, B, C, D


def frontera_sigma(mu_objetivo, mu, Sigma):
    """Desvio de la cartera de minima varianza para cada rendimiento objetivo.

    Implementa sigma^2 = (C*mu_p^2 - 2*A*mu_p + B)/D, la hiperbola de Markowitz.
    """
    A, B, C, D = frontera_abcd(mu, Sigma)
    m = np.asarray(mu_objetivo, dtype=float)
    var = (C * m ** 2 - 2 * A * m + B) / D
    return np.sqrt(np.maximum(var, 0.0))


def cartera_gmv(mu, Sigma):
    """Cartera de minima varianza global: w = S^-1 1 / C. Devuelve (w, mu_p, sigma_p)."""
    mu = np.asarray(mu, dtype=float)
    Sigma = np.asarray(Sigma, dtype=float)
    Si = np.linalg.inv(Sigma)
    uno = np.ones_like(mu)
    C = float(uno @ Si @ uno)
    w = (Si @ uno) / C
    m, s = momentos_cartera(w, mu, Sigma)
    return w, m, s


def cartera_tangente(mu, Sigma, rf: float):
    """Portafolio tangente: w proporcional a S^-1 (mu - rf*1), normalizado a sumar 1."""
    mu = np.asarray(mu, dtype=float)
    Sigma = np.asarray(Sigma, dtype=float)
    Si = np.linalg.inv(Sigma)
    z = Si @ (mu - rf * np.ones_like(mu))
    w = z / z.sum()
    m, s = momentos_cartera(w, mu, Sigma)
    return w, m, s


def ratio_sharpe(mu_p: float, sigma_p: float, rf: float) -> float:
    """(mu_p - rf) / sigma_p. Pendiente de la Linea del Mercado de Capitales."""
    return (mu_p - rf) / sigma_p


def beta_capm(cov_iM: float, var_M: float) -> float:
    """beta_i = Cov(r_i, r_M) / Var(r_M)."""
    return cov_iM / var_M


def capm(beta: float, rf: float, mu_M: float) -> float:
    """Rendimiento de equilibrio segun la SML: mu_i = rf + beta*(mu_M - rf)."""
    return rf + beta * (mu_M - rf)


def descomposicion_riesgo(sigma_i: float, beta: float, sigma_M: float):
    """Descompone la varianza total en sistematica y no sistematica.

    Devuelve (var_total, var_sistematica, var_idiosincratica, R2).
    """
    var_t = sigma_i ** 2
    var_s = (beta ** 2) * (sigma_M ** 2)
    var_e = var_t - var_s
    return var_t, var_s, var_e, var_s / var_t


def hedge_ratio(rho_SF: float, sigma_S: float, sigma_F: float) -> float:
    """Ratio de cobertura de varianza minima: h* = rho * sigma_S / sigma_F."""
    return rho_SF * sigma_S / sigma_F


# ==========================================================================
#  5. Unidad V - Firma competitiva bajo incertidumbre (Sandmo)
# ==========================================================================

def producto_certeza(mu: float, c: float) -> float:
    """Producto de certeza con costo cuadratico C(x) = (c/2)x^2: x_c = mu/c."""
    return mu / c


def sandmo_media_varianza(mu: float, c: float, rho: float, sigma2: float):
    """Optimo de la firma con preferencias media-varianza y costo cuadratico.

        x* = mu / (c + rho*sigma^2)

    Devuelve un diccionario con el producto optimo, el producto de certeza, la
    prima marginal de riesgo, el beneficio esperado (sin costo fijo), el
    descuento por riesgo y el equivalente cierto.
    """
    x = mu / (c + rho * sigma2)
    xc = producto_certeza(mu, c)
    E_pi = mu * x - 0.5 * c * x ** 2
    descuento = 0.5 * rho * (x ** 2) * sigma2
    return {
        "x": x,
        "x_certeza": xc,
        "costo_marginal": c * x,
        "prima_marginal": mu - c * x,
        "beneficio_esperado": E_pi,
        "descuento_riesgo": descuento,
        "equivalente_cierto": E_pi - descuento,
    }


# ==========================================================================
#  6. Helpers de presentacion
# ==========================================================================

def tabla(datos, columnas=None, indice=None, decimales: int = 4):
    """Envuelve datos en un DataFrame redondeado, listo para mostrar en Colab."""
    if pd is None:  # pragma: no cover
        return datos
    df = pd.DataFrame(datos, columns=columnas, index=indice)
    num = df.select_dtypes(include=[np.number]).columns
    df[num] = df[num].round(decimales)
    return df


def resaltar(texto: str, valor=None, decimales: int = 4) -> None:
    """Imprime un resultado destacado con formato uniforme en todos los notebooks."""
    if valor is None:
        print("  >> %s" % texto)
    elif isinstance(valor, (bool, np.bool_)):
        print("  >> %-46s %s" % (texto, valor))
    elif isinstance(valor, (int, np.integer)):
        print("  >> %-46s %d" % (texto, valor))
    elif isinstance(valor, (float, np.floating)):
        print("  >> %-46s %.*f" % (texto, decimales, valor))
    else:
        print("  >> %-46s %s" % (texto, valor))
