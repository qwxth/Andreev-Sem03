"""
Модуль содержит класс FigureColor для работы с цветом фигуры
"""


class FigureColor:
    """
    Класс "Цвет фигуры"
    """

    def __init__(self):
        self._color = None

    @property
    def color(self):
        """
        Геттер для получения цвета
        """
        return self._color

    @color.setter
    def color(self, value):
        """
        Сеттер для установки цвета
        """
        self._color = value

    def __str__(self):
        return str(self._color)