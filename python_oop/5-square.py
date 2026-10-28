#!/usr/bin/env python3
"""Módulo que define clase Square."""


class Square:
    """Clase que define un cuadrado."""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """Imprimre en stdout el cuadrado con el caracter #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

    def area(self):
        """Calcula el área del cuadrado."""
        return self.__size ** 2

    @property
    def size(self):
        """Obtiene el tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece el tamaño del cuadrado."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
