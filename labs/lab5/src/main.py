#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Главный модуль программы.
"""

import sys
from solver import EquationSolver, print_equation, print_results


def get_coefficient(prompt: str, arg_value: str = None) -> float:
    """Получение коэффициента от пользователя."""
    if arg_value is not None:
        try:
            value = float(arg_value)
            print(f"{prompt}{value} (из командной строки)")
            return value
        except ValueError:
            print(f"⚠️  Некорректное значение '{arg_value}'")

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠️  Введите число!")
        except KeyboardInterrupt:
            print("\n\n👋 Выход")
            sys.exit(0)


def main():
    """Главная функция."""
    print("\n" + "🎯 "*20)
    print("    РЕШЕНИЕ БИКВАДРАТНОГО УРАВНЕНИЯ")
    print("    A*x⁴ + B*x² + C = 0")
    print("🎯 "*20 + "\n")

    args = sys.argv[1:]
    while len(args) < 3:
        args.append(None)

    # Получение коэффициентов
    a = get_coefficient("Введите A: ", args[0])
    b = get_coefficient("Введите B: ", args[1])
    c = get_coefficient("Введите C: ", args[2])

    # Решение
    print_equation(a, b, c)
    solver = EquationSolver()
    roots = solver.solve_biquadratic(a, b, c)
    print_results(roots)


if __name__ == "__main__":
    main()
