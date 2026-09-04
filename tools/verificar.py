# -*- coding: utf-8 -*-
"""
Verificacion de `src/eri_utils.py` contra la guia de ejercicios resueltos.

Cada assert corresponde a un resultado publicado en `latex/guia_ejercicios_soluciones.tex`.
Si alguno falla, el modulo compartido dejo de reproducir la guia y hay que arreglarlo
antes de commitear: los notebooks dependen de estos valores.

Uso:
    python tools/verificar.py
"""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))
import eri_utils as eri  # noqa: E402

TOL = 1e-6
_ok = 0


def check(descripcion, obtenido, esperado, tol=TOL):
    global _ok
    obtenido = float(obtenido)
    if abs(obtenido - esperado) > tol:
        print("  FALLA  %-52s obtenido %.8f  esperado %.8f" % (descripcion, obtenido, esperado))
        raise SystemExit(1)
    print("  ok     %-52s %.6f" % (descripcion, obtenido))
    _ok += 1


def check_igual(descripcion, obtenido, esperado):
    global _ok
    if obtenido != esperado:
        print("  FALLA  %-52s obtenido %s  esperado %s" % (descripcion, obtenido, esperado))
        raise SystemExit(1)
    print("  ok     %-52s %s" % (descripcion, obtenido))
    _ok += 1


print("\nClase 1 - Unidad I")
pagos = [[10, 40, 70], [30, 30, 30], [60, 20, 5]]
check_igual("Ej 1 maximin elige a2", eri.maximin(pagos)[0], 1)
check_igual("Ej 1 maximax elige a1", eri.maximax(pagos)[0], 0)
check_igual("Ej 1 Hurwicz(0.6) elige a1", eri.hurwicz(pagos, 0.6)[0], 0)
check_igual("Ej 1 Laplace elige a1", eri.laplace(pagos)[0], 0)
check_igual("Ej 1 minimax-arrepentimiento elige a2", eri.minimax_arrepentimiento(pagos)[0], 1)
check("Ej 1 max arrepentimiento de a2", eri.minimax_arrepentimiento(pagos)[1][1], 40.0)
check("Ej 2 equivalente cierto log(100,400)", eri.equivalente_cierto(eri.u_log, [100, 400], [0.5, 0.5]), 200.0)
check("Ej 2 prima de riesgo", eri.prima_riesgo(eri.u_log, [100, 400], [0.5, 0.5]), 50.0)
check("Ej 3 CARA a=2 tiene r_A constante", eri.arrow_pratt_absoluta(lambda y: eri.u_cara(y, 2.0), 3.0), 2.0, 1e-4)
check("Ej 3 CRRA R=3 tiene r_R constante", eri.arrow_pratt_relativa(lambda y: eri.u_crra(y, 3.0), 5.0), 3.0, 1e-4)

print("\nClase 2 - Unidad II")
check("Ej 1b San Petersburgo E[ln X] = ln 4",
      sum((0.5 ** n) * np.log(2.0 ** n) for n in range(1, 400)), np.log(4.0))
check("Ej 4a E[u(X)] con sqrt(36,100)", eri.utilidad_esperada(eri.u_sqrt, [36, 100], [0.5, 0.5]), 8.0)
check("Ej 4a equivalente cierto", eri.equivalente_cierto(eri.u_sqrt, [36, 100], [0.5, 0.5]), 64.0)
check("Ej 4a prima de riesgo exacta", eri.prima_riesgo(eri.u_sqrt, [36, 100], [0.5, 0.5]), 4.0)
check("Ej 4b aproximacion de Pratt", eri.prima_pratt(eri.u_sqrt, 68.0, 1024.0), 512.0 / 136.0, 1e-4)
check("Ej 6a r_A de A(w)=-exp(-2w)", eri.arrow_pratt_absoluta(lambda w: -np.exp(-2 * w), 1.0), 2.0, 1e-4)
_q, _w1, _w2, _ = eri.cobertura_optima(eri.u_log, 100.0, 51.0, 1 / 3, 1 / 3)
check("Ej 8a seguro a prima justa: q* = L", _q, 51.0, 1e-3)
check("Ej 8a riqueza final cierta", _w1, 83.0, 1e-3)
_q, _, _, _ = eri.cobertura_optima(eri.u_log, 100.0, 51.0, 1 / 3, 0.4)
check("Ej 8b seguro con recargo: q* = 260/9", _q, 260.0 / 9.0, 1e-3)

print("\nClase 3 - Unidad III")
_q, _w1, _w2, _ = eri.cobertura_optima(eri.u_sqrt, 100.0, 64.0, 0.25, 0.25)
check("Ej 1 cobertura total q* = 64", _q, 64.0, 1e-3)
check("Ej 1 ingreso cierto = 84", _w1, 84.0, 1e-3)
check("Ej 1 CE sin seguro = 81", eri.equivalente_cierto(eri.u_sqrt, [100, 36], [0.75, 0.25]), 81.0)
_q, _w1, _w2, _ = eri.cobertura_optima(eri.u_log, 100.0, 64.0, 0.25, 0.40)
check("Ej 2 cobertura parcial q* = 17.5", _q, 17.5, 1e-3)
_eu1, _ = eri.pooling_iid(eri.u_sqrt, [100, 0], [0.5, 0.5], 1)
_eu2, _ = eri.pooling_iid(eri.u_sqrt, [100, 0], [0.5, 0.5], 2)
check("Ej 6 pooling n=1: CE = 25", _eu1 ** 2, 25.0)
check("Ej 6 pooling n=2: CE ~ 36.4", _eu2 ** 2, 36.4276, 1e-3)
_alpha, _beta, _C = eri.reparto_borch_cara([0.01, 0.02], [100.0, 200.0])
check("Ej 8 cuota de riesgo del agente 1 = 2/3", _alpha[0], 2.0 / 3.0)
check("Ej 8 cuota de riesgo del agente 2 = 1/3", _alpha[1], 1.0 / 3.0)
check("Ej 8 transferencia beta_1 ~ -23.1", _beta[0], -np.log(2.0) / 0.03, 1e-3)
check("Ej 8 factibilidad: las transferencias suman 0", _beta.sum(), 0.0, 1e-9)
check("Ej 8 factibilidad estado 1", _C[:, 0].sum(), 100.0, 1e-9)

print("\nClase 4 - Unidad IV")
_mu2 = np.array([0.10, 0.18])
_S2 = np.array([[0.0225, 0.009], [0.009, 0.09]])
_m, _s = eri.momentos_cartera([0.6, 0.4], _mu2, _S2)
check("Ej 1 rendimiento de la cartera", _m, 0.132)
check("Ej 1 desvio de la cartera", _s, 0.163768, 1e-5)
_w, _m, _s = eri.cartera_gmv(_mu2, _S2)
check("Ej 2 GMV: ponderacion del activo A", _w[0], 0.857143, 1e-5)
check("Ej 2 GMV: desvio", _s, 0.1434274, 1e-6)  # guia: 14.34 %
_mu3 = np.array([0.06, 0.10, 0.14])
_S3 = np.diag([0.04, 0.09, 0.16])
_w, _m, _s = eri.cartera_gmv(_mu3, _S3)
check("Ej 4 GMV de 3 activos: w_1", _w[0], 0.590164, 1e-5)
check("Ej 4 GMV de 3 activos: rendimiento", _m, 0.0822951, 1e-6)  # guia: 8.23 %
check("Ej 4 GMV de 3 activos: desvio", _s, 0.153644, 1e-5)
_w, _m, _s = eri.cartera_tangente(_mu3, _S3, 0.03)
check("Ej 5 tangente: w_1", _w[0], 0.3385580, 1e-6)  # guia: 0.339
check("Ej 5 tangente: rendimiento", _m, 0.0988715, 1e-6)  # guia: 9.89 %
check("Ej 5 tangente: ratio de Sharpe", eri.ratio_sharpe(_m, _s, 0.03), 0.3906014, 1e-6)
check("Ej 6 beta del activo", eri.beta_capm(0.0243, 0.0324), 0.75)
check("Ej 6 rendimiento CAPM de equilibrio", eri.capm(0.75, 0.03, 0.10), 0.0825)
_vt, _vs, _ve, _r2 = eri.descomposicion_riesgo(0.28, 1.2, 0.18)
check("Ej 7 varianza sistematica", _vs, 0.046656)
check("Ej 7 varianza idiosincratica", _ve, 0.031744)
check("Ej 7 fraccion sistematica (R2)", _r2, 0.595102, 1e-5)
check("Ej 8 ratio de cobertura de varianza minima", eri.hedge_ratio(0.9, 0.03, 0.028), 0.964286, 1e-5)

print("\nClase 5 - Unidad V")
_s = eri.sandmo_media_varianza(mu=10.0, c=1.0, rho=1.0, sigma2=1.0)
check("Ej 4 producto optimo x*", _s["x"], 5.0)
check("Ej 4 producto de certeza x_c", _s["x_certeza"], 10.0)
check("Ej 4 prima marginal de riesgo", _s["prima_marginal"], 5.0)
check("Ej 6b beneficio esperado", _s["beneficio_esperado"], 37.5)
check("Ej 6b descuento por riesgo", _s["descuento_riesgo"], 12.5)
check("Ej 6b equivalente cierto", _s["equivalente_cierto"], 25.0)
_s = eri.sandmo_media_varianza(mu=12.0, c=1.0, rho=2.0, sigma2=1.0)
check("Ej 3 CARA-Normal x* = 4", _s["x"], 4.0)
check("Ej 3 prima marginal = 8", _s["prima_marginal"], 8.0)
_s = eri.sandmo_media_varianza(mu=10.0, c=1.0, rho=1e-12, sigma2=1.0)
check("Ej 4 limite neutral al riesgo: x* -> x_c", _s["x"], 10.0, 1e-6)

print("\n%d verificaciones, todas correctas.\n" % _ok)
