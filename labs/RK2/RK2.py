# -*- coding: utf-8 -*-
import unittest

from rk1_refactored import (
    create_test_data,
    make_one_to_many,
    make_many_to_many,
    task1,
    task2,
    task3,
)


class TestRK1(unittest.TestCase):
    def setUp(self):
        self.suppliers, self.details, self.link_table = create_test_data()
        self.one_to_many = make_one_to_many(self.suppliers, self.details)
        self.many_to_many = make_many_to_many(
            self.suppliers, self.details, self.link_table
        )

    def test_task1(self):
        """Проверка сортировки списка деталь–поставщик (1‑ко‑многим)."""
        expected = [
            ("Болт", 10, "МеталлПром"),
            ("Втулка", 12, "МеталлПром"),
            ("Гайка", 7, "Иванов ИП"),
            ("Крышка", 15, "Детали+"),
            ("Прокладка", 8, "СтройСнаб"),
            ("Ручка", 20, "Технолов"),
            ("Шайба", 5, "Иванов ИП"),
        ]
        self.assertEqual(task1(self.one_to_many), expected)

    def test_task2(self):
        """Проверка подсчёта количества деталей у каждого поставщика."""
        expected = [
            ("Иванов ИП", 2),
            ("МеталлПром", 2),
            ("Детали+", 1),
            ("Технолов", 1),
            ("СтройСнаб", 1),
        ]
        self.assertEqual(task2(self.suppliers, self.details), expected)

    def test_task3(self):
        """Проверка выборки деталей, оканчивающихся на «ка» (многие‑ко‑многим)."""
        expected = [
            ("Гайка", "Иванов ИП"),
            ("Втулка", "МеталлПром"),
            ("Крышка", "МеталлПром"),
            ("Крышка", "Детали+"),
            ("Ручка", "Технолов"),
            ("Прокладка", "СтройСнаб"),
            ("Втулка", "СтройСнаб"),
        ]
        self.assertEqual(task3(self.many_to_many), expected)

name = "main"
if name == "main":
    unittest.main()
