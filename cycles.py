# 40. Как выглядит простейшая конструкция с while?
# Сделать пример где count_chars принимает строку и символ и
# подсчитывает количество этого символа в строке, возвращает целое значение 

def count_chars(s: str, c: str) -> int:
    i = 0
    result = 0
    while i < len(s):
        if s[i] == c:
            result += 1
        i += 1
    return result 

print(count_chars('hello', 'l'))

# 42. Как в Python выглядит базовая конструкция цикла без условия остановки?
# Какой это цикл? Сделать с его помощью переворот строки

def str_reverse(string: str) -> str:
    result = ''
    for char in string:
        result = char + result
    
    return result

print(str_reverse("hello"))

# 43. Как можно перебрать последовательность чисел от 1 до 10 в цикле for без счётчика?
# Сделать пример суммирования всех чисел до x = 10 т.е. из ряда от 0 до 10.
# Как можно ограничить цикл так, что бы перебирался не весь ряд а толко до 5?
# Как можно сложить все числа ряда до 5 но только каждое второе число ряда?

def serial_sum():
    x = 10
    result1 = 0
    for i in range(x):
        result1 += i
    print(f'result for range(10): {result1}')

    result2 = 0
    for i in range(1, 5):
        result2 += i
    print(f'result for range(1, 5): {result2}')

    result3 = 0
    for i in range(1, 5, 2):
        result3 += i
    print(f'result for range(1, 5, 2): {result3}')

    for i in range(5, 0, -1):
        print(i)
        
    
serial_sum()

# 43.1 Реализуйте функцию fizzbuzz(n), которая возвращает строку с числами от 1 до n.
# При этом: если число делится на 3, вместо него подставляется слово "Fizz",
# если число делится на 5 — слово "Buzz", если делится и на 3, и на 5 — слово "FizzBuzz". 
# Все элементы должны соединяться пробелом.

def fizzbuzz(n: int) -> str:
    result = ""
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            result += 'FizzBuzz'
        elif i % 3 == 0:
            result += 'Fizz'
        elif i % 5 == 0:
            result += 'Buzz'
        else:
            result += str(i)
        if i < n:
            result += ' '
    return result

print(fizzbuzz(16))
        
