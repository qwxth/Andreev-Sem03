#!/usr/bin/env python3
"""
Главный модуль программы дл�� тестирования классов геометрических фигур
"""

from lab_python_oop import Rectangle, Circle, Square
from colorama import init, Fore, Style


def print_colored(text, color):
    """
    Функция для цветного вывода текста с использованием colorama
    """
    colors = {
        'синий': Fore.BLUE,
        'синего': Fore.BLUE,
        'зеленый': Fore.GREEN,
        'зеленого': Fore.GREEN,
        'красный': Fore.RED,
        'красного': Fore.RED
    }

    color_code = colors.get(color.lower(), Fore.WHITE)
    print(color_code + text + Style.RESET_ALL)


def main():
    """
    Главная функция программы
    """
    # Инициализация colorama для Windows
    init()

    # Номер варианта (замените на свой номер по списку)
    N = 10  # Измените на свой номер варианта

    print("=" * 70)
    print(f"Лабораторная работа: Работа с классами")
    print(f"Вариант №{N}")
    print("=" * 70)
    print()

    # Создание прямоугольника синего цвета
    rect = Rectangle(N, N, "синего")
    print_colored(repr(rect), "синего")
