# 22. Можно ли строки привести к bool
s = 'some string'
b = bool(s)
print(b)

# 23. какие примитивныйе типы есть в Python:
print('TYPES: int, str, bool, float')

# 24. Как работают аннотации типов?
# Определить функцию test принимающую строку и целочисленное число и возварщающую bool.
# Как указать что фукнция ничего не возвращает?

def test1(s: str, i: int) -> bool:
    print(f'string: {s}, number int: {i}')
    return True

def test2(flag: bool) -> None:
    print(f'Is it work\'s witho no return? {flag}')
test1('snake', 5)
test2(True)