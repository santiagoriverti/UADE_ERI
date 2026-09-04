# -*- coding: utf-8 -*-
"""
Ejecuta un notebook de punta a punta LOCALMENTE y reporta si falla algo.

Es el test del repositorio: cada notebook cierra sus ejercicios con `assert`, de modo
que "ejecuta limpio" equivale a "todos los resultados coinciden con la guia".

El problema que resuelve: la celda de setup de cada notebook descarga `eri_utils.py`
y los datasets desde raw.githubusercontent, lo que exige (a) tener `wget`, que en
Windows no viene, y (b) que lo que se prueba sea la version ya pusheada, no la local.
Este script parchea esas lineas en memoria para que el notebook use `src/` y `data/`
del repositorio, sin tocar el archivo en disco.

Uso:
    python tools/probar_nb.py notebooks/04_unidad_IV_finanzas.ipynb
    python tools/probar_nb.py --todos
    python tools/probar_nb.py --todos --saltear-esqueletos

Requiere las dependencias de `requirements-dev.txt`:
    pip install -r requirements-dev.txt
"""

import argparse
import glob
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _parche(raiz: str) -> str:
    """Codigo que reemplaza a la descarga de Colab: apunta a src/ y data/ locales."""
    return (
        "import sys, os\n"
        "sys.path.insert(0, r'%s')\n"
        "os.chdir(r'%s')\n"
        "import matplotlib\n"
        "matplotlib.use('Agg')          # sin ventana grafica\n"
        "from IPython.display import display\n"
    ) % (os.path.join(raiz, "src"), os.path.join(raiz, "data"))


def probar(ruta: str, timeout: int = 900, verboso: bool = False):
    """Ejecuta un notebook. Devuelve (ok, mensaje, n_asserts)."""
    import nbformat
    from nbclient import NotebookClient
    from nbclient.exceptions import CellExecutionError

    nb = nbformat.read(ruta, as_version=4)

    n_asserts = sum(c.source.count("assert ") for c in nb.cells if c.cell_type == "code")

    parcheado = False
    for celda in nb.cells:
        if celda.cell_type == "code" and "wget" in celda.source:
            lineas = [l for l in celda.source.split("\n") if not l.strip().startswith("!wget")]
            celda.source = _parche(RAIZ) + "\n".join(lineas)
            parcheado = True
            break
    if not parcheado:
        return False, "no encontre la celda de setup con el wget", n_asserts

    cliente = NotebookClient(nb, timeout=timeout, kernel_name="python3", allow_errors=False)
    try:
        cliente.execute()
    except CellExecutionError as e:
        return False, str(e).strip().split("\n")[-1], n_asserts
    except Exception as e:  # kernel caido, timeout, etc.
        return False, "%s: %s" % (type(e).__name__, e), n_asserts

    if verboso:
        print()
        for i, celda in enumerate(nb.cells):
            if celda.cell_type != "code":
                continue
            for salida in celda.get("outputs", []):
                if salida.get("output_type") == "stream":
                    txt = salida.get("text", "").rstrip()
                    if txt:
                        print("[celda %02d] %s" % (i, txt.replace("\n", "\n           ")))

    return True, "", n_asserts


def es_esqueleto(ruta: str) -> bool:
    """Un esqueleto es un notebook todavia sin desarrollar (lleva el aviso de obra)."""
    import nbformat
    nb = nbformat.read(ruta, as_version=4)
    return any("Notebook en construcción" in c.source for c in nb.cells if c.cell_type == "markdown")


def main() -> int:
    ap = argparse.ArgumentParser(description="Ejecuta notebooks y verifica que corran limpios.")
    ap.add_argument("notebook", nargs="?", help="ruta al .ipynb (relativa a la raiz del repo)")
    ap.add_argument("--todos", action="store_true", help="ejecuta todos los notebooks de notebooks/")
    ap.add_argument("--saltear-esqueletos", action="store_true",
                    help="omite los notebooks que todavia son esqueleto")
    ap.add_argument("--verboso", "-v", action="store_true", help="imprime las salidas de cada celda")
    ap.add_argument("--timeout", type=int, default=900, help="segundos por notebook (default 900)")
    args = ap.parse_args()

    if args.todos:
        rutas = sorted(glob.glob(os.path.join(RAIZ, "notebooks", "*.ipynb")))
    elif args.notebook:
        rutas = [args.notebook if os.path.isabs(args.notebook)
                 else os.path.join(RAIZ, args.notebook)]
    else:
        ap.print_help()
        return 2

    fallas = 0
    for ruta in rutas:
        nombre = os.path.basename(ruta)
        if args.saltear_esqueletos and es_esqueleto(ruta):
            print("  omitido    %-52s (esqueleto)" % nombre)
            continue

        ok, mensaje, n = probar(ruta, timeout=args.timeout, verboso=args.verboso)
        if ok:
            print("  OK         %-52s %d asserts" % (nombre, n))
        else:
            print("  FALLA      %-52s %s" % (nombre, mensaje))
            fallas += 1

    print()
    if fallas:
        print("%d de %d notebooks fallaron." % (fallas, len(rutas)))
        return 1
    print("Todos los notebooks ejecutados corren limpios.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
