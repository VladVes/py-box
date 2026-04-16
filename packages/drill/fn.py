from .const import VOWELS

def count_vowels(word: str) -> int:
    counter = 0
    for char in word:
        if char.lower() in VOWELS:
           counter += 1 
    return counter