#!/usr/bin/env python3
"""Módulo que define clase Square."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Clase Square que hereda de Rectangle."""

    def __init__(self, size):
        """Inicializa un objeto Square con tamaño."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calcula el área del cuadrado."""
        return self.__size ** 2
