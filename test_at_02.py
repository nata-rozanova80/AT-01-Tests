import pytest
from main_at_02 import count_vowels

def test_only_vowels():
    """Проверка, что функция правильно считает гласные в строке, содержащей только гласные."""
    assert count_vowels("aeiouAEIOUаеиоуыэюяАЕИОУЫЭЮЯ") == 28

def test_no_vowels():
    """Проверка, что функция возвращает 0 для строки, не содержащей гласных."""
    assert count_vowels("bcdfgBCDFG1234!@#$") == 0

def test_mixed_string():
    """Проверка, что функция правильно считает гласные в смешанных строках."""
    assert count_vowels("Hello World!") == 3
    assert count_vowels("Привет Мир!") == 3
    assert count_vowels("Mixed Вариант Текста") == 7

@pytest.mark.parametrize("input_string, expected_count", [
    ("", 0),                               # Пустая строка
    ("aeiou", 5),                          # Только латинские гласные (строчные)
    ("AEIOU", 5),                          # Только латинские гласные (прописные)
    ("Привет", 2),                         # Только кириллические гласные
    ("1234!@#$", 0),                       # Только символы и числа
    ("Hello Привет!", 4)                   # Смешанные языки
])
def test_parametrized(input_string, expected_count):
    """Параметризованный тест для различных строк."""
    assert count_vowels(input_string) == expected_count
