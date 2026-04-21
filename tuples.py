rgb_color = (255, 127, 64)
name_and_age = ("John", 88)
three_bool = (True, False, True)
pairs = ((1, 2), (3, 4))
one_elemet_tuple = (1,)
additional_syntax = 1, 2, 3 # no brackets
print(rgb_color)
print(len(rgb_color)) # has len

# 48. Создать фукнцию которая может возвращать сразу несколько значений с помощью
# (специальной струтуры данных) div_mod - возвращает два значения одновременно:
# результат деления нацело и остаток от деления.
# Как из результата получить отдельно значение деления и остатка?

def div_mod(a: int, b: int) -> tuple:
    result1 = a // b
    result2 = a % b
    return result1, result2

div_mod_res = div_mod(10, 3)
print(div_mod_res)
print(div_mod_res[0])
print(div_mod_res[1])
a, b = div_mod_res
print(a)
print(b)

