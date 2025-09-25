"""
Модуль содержит абстрактный класс Figure
"""
from abc import ABC, abstractmethod


class Figure(ABC):
    """
    Абстрактный класс "Геометрическая фигура"
    """

    @abstractmethod
    def square(self):
        """
        Абстрактный метод для вычисления площади фигуры
        """
        pass