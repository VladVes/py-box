# Как работают аннотации типов?
# Определить функцию test принимающую строку и целочисленное число и возварщающую bool.
# Как указать что фукнция ничего не возвращает?

def test1(s: str, i: int) -> bool:
    print(f'string: {s}, number int: {i}')
    return True

def test2(flag: bool) -> None:
    print(f'Is it work\'s witho no return? {flag}')