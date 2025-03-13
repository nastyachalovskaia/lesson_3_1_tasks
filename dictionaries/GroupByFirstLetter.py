# Напишите функцию **`group_by_first_letter(strings)`**,
# которая принимает список строк и группирует их в словарь, где ключами являются первые символы строк,
# а значением — список строк, начинающихся с этого символа.
# - Функция должна принимать один аргумент: список строк **`strings`**.
# - Верните словарь с группировкой.

def group_by_first_letter(strings):
    groups = {}
    for s in strings:
        first_letter = s[0].casefold()

        if first_letter not in groups:
            groups[first_letter] = []
        groups[first_letter].append(s)
    return groups

user_input = input("Введите список строк: ").split()
result = group_by_first_letter(user_input)
print(result)