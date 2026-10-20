VOWELS = "aeiouy"
def count_vowels(word: str) -> int:
    counter = 0
    for ch in word:
        if ch in VOWELS:
            counter += 1
    return counter
            

print(count_vowels("Hello"))