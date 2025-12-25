#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TDD тесты для решателя уравнений.
Фреймворки: unittest и pytest
"""

import unittest
import pytest
import sys
import os

# Добавляем путь к модулю
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from solver import EquationSolver


class TestQuadraticEquation(unittest.TestCase):
    """TDD тесты для квадратных уравнений (unittest)."""

    def setUp(self):
        """Подготовка перед каждым тестом."""
        self.solver = EquationSolver()

    # ==================== TDD ТЕСТ 1 ====================
    def test_two_positive_roots(self):
        """
        Квадратное уравнение с двумя положительными корнями.
        y² - 5y + 4 = 0
        Решение: (y - 4)(y - 1) = 0 => y₁ = 4, y₂ = 1
        """
        roots = self.solver.solve_quadratic(1.0, -5.0, 4.0)

        self.assertEqual(len(roots), 2, "Должно быть 2 корня")
        self.assertAlmostEqual(roots[0], 4.0, places=6)
        self.assertAlmostEqual(roots[1], 1.0, places=6)

    # ==================== TDD ТЕСТ 2 ====================
    def test_one_positive_root(self):
        """
        Квадратное уравнение с одним положительным корнем.
        y² - 2y - 3 = 0
        Решение: (y - 3)(y + 1) = 0 => y₁ = 3, y₂ = -1 (игнорируем)
        """
        roots = self.solver.solve_quadratic(1.0, -2.0, -3.0)

        self.assertEqual(len(roots), 1, "Должен быть 1 корень")
        self.assertAlmostEqual(roots[0], 3.0, places=6)

    # ==================== TDD ТЕСТ 3 ====================
    def test_no_real_roots(self):
        """
        Квадратное уравнение без действительных корней.
        y² + y + 1 = 0
        D = 1 - 4 = -3 < 0
        """
        roots = self.solver.solve_quadratic(1.0, 1.0, 1.0)

        self.assertEqual(len(roots), 0, "Не должно быть корней")

    # ==================== TDD ТЕСТ 4 ====================
    def test_linear_equation(self):
        """
        Линейное уравнение (a = 0).
        2y - 8 = 0 => y = 4
        """
        roots = self.solver.solve_quadratic(0.0, 2.0, -8.0)

        self.assertEqual(len(roots), 1)
        self.assertAlmostEqual(roots[0], 4.0, places=6)

    # ==================== TDD ТЕСТ 5 ====================
    def test_double_root(self):
        """
        Двойной корень.
        y² - 4y + 4 = 0
        (y - 2)² = 0 => y = 2
        """
        roots = self.solver.solve_quadratic(1.0, -4.0, 4.0)

        self.assertEqual(len(roots), 1)
        self.assertAlmostEqual(roots[0], 2.0, places=6)

    # ==================== TDD ТЕСТ 6 ====================
    def test_discriminant_positive(self):
        """
        Проверка вычисления дискриминанта.
        y² - 5y + 4 = 0
        D = 25 - 16 = 9
        """
        d = self.solver.get_discriminant(1.0, -5.0, 4.0)

        self.assertAlmostEqual(d, 9.0, places=6)


class TestBiquadraticEquation(unittest.TestCase):
    """TDD тесты для биквадратных уравнений (unittest)."""

    def setUp(self):
        """Подготовка перед каждым тестом."""
        self.solver = EquationSolver()

    # ==================== TDD ТЕСТ 7 ====================
    def test_four_roots(self):
        """
        Биквадратное уравнение с четырьмя корнями.
        x⁴ - 5x² + 4 = 0
        y² - 5y + 4 = 0 => y = 4, y = 1
        x² = 4 => x = ±2
        x² = 1 => x = ±1
        """
        roots = self.solver.solve_biquadratic(1.0, -5.0, 4.0)

        self.assertEqual(len(roots), 4)
        expected = [-2.0, -1.0, 1.0, 2.0]
        for i, expected_val in enumerate(expected):
            self.assertAlmostEqual(roots[i], expected_val, places=6)

    # ==================== TDD ТЕСТ 8 ====================
    def test_three_roots_with_zero(self):
        """
        Биквадратное уравнение с нулевым корнем.
        x⁴ - 4x² = 0
        x²(x² - 4) = 0 => x = 0, x = ±2
        """
        roots = self.solver.solve_biquadratic(1.0, -4.0, 0.0)

        self.assertEqual(len(roots), 3)
        self.assertAlmostEqual(roots[0], -2.0, places=6)
        self.assertAlmostEqual(roots[1], 0.0, places=6)
        self.assertAlmostEqual(roots[2], 2.0, places=6)

    # ==================== TDD ТЕСТ 9 ====================
    def test_no_roots(self):
        """
        Биквадратное уравнение без корней.
        x⁴ + x² + 1 = 0
        """
        roots = self.solver.solve_biquadratic(1.0, 1.0, 1.0)

        self.assertEqual(len(roots), 0)

    # ==================== TDD ТЕСТ 10 ====================
    def test_two_roots(self):
        """
        Биквадратное уравнение с двумя корнями.
        x⁴ - 16 = 0
        y² - 16 = 0 => y = 16 (берём только положительный)
        Ошибка в предыдущей версии: y² = 16, а не y = 16!
        y = ±4, берём y = 4
        x² = 4 => x = ±2
        """
        roots = self.solver.solve_biquadratic(1.0, 0.0, -16.0)

        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], -2.0, places=6)  # ИСПРАВЛЕНО!
        self.assertAlmostEqual(roots[1], 2.0, places=6)   # ИСПРАВЛЕНО!


# ============================================================================
# PYTEST ТЕСТЫ
# ============================================================================

@pytest.fixture
def solver():
    """Фикстура для создания решателя."""
    return EquationSolver()


class TestPytestQuadratic:
    """TDD тесты с pytest для квадратных уравнений."""

    def test_two_roots_pytest(self, solver):
        """Pytest: два корня."""
        roots = solver.solve_quadratic(1.0, -5.0, 4.0)
        assert len(roots) == 2
        assert pytest.approx(roots[0], 0.000001) == 4.0
        assert pytest.approx(roots[1], 0.000001) == 1.0

    def test_no_roots_pytest(self, solver):
        """Pytest: нет корней."""
        roots = solver.solve_quadratic(1.0, 1.0, 1.0)
        assert len(roots) == 0


class TestPytestBiquadratic:
    """TDD тесты с pytest для биквадратных уравнений."""

    @pytest.mark.parametrize("a,b,c,expected_count", [
        (1.0, -5.0, 4.0, 4),    # Четыре корня
        (1.0, -4.0, 0.0, 3),    # Три корня
        (1.0, 1.0, 1.0, 0),     # Нет корней
        (1.0, 0.0, -16.0, 2),   # Два корня
    ])
    def test_parametrized(self, solver, a, b, c, expected_count):
        """Pytest: параметризованный тест."""
        roots = solver.solve_biquadratic(a, b, c)
        assert len(roots) == expected_count


if __name__ == '__main__':
    # Запуск unittest тестов
    unittest.main(verbosity=2)
