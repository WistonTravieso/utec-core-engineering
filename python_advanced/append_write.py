#!/usr/bin/env python3
""" Módulo que contiene la función para agregar contenido a un archivo"""


def append_write(filename="", text=""):
    """Agrega contenido a un archivo de texto."""
    with open(filename, "a", encoding="utf-8") as file:
        added = file.write(text)
    print(added)
