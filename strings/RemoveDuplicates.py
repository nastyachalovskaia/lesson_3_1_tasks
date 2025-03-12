# Напишите функцию **`remove_duplicates(s)`**,
# которая принимает строку и возвращает новую строку, из которой удалены все повторяющиеся символы,
# оставляя только первое вхождение каждого символа.
# **Требования:**
# - Функция должна принимать один аргумент: строку **`s`**.
# - Верните строку без повторяющихся символов.

def remove_duplicate(s):
    result = []
    seen = set()

    for char in s:
        if char not in seen:
            result.append(char)
            seen.add(char)

    return ''.join(result)

user_input = input("Введите строку: ")
unique = remove_duplicate(user_input)
print(unique)
