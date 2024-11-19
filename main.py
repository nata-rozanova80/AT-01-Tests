
def add(a, b):
   return a + b

def subtract(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
   return a / b


def safe_modulo(a, b):
    """
    Вычисляет остаток от деления a на b.

    Args:
        a (int or float): Делимое.
        b (int or float): Делитель.

    Returns:
        int or float: Остаток от деления, если деление возможно.
        str: Сообщение об ошибке, если делитель равен нулю.
    """
    if b == 0:
        return "Ошибка: Деление на ноль невозможно."
    return a % b



