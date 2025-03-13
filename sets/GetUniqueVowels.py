# Создайте функцию **`get_unique_vowels(s)`**, которая принимает строку и возвращает набор уникальных гласных,
# содержащихся в строке (игнорируя регистр).
# - Функция должна принимать один аргумент: строку **`s`**.
# - Гласные буквы: **`a, e, i, o, u`**.
# - Игнорируйте регистр символов.
# - Верните множество уникальных гласных.

def get_unique_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    total = set()
    for char in s.lower():
        if char in vowels:
            total.add(char)
    return total

user_input_str = input("Введите строку: ")
print(get_unique_vowels(user_input_str))
