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