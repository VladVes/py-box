print('Drill!')

def str_reverse(string: str) -> str:
    result = ''
    for ch in string:
        result = ch + result
    return result

print(str_reverse('super'))