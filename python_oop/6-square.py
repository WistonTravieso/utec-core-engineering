#!/usr/bin/env python3
"""Módulo que define clase Square."""


class Square:
    """Clase que define un cuadrado."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa un cuadrado con un tamaño y posición opcionales."""
        self.__size = size
        self.__position = position

    def __str__(self):
        """Devuelve una representación en cadena del cuadrado."""
        if self.__size == 0:
            return ""

        lines = []
        for _ in range(self.__position[1]):
            lines.append("")
        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(lines)

    def my_print(self):
        """Imprimre el cuadrado con el caracter #."""
        print(self)

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
    @property
    def position(self):
        """Obtiene la posición del cuadrado."""
        return self.__position

    @position.setter
    def position(self, value):
        """Establece la posición del cuadrado."""
        if (not isinstance(value, tuple) or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(x) is not int or x < 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value