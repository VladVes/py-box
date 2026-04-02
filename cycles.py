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