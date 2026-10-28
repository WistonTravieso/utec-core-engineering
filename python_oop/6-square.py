#!/usr/bin/env python3
"""Módulo que define clase Square."""


class Square:
    """Clase que define un cuadrado."""

    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (not isinstance(position, tuple) or len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def __str__(self):
        """Devuelve una representación en cadena del cuadrado."""
        if self.__size == 0:
            return ""
        else:
            lines = []
            for _ in range(self.__position[1]):
                lines.append("")
            for _ in range(self.__size):
                lines.append(" " * self.__position[0] + "#" * self.__size)
            return "\n".join(lines)

    def my_print(self):
        """Imprimre el cuadrado con el caracter #."""
        print(self.__str__())
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

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
