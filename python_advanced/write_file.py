#!/usr/bin/env python3
""" Módulo que contiene la función write_file para escribir en un archivo"""


def write_file(filename="", text=""):
    """Escribe contenido en un archivo de texto."""
    with open(filename, "w", encoding="utf-8") as file:
        written = file.write(text)
    print(written)
