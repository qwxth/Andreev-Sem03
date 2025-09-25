"""
Модуль содержит класс Square
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    Класс "Квадрат" наследуется от класса "Прямоугольник"
    """

    # Поле класса с названием фигуры
    FIGURE_TYPE = "Квадрат"

    def __init__(self, side, color):
        """
        Конструктор класса

        :param side: длина стороны квадрата
        :param color: цвет квадрата
        """
        # Вызов конструктора базового класса
        super().__init__(side, side, color)

    def __repr__(self):
        """
        Метод для строкового представления объекта
        """
        return "{} {} цвета со стороной {:.1f} площадью {:.1f}".format(
            self.FIGURE_TYPE,
            self.fc.color,
            self.width,
            self.square()
        )