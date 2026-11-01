VOWELS = set("аеєиіїоуюяaeiou")


def count_symbols(text: str) -> int:
    return len(text)


def count_vowels(text: str) -> int:
    return sum(1 for symbol in text.lower() if symbol in VOWELS)


def divide(a, b):
    return a / b
