#!/usr/bin/env python3
# qr.py - программа для решения квадратного уравнения Ax^2 + Bx + C = 0

import sys
import math


def get_coefficient(coef_name, coef_value=None):
    """
    Получает коэффициент из командной строки или с клавиатуры.
    Проверяет корректность ввода.
    """
    # Если значение передано из командной строки
    if coef_value is not None:
        try:
            return float(coef_value)
        except ValueError:
            print(f"Некорректное значение коэффициента {coef_name}: '{coef_value}'")

    # Ввод с клавиатуры с проверкой корректности
    while True:
        try:
            value = input(f"Введите коэффициент {coef_name}: ")
            return float(value)
        except ValueError:
            print(f"Некорректное значение! Попробуйте еще раз.")


def solve_quadratic(a, b, c):
    """
    Решает квадратное уравнение ax^2 + bx + c = 0
    Возвращает список действительных корней
    """
    # Проверка, является ли уравнение квадратным
    if a == 0:
        if b == 0:
            if c == 0:
                print("Уравнение имеет бесконечное множество решений")
                return []
            else:
                print("Уравнение не имеет решений")
                return []
        else:
            # Линейное уравнение bx + c = 0
            x = -c / b
            return [x]

    # Вычисление дискриминанта
    discriminant = b * b - 4 * a * c

    print(f"\nУравнение: {a}x² + {b}x + {c} = 0")
    print(f"Дискриминант D = {discriminant}")

    # Анализ дискриминанта
    if discriminant > 0:
        # Два различных действительных корня
        sqrt_d = math.sqrt(discriminant)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return [x1, x2]
    elif discriminant == 0:
        # Один действительный корень (два совпадающих)
        x = -b / (2 * a)
        return [x]
    else:
        # Нет действительных корней
        print("Уравнение не имеет действительных корней (D < 0)")
        return []


def main():
    """
    Главная функция программы
    """
    print("Решение квадратного уравнения Ax² + Bx + C = 0")
    print("-" * 50)

    # Получение коэффициентов из командной строки или с клавиатуры
    a_value = sys.argv[1] if len(sys.argv) > 1 else None
    b_value = sys.argv[2] if len(sys.argv) > 2 else None
    c_value = sys.argv[3] if len(sys.argv) > 3 else None

    # Получение коэффициентов с проверкой корректности
    a = get_coefficient("A", a_value)
    b = get_coefficient("B", b_value)
    c = get_coefficient("C", c_value)

    # Решение уравнения
    roots = solve_quadratic(a, b, c)

    # Вывод результатов
    if len(roots) == 0:
        if a != 0:  # Если это было квадратное уравнение
            pass  # Сообщение уже выведено в solve_quadratic
    elif len(roots) == 1:
        if a == 0:
            print(f"\nЛинейное уравнение имеет один корень: x = {roots[0]}")
        else:
            print(f"\nУравнение имеет один действительный корень: x = {roots[0]}")
    else:
        print(f"\nУравнение имеет два действительных корня:")
        print(f"x₁ = {roots[0]}")
        print(f"x₂ = {roots[1]}")


if __name__ == "__main__":
    main()