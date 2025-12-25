#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль для решения биквадратных уравнений.
"""

import math
from typing import List


class EquationSolver:
    """Решатель уравнений."""

    EPSILON = 1e-10

    @staticmethod
    def solve_quadratic(a: float, b: float, c: float) -> List[float]:
        """
        Решение квадратного уравнения a*y^2 + b*y + c = 0.
        Возвращает только неотрицательные корни для использования в биквадратном.

        Args:
            a, b, c: Коэффициенты уравнения

        Returns:
            List[float]: Список неотрицательных корней
        """
        roots = []

        # Вырожденный случай: a = 0 (линейное уравнение)
        if abs(a) < EquationSolver.EPSILON:
            if abs(b) < EquationSolver.EPSILON:
                # Уравнение вида c = 0
                return roots  # Пустой список или бесконечно много решений
            else:
                # Линейное: b*y + c = 0 => y = -c/b
                y = -c / b
                if y >= 0:
                    roots.append(y)
                return roots

        # Квадратное уравнение
        discriminant = b**2 - 4*a*c

        if discriminant < 0:
            return roots  # Нет действительных корней

        sqrt_d = math.sqrt(discriminant)
        y1 = (-b + sqrt_d) / (2 * a)
        y2 = (-b - sqrt_d) / (2 * a)

        # Добавляем только неотрицательные корни
        if y1 >= -EquationSolver.EPSILON:  # Учитываем погрешность
            roots.append(max(0, y1))
        if y2 >= -EquationSolver.EPSILON and abs(y1 - y2) > EquationSolver.EPSILON:
            roots.append(max(0, y2))

        return sorted(roots, reverse=True)  # От большего к меньшему

    @staticmethod
    def solve_biquadratic(a: float, b: float, c: float) -> List[float]:
        """
        Решение биквадратного уравнения A*x^4 + B*x^2 + C = 0.

        Args:
            a, b, c: Коэффициенты уравнения

        Returns:
            List[float]: Отсортированный список действительных корней
        """
        # Замена y = x^2
        y_roots = EquationSolver.solve_quadratic(a, b, c)

        if not y_roots:
            return []

        # Извлечение корней x из y = x^2
        x_roots = []

        for y in y_roots:
            if y > EquationSolver.EPSILON:
                x = math.sqrt(y)
                x_roots.extend([-x, x])
            elif abs(y) <= EquationSolver.EPSILON:
                x_roots.append(0.0)

        return sorted(x_roots)

    @staticmethod
    def get_discriminant(a: float, b: float, c: float) -> float:
        """
        Вычисление дискриминанта квадратного уравнения.

        Args:
            a, b, c: Коэффициенты

        Returns:
            float: Значение дискриминанта
        """
        return b**2 - 4*a*c


def print_equation(a: float, b: float, c: float, eq_type: str = "biquadratic"):
    """Вывод уравнения."""
    if eq_type == "biquadratic":
        print(f"\n{'='*60}")
        print(f"🔢 Биквадратное уравнение: {a}*x⁴ + {b}*x² + {c} = 0")
        print(f"{'='*60}")
    else:
        print(f"\n📊 Квадратное уравнение: {a}*y² + {b}*y + {c} = 0")


def print_results(roots: List[float]):
    """Вывод результатов."""
    print(f"\n{'='*60}")
    print("📋 РЕЗУЛЬТАТЫ:")
    print(f"{'='*60}")

    if not roots:
        print("❌ Действительных корней нет.")
    else:
        print(f"✅ Найдено корней: {len(roots)}")
        for i, root in enumerate(roots, 1):
            print(f"  x{i} = {root:.6f}")

    print(f"{'='*60}\n")
