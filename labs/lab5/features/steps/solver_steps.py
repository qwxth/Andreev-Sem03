#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Шаги для BDD тестов (behave).
"""

from behave import given, when, then
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from solver import EquationSolver


# ============================================================================
# GIVEN (Дано) - начальное состояние
# ============================================================================

@given('у меня есть решатель уравнений')
def step_create_solver(context):
    """Создание решателя."""
    context.solver = EquationSolver()


@given('биквадратное уравнение x⁴ - 5x² + 4 = 0')
def step_equation_1(context):
    """Уравнение 1."""
    context.a, context.b, context.c = 1.0, -5.0, 4.0


@given('биквадратное уравнение x⁴ - 4x² = 0')
def step_equation_2(context):
    """Уравнение 2."""
    context.a, context.b, context.c = 1.0, -4.0, 0.0


@given('биквадратное уравнение x⁴ + x² + 1 = 0')
def step_equation_3(context):
    """Уравнение 3."""
    context.a, context.b, context.c = 1.0, 1.0, 1.0


@given('квадратное уравнение y² - 5y + 4 = 0')
def step_quad_equation_1(context):
    """Квадратное уравнение 1."""
    context.a, context.b, context.c = 1.0, -5.0, 4.0
    context.is_quadratic = True


@given('квадратное уравнение y² + y + 1 = 0')
def step_quad_equation_2(context):
    """Квадратное уравнение 2."""
    context.a, context.b, context.c = 1.0, 1.0, 1.0
    context.is_quadratic = True


# ============ НОВЫЕ ШАГИ ДЛЯ ПАРАМЕТРИЗОВАННЫХ СЦЕНАРИЕВ ============

@given('биквадратное уравнение с коэффициентами {a:g}, {b:g}, {c:g}')
def step_equation_params(context, a, b, c):
    """Уравнение с параметрами (использует :g для чисел)."""
    context.a, context.b, context.c = float(a), float(b), float(c)


@given('биквадратное уравнение с коэффициентами {a:d}, {b:d}, {c:d}')
def step_equation_params_int(context, a, b, c):
    """Уравнение с целыми параметрами."""
    context.a, context.b, context.c = float(a), float(b), float(c)


# ============================================================================
# WHEN (Когда) - действие
# ============================================================================

@when('я решаю это уравнение')
def step_solve_biquadratic(context):
    """Решение биквадратного уравнения."""
    context.roots = context.solver.solve_biquadratic(
        context.a, context.b, context.c
    )


@when('я решаю квадратное уравнение')
def step_solve_quadratic(context):
    """Решение квадратного уравнения."""
    context.roots = context.solver.solve_quadratic(
        context.a, context.b, context.c
    )


# ============================================================================
# THEN (Тогда) - проверка результата
# ============================================================================

@then('я получаю {count:d} корня')
@then('я получаю {count:d} корней')
def step_check_count(context, count):
    """Проверка количества корней."""
    actual = len(context.roots)
    assert actual == count, \
        f"Ожидалось {count} корней, получено {actual}. Корни: {context.roots}"


@then('корни равны {expected}')
def step_check_values(context, expected):
    """Проверка значений корней."""
    expected_list = [float(x.strip()) for x in expected.split(',')]
    actual = context.roots

    assert len(actual) == len(expected_list), \
        f"Количество не совпадает: {actual} != {expected_list}"

    for i, (a, e) in enumerate(zip(actual, expected_list)):
        assert abs(a - e) < 1e-6, \
            f"Корень {i}: {a} != {e}"


# ============ ИСПРАВЛЕННЫЙ ШАГ ============

@then('среди корней есть {value:d}')
@then('среди корней есть {value:f}')
@then('среди корней есть {value:g}')
def step_check_contains(context, value):
    """Проверка наличия конкретного корня."""
    value = float(value)
    roots = context.roots
    assert any(abs(r - value) < 1e-6 for r in roots), \
        f"Корень {value} не найден среди {roots}"


@then('все корни положительные')
def step_check_positive(context):
    """Проверка положительности корней."""
    roots = context.roots
    assert all(r > 0 for r in roots), \
        f"Не все корни положительные: {roots}"
