# Напишите функцию **`dict_to_lists(my_dict)`**, которая принимает словарь и возвращает два списка:
# один с ключами и другой с соответствующими значениями.
# - Функция должна принимать один аргумент: словарь **`my_dict`**.
# - Используйте методы **`.keys()`** и **`.values()`** для извлечения ключей и значений.
# - Верните кортеж, содержащий два списка: список ключей и список значений.

from utils_package import MyDictUtils


def dict_to_lists(my_dict):
    list_of_keys = list(my_dict.keys())
    list_of_values = list(my_dict.values())

    result = (list_of_keys, list_of_values)

    return result

user_input = MyDictUtils.user_input()

res = dict_to_lists(user_input())
print(res)
