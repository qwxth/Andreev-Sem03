"""
Модуль содержит класс Rectangle
"""
from .figure import Figure
from .color import FigureColor


class Rectangle(Figure):
    """
    Класс "Прямоугольник" наследуется от класса "Геометрическая фигура"
    """

    # Поле класса с названием фигуры
    FIGURE_TYPE = "Прямоугольник"

    def __init__(self, width, height, color):
        """
        Конструктор класса

        :param width: ширина прямоугольника
        :param height: высота прямоугольника
        :param color: цвет прямоугольника
        """
        self.width = width
        self.height = height
        self.fc = FigureColor()
        self.fc.color = color

    def square(self):
        """
        Метод вычисления площади прямоугольника
        """
        return self.width * self.height

    def __repr__(self):
        """
        Метод для строкового представления объекта
        """
        return "{} {} цвета шириной {:.1f} и высотой {:.1f} площадью {:.1f}".format(
            self.FIGURE_TYPE,
            self.fc.color,
            self.width,
            self.height,
            self.square()
        )

    @classmethod
    def get_figure_type(cls):
        """
        Метод класса для получения типа фигуры
        """
        return cls.FIGURE_TYPE