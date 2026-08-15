"""
Сгенерированные примеры использования конструкции match (структурное сопоставление) в Python 3.10+
"""

def example1(value):
    """Сопоставление с литералами"""
    match value:
        case "start":
            return "Начало работы"
        case "stop":
            return "Остановка"
        case "pause":
            return "Пауза"
        case _:
            return f"Неизвестная команда: {value}"

def example2(data):
    """Сопоставление с последовательностями (list, tuple)"""
    match data:
        case [x, y]:
            return f"Два элемента: {x}, {y}"
        case [x, y, z]:
            return f"Три элемента: {x}, {y}, {z}"
        case []:
            return "Пустой список"
        case _:
            return "Другая структура"

def example3(point):
    """Сопоставление с классами и извлечение атрибутов"""
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    match point:
        case Point(x=0, y=0):
            return "Точка в начале координат"
        case Point(x, y) if x == y:
            return f"Точка на диагонали: ({x}, {y})"
        case Point(x, y):
            return f"Точка: ({x}, {y})"
        case _:
            return "Не точка"

def example4(command):
    """Сопоставление с guard условиями (if)"""
    match command:
        case ("move", direction, distance) if distance > 0:
            return f"Движение {direction} на {distance} единиц"
        case ("move", direction, distance) if distance <= 0:
            return f"Некорректное расстояние: {distance}"
        case ("jump", height):
            return f"Прыжок на высоту {height}"
        case _:
            return "Неизвестная команда"

def example5(value):
    """Сопоставление с OR шаблоном (|)"""
    match value:
        case 1 | 2 | 3:
            return "Маленькое число"
        case 4 | 5 | 6:
            return "Среднее число"
        case 7 | 8 | 9:
            return "Большое число"
        case _:
            return "Число вне диапазона 1-9"

def example6(data):
    """Сопоставление с вложенными структурами"""
    match data:
        case {"type": "user", "name": str(name), "age": int(age)}:
            return f"Пользователь {name}, возраст {age}"
        case {"type": "product", "id": int(id), "price": float(price)}:
            return f"Товар #{id}, цена {price}"
        case _:
            return "Неизвестный объект"

def main():
    print("=== Примеры конструкции match ===")
    
    # Пример 1
    print("\n1. Сопоставление с литералами:")
    for cmd in ["start", "stop", "pause", "unknown"]:
        print(f"   {cmd!r} -> {example1(cmd)}")
    
    # Пример 2
    print("\n2. Сопоставление с последовательностями:")
    for seq in [[1, 2], [3, 4, 5], [], [1]]:
        print(f"   {seq} -> {example2(seq)}")
    
    # Пример 3
    print("\n3. Сопоставление с классами:")
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def __repr__(self):
            return f"Point({self.x}, {self.y})"
    
    points = [Point(0, 0), Point(5, 5), Point(2, 3)]
    for pt in points:
        print(f"   {pt} -> {example3(pt)}")
    
    # Пример 4
    print("\n4. Сопоставление с guard условиями:")
    commands = [("move", "north", 10), ("move", "south", -5), ("jump", 3), ("run", 5)]
    for cmd in commands:
        print(f"   {cmd} -> {example4(cmd)}")
    
    # Пример 5
    print("\n5. Сопоставление с OR шаблоном:")
    for num in [2, 5, 8, 11]:
        print(f"   {num} -> {example5(num)}")
    
    # Пример 6
    print("\n6. Сопоставление с вложенными структурами:")
    objects = [
        {"type": "user", "name": "Анна", "age": 30},
        {"type": "product", "id": 123, "price": 99.99},
        {"type": "unknown", "data": "test"}
    ]
    for obj in objects:
        print(f"   {obj} -> {example6(obj)}")
    
    print("\n=== Дополнительные примеры ===")
    
    # Пример с match и переменными
    print("\n7. Извлечение значений в переменные:")
    data = ("error", 404, "Not Found")
    match data:
        case ("success", code, message):
            print(f"   Успех: {code} - {message}")
        case ("error", code, message):
            print(f"   Ошибка: {code} - {message}")
        case _:
            print("   Неизвестный статус")
    
    # Пример с match для типов
    print("\n8. Сопоставление по типу:")
    items = [42, "hello", 3.14, [1, 2, 3]]
    for item in items:
        match item:
            case int():
                print(f"   {item!r} - целое число")
            case str():
                print(f"   {item!r} - строка")
            case float():
                print(f"   {item!r} - число с плавающей точкой")
            case list():
                print(f"   {item!r} - список")
            case _:
                print(f"   {item!r} - другой тип")

if __name__ == "__main__":
    main()