# Напишите функцию **`extract_subdict(my_dict, keys)`**, которая принимает словарь и список ключей.
# Функция должна вернуть новый словарь, включающий только те пары, ключи которых содержатся в списке.
# - Функция должна принимать два аргумента: словарь **`my_dict`** и список ключей **`keys`**.
# - Верните новый словарь.

from utils_package import MyDictUtils


def extract_subdict(my_dict, keys):
    new_dict = {}
    for key in keys:
        if key in my_dict:
            new_dict[key] = my_dict[key]

    return new_dict

user_input = MyDictUtils.user_input()
key_s = input("Введите желаемые ключи через запятую: ")
print(extract_subdict(user_input, key_s))
