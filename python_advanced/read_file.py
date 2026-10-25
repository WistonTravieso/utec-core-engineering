#!/usr/bin/env python3
""" Módulo que contiene la función read_file para leer un archivo de texto y mostrar su contenido en la consola."""

def read_file(filename=""):
    """Lee un archivo de texto y muestra su contenido en la consola."""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    print(content, end="")
