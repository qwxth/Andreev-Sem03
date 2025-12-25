#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Запуск всех тестов (TDD и BDD).
"""

import subprocess
import sys
import os


def run_command(cmd, description):
    """Запуск команды."""
    print(f"\n{'='*70}")
    print(f"🧪 {description}")
    print('='*70)

    result = subprocess.run(cmd, shell=True)

    if result.returncode != 0:
        print(f"❌ {description} - FAILED")
        return False
    else:
        print(f"✅ {description} - PASSED")
        return True


def main():
    """Главная функция."""
    print("\n" + "🎯"*35)
    print(" "*20 + "ЗАПУСК ВСЕХ ТЕСТОВ")
    print("🎯"*35)

    results = []

    # TDD тесты (unittest) - ИСПРАВЛЕНО: python -> python3
    results.append(run_command(
        "python3 -m unittest discover -s tests -p 'test_*.py' -v",
        "TDD тесты (unittest)"
    ))

    # TDD тесты (pytest)
    results.append(run_command(
        "pytest tests/ -v",
        "TDD тесты (pytest)"
    ))

    # BDD тесты (behave)
    results.append(run_command(
        "behave features/ --lang=ru",
        "BDD тесты (behave)"
    ))

    # Покрытие кода (опционально, если установлен pytest-cov)
    if os.system("python3 -c 'import pytest_cov' 2>/dev/null") == 0:
        results.append(run_command(
            "pytest --cov=src --cov-report=term-missing --cov-report=html",
            "Покрытие кода"
        ))
    else:
        print("\n" + "="*70)
        print("⚠️  Покрытие кода (пропущено - pytest-cov не установлен)")
        print("="*70)
        print("Для установки: pip install pytest-cov")

    # Итоги
    print("\n" + "="*70)
    print("📊 ИТОГОВАЯ СТАТИСТИКА")
    print("="*70)

    passed = sum(results)
    total = len(results)

    print(f"✅ Прошло: {passed}/{total}")
    print(f"❌ Не прошло: {total - passed}/{total}")

    if all(results):
        print("\n🎉 ВСЕ ТЕСТЫ ПРОШЛИ УСПЕШНО!")
        return 0
    else:
        print("\n⚠️  НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОШЛИ")
        return 1


if __name__ == '__main__':
    sys.exit(main())
