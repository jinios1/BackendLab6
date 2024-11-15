from module1 import func_a1, func_a2, func_a3
import random
import math
import locale
from decimal import Decimal
from dataclasses import dataclass

# Шаг 4: Использование модуля random
def random_example_1():
    """Шаг 4: Функция, использующая random для выбора случайного числа."""
    return random.randint(1, 100)

def random_example_2():
    """Шаг 4: Функция, использующая random для перемешивания списка."""
    lst = [1, 2, 3, 4, 5]
    random.shuffle(lst)
    return lst

# Шаг 5: Использование модуля math
def math_example_1(x):
    """Шаг 5: Функция, которая возвращает квадратный корень числа."""
    return math.sqrt(x)

def math_example_2(x):
    """Шаг 5: Функция, которая возвращает косинус числа."""
    return math.cos(x)

def math_example_3(x):
    """Шаг 5: Функция, которая округляет число вверх."""
    return math.ceil(x)

# Шаг 6: Использование модуля locale
def locale_example_1():
    """Шаг 6: Функция, которая форматирует число в локальном формате."""
    locale.setlocale(locale.LC_ALL, '')
    return locale.format_string("%d", 1234567890, grouping=True)

def locale_example_2():
    """Шаг 6: Функция, которая форматирует число с плавающей точкой."""
    locale.setlocale(locale.LC_ALL, '')
    return locale.format_string("%.2f", 12345.6789, grouping=True)

def locale_example_3():
    """Шаг 6: Функция, которая устанавливает новую локаль."""
    locale.setlocale(locale.LC_TIME, 'en_US')
    return locale.getlocale(locale.LC_TIME)

# Шаг 7: Использование модуля decimal
def decimal_example_1():
    """Шаг 7: Функция, демонстрирующая работу с Decimal."""
    return Decimal('0.1') + Decimal('0.2')

def decimal_example_2():
    """Шаг 7: Функция, которая умножает числа с Decimal."""
    return Decimal('2.5') * Decimal('3.0')

# Шаг 8: Создание data-классов
@dataclass
class DataClass1:
    value: int

@dataclass
class DataClass2:
    text: str
    number: float

@dataclass
class DataClass3:
    is_active: bool
    items: list

# Шаг 9: Работа с data-классами
def data_class_example_1(obj):
    """Шаг 9.1: Передача объекта data-класса как параметра."""
    return obj.value + 1

def data_class_example_2(obj_list):
    """Шаг 9.2: Работа со списком объектов data-классов."""
    return [obj.value * 2 for obj in obj_list]

def data_class_example_3(data_dict):
    """Шаг 9.3: Работа со словарём, где значения - объекты data-классов."""
    return {k: v.text.upper() for k, v in data_dict.items()}

def data_class_example_4(obj):
    """Шаг 9.4: Модификация значений объекта data-класса."""
    obj.value += 10
    return obj

def data_class_example_5(value, text, is_active):
    """Шаг 9.5: Создание объекта data-класса из параметров."""
    return DataClass1(value=value), DataClass2(text=text, number=1.0), DataClass3(is_active=is_active, items=[])

def call_all_functions():
    """Шаг 10: Вызов всех функций из шагов 2-9."""
    print(func_a1(10))
    print(func_a2([1, 2, 3]))
    print(func_a3(10, 5))

    print(random_example_1())
    print(random_example_2())

    print(math_example_1(16))
    print(math_example_2(1.57))
    print(math_example_3(2.1))

    print(locale_example_1())
    print(locale_example_2())
    print(locale_example_3())

    print(decimal_example_1())
    print(decimal_example_2())

    obj = DataClass1(5)
    print(data_class_example_1(obj))
    obj_list = [DataClass1(i) for i in range(5)]
    print(data_class_example_2(obj_list))
    data_dict = {"a": DataClass2("example", 3.5)}
    print(data_class_example_3(data_dict))
    print(data_class_example_4(obj))
    print(data_class_example_5(10, "Hello", True))

if __name__ == "__main__":
    call_all_functions()
