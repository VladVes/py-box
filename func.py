# 26. Как определяется функция в Python? 
# Создать простую функцию calc_average получающую два int числа a, b
# и возвращает среднее арифметическое.
# Какое есть специальное значение которое вернёт функция в случае осутствия
# return или если в return нет значения?

def calc_average (a, b: int) -> float:
    sum = a + b
    result = sum / 2
    return result

# None