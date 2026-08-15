def get_type_of_sentence(sentence: str) -> str:
    return "question" if sentence.endswith("?") else "normal"

print(get_type_of_sentence("Hello!"))
print(get_type_of_sentence("How are you?"))

