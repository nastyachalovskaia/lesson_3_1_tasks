# - Функция должна принимать два аргумента: словари **`dict1`** и **`dict2`**.
# - Если ключ присутствует в обоих словарях, сложите их значения.
# - Верните объединённый словарь.

def merge_dicts(dict1, dict2):
    result = {}

    for key in dict1:
        if key in dict2:
            result[key] = dict1[key] + dict2[key]
        else:
            result[key] = dict1[key]
    for key in dict2:
        if key not in dict1:
            result[key] = dict2[key]

    return result

dict_1 = {"a": 1, "b": 2}
dict_2 = {"b": 3, "c": 4}

print(merge_dicts(dict_1, dict_2))
