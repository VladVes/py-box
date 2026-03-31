# 37. конструкция основного условного оператора
x = 10
if x > 10:
    print('if works!')
elif x == 10:
    print('elif works')
else:
    print('else')

# 38. Как устроен тернарный оператор в Python? 
# Написать пример функции get_type_of_sentence которая возвращает тип предложения
# (question или normal) в зависимости от знака на которое оно заканчивается 

def get_type_of_sentence(sent: str) -> str:
    return 'question' if sent.strip().endswith('?') else 'normal'

# 39. Чем по сути является match в Python?
# Набрать пример конструкции в функции get_status
# которая получает значение в виде кода 100 - new, 200 - processing, 300 - paid
# печатает и возвращает их текстовые значенияю.
# Если код не совпадает то пишет Error

def get_status(code: int) -> str:
    match code:
        case 100:
            return 'NEW'
        case 200:
            return 'PROCESSING'
        case 300:
            return 'PAID'
        case _:
            return 'ERROR'

print(get_status(100))
print(get_status(200))
print(get_status(300))
print(get_status(0))