import unittest
from main import add, subtract, multiply, divide, safe_modulo

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertNotEqual(add(3, 7), 9)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)
        self.assertNotEqual(subtract(4, 2), 1)

    def test_multiply(self):
        self.assertNotEqual(multiply(2, 5), 12)
        self.assertEqual(multiply(3, 6), 18)

    def test_divide(self):
        self.assertNotEqual(divide(4, 2), 3)
        self.assertEqual(divide(20, 5), 4)

    def test_safe_modulo(self):
        print("Начало процедуры test_safe_modulo")
        # Проверяет корректность работы функции safe_modulo.

        # Тесты с нормальными числами
        self.assertEqual(safe_modulo(10, 3), 1, "Ошибка в тесте: 10 % 3")
        self.assertEqual(safe_modulo(10, 0), "Ошибка: Деление на ноль невозможно.", "Ошибка в тесте: 10 % 0")
        print("Все тесты пройдены!")
# Запуск тестов
if __name__ == '__main__':
    unittest.main()