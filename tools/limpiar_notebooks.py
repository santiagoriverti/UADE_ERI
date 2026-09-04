# -*- coding: utf-8 -*-
"""
Borra las salidas de todos los notebooks de `notebooks/` antes de commitear.

Se versiona el codigo, no el resultado de ejecutarlo: un notebook con salidas genera
diffs de miles de lineas por un grafico que cambio un pixel y vuelve el historial
ilegible. Ver `docs/ARQUITECTURA.md`, seccion 3.6.

Uso:
    python tools/limpiar_notebooks.py            # limpia notebooks/
    python tools/limpiar_notebooks.py ruta.ipynb # limpia uno solo
"""

import glob
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def limpiar(ruta: str) -> bool:
    """Borra outputs y execution_count. Devuelve True si el archivo cambio."""
    with io.open(ruta, encoding="utf-8") as f:
        nb = json.load(f)

    cambio = False
    for celda in nb.get("cells", []):
        if celda.get("cell_type") != "code":
            continue
        if celda.get("outputs"):
            celda["outputs"] = []
            cambio = True
        if celda.get("execution_count") is not None:
            celda["execution_count"] = None
            cambio = True
        # Colab guarda ids de salida y metadatos de widgets que tambien ensucian el diff.
        meta = celda.get("metadata", {})
        for clave in ("outputId", "executionInfo", "colab"):
            if clave in meta:
                del meta[clave]
                cambio = True

    if nb.get("metadata", {}).get("widgets"):
        del nb["metadata"]["widgets"]
        cambio = True

    if cambio:
        with io.open(ruta, "w", encoding="utf-8") as f:
            json.dump(nb, f, ensure_ascii=False, indent=1)
            f.write("\n")
    return cambio


def main() -> None:
    if len(sys.argv) > 1:
        rutas = sys.argv[1:]
    else:
        rutas = sorted(glob.glob(os.path.join(RAIZ, "notebooks", "*.ipynb")))

    if not rutas:
        print("No se encontraron notebooks.")
        return

    modificados = 0
    for ruta in rutas:
        nombre = os.path.basename(ruta)
        if limpiar(ruta):
            print("  limpiado   %s" % nombre)
            modificados += 1
        else:
            print("  ya limpio  %s" % nombre)

    print("\n%d de %d notebooks modificados." % (modificados, len(rutas)))


if __name__ == "__main__":
    main()
