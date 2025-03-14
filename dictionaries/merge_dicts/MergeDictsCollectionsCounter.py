# - Функция должна принимать два аргумента: словари **`dict1`** и **`dict2`**.
# - Если ключ присутствует в обоих словарях, сложите их значения.
# - Верните объединённый словарь.
# заюзать collections.Counter

from collections import Counter


def merge_dicts(dict1, dict2):
    return dict(Counter(dict1) + Counter(dict2))

dict_1 = {"a": 1, "b": -2}
dict_2 = {"b": 3, "c": 4}

print(merge_dicts(dict_1, dict_2))
