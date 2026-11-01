#!/usr/bin/env python3
"""Módulo que define clase Rectangle."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Clase Rectangle que hereda de BaseGeometry."""

    def __init__(self, width, height):
        """Inicializa un objeto Rectangle con ancho y alto."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calcula el área del rectángulo."""
        return self.__width * self.__height

    def __str__(self):
        """Devuelve una representación en cadena del rectángulo."""
        return f"[Rectangle] {self.__width}/{self.__height}"
