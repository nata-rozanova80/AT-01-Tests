def count_vowels(s):
    """
    Считает количество гласных букв в строке.

    Args:
        s (str): Входная строка.

    Returns:
        int: Количество гласных в строке.
    """
    vowels = "aeiouAEIOUаеиоуыэюяАЕИОУЫЭЮЯ"
    return sum(1 for char in s if char in vowels)
