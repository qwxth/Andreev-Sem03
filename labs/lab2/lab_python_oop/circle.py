"""
Модуль содержит класс Circle
"""
import math
from .figure import Figure
from .color import FigureColor


class Circle(Figure):
    """
    Класс "Круг" наследуется от класса "Геометрическая фигура"
    """

    # Поле класса с названием фигуры
    FIGURE_TYPE = "Круг"

    def __init__(self, radius, color):
        """
        Конструктор класса

        :param radius: радиус круга
        :param color: цвет круга
        """
        self.radius = radius
        self.fc = FigureColor()
        self.fc.color = color

    def square(self):
        """
        Метод вычисления площади круга
        """
        return math.pi * self.radius * self.radius

    def __repr__(self):
        """
        Метод для строкового представления объекта
        """
        return "{} {} цвета радиусом {:.1f} площадью {:.1f}".format(
            self.FIGURE_TYPE,
            self.fc.color,
            self.radius,
            self.square()
        )

    @classmethod
    def get_figure_type(cls):
        """
        Метод класса для получения типа фигуры
        """
        return cls.FIGURE_TYPE