# -*- coding: utf-8 -*-
"""
Convierte un archivo de texto plano (`.nbsrc`) en un notebook `.ipynb`.

Escribir un notebook grande editando JSON a mano es incomodo, y hacerlo dentro de
Colab obliga a ir y venir del navegador. Este helper permite redactar el notebook
como un unico archivo de texto, con las celdas separadas por marcadores, y generarlo
de una sola vez.

Formato del `.nbsrc`:

    #%% md
    # Titulo en markdown
    Texto normal, con $LaTeX$ si hace falta.

    #%% code
    print("una celda de codigo")

    #%% md
    Otra celda de markdown.

Uso:
    python tools/nbgen.py borrador.nbsrc notebooks/03_unidad_III_reparto_del_riesgo.ipynb

IMPORTANTE — cual es la fuente de verdad. Una vez generado, **el `.ipynb` es el
archivo canonico**: es lo que se versiona, lo que abre Colab y lo que se edita de ahi
en adelante. Los `.nbsrc` son borradores de trabajo y NO se versionan (estan en
`.gitignore`). Si volves a generar sobre un notebook ya editado, perdes esas ediciones.
"""

import argparse
import io
import json
import os
import sys

MARCADORES = {"#%% md": "markdown", "#%% code": "code"}


def _fuente(texto: str):
    """Convierte un bloque de texto en la lista de lineas que espera el formato ipynb."""
    lineas = texto.split("\n")
    return [l + "\n" for l in lineas[:-1]] + [lineas[-1]]


def construir(ruta_src: str, ruta_dest: str) -> int:
    with io.open(ruta_src, encoding="utf-8") as f:
        crudo = f.read()

    celdas = []
    tipo_actual, acumulado = None, []

    def cerrar():
        if tipo_actual is None:
            return
        texto = "\n".join(acumulado).strip("\n")
        if not texto.strip():
            return
        if tipo_actual == "markdown":
            celdas.append({"cell_type": "markdown", "metadata": {},
                           "source": _fuente(texto)})
        else:
            celdas.append({"cell_type": "code", "execution_count": None,
                           "metadata": {}, "outputs": [], "source": _fuente(texto)})

    for linea in crudo.split("\n"):
        marcador = MARCADORES.get(linea.rstrip())
        if marcador:
            cerrar()
            tipo_actual, acumulado = marcador, []
        else:
            acumulado.append(linea)
    cerrar()

    if not celdas:
        raise SystemExit("El archivo no tiene celdas. Falta algun marcador '#%% md' o '#%% code'?")

    nb = {
        "cells": celdas,
        "metadata": {
            "colab": {"provenance": [], "toc_visible": True},
            "kernelspec": {"display_name": "Python 3", "name": "python3"},
            "language_info": {"name": "python"},
        },
        "nbformat": 4,
        "nbformat_minor": 0,
    }

    with io.open(ruta_dest, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
        f.write("\n")

    return len(celdas)


def main() -> int:
    ap = argparse.ArgumentParser(description="Genera un .ipynb a partir de un .nbsrc.")
    ap.add_argument("origen", help="archivo .nbsrc")
    ap.add_argument("destino", help="archivo .ipynb a generar")
    ap.add_argument("--forzar", action="store_true",
                    help="sobrescribe el destino si ya existe")
    args = ap.parse_args()

    if os.path.exists(args.destino) and not args.forzar:
        print("El destino ya existe: %s" % args.destino)
        print("Si lo sobrescribis, perdes cualquier edicion hecha directamente sobre el")
        print("notebook (por ejemplo, desde Colab). Usa --forzar si estas seguro.")
        return 1

    n = construir(args.origen, args.destino)
    print("OK  %s -> %s  (%d celdas)" % (os.path.basename(args.origen),
                                         os.path.basename(args.destino), n))
    print("Ahora verificalo:  python tools/probar_nb.py %s" % args.destino)
    return 0


if __name__ == "__main__":
    sys.exit(main())
