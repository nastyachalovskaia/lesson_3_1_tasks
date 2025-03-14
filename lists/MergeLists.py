# Напишите функцию **`merge_lists(list1, list2)`**,
# которая принимает два списка одинаковой длины и возвращает новый список,
# где элементы получены путём сложения соответствующих элементов из обоих списков.
# - Функция должна принимать два аргумента: списки **`list1`** и **`list2`**.
# - Используйте генератор списков для создания нового списка.
# - Верните список с результатами сложения.

def merge_lists(list1, list2):
    is_length_equal = len(list1) == len(list2)
    if is_length_equal:
        return [x + y for x, y in zip(list1, list2)]
    else:
        return "Попробуйте снова ввести два списка одной длины"

user_input = input("Введите первый список чисел через запятую: ")
user_input_2 = input("Введите второй список чисел через запятую: ")

items_1 = [int(x.strip()) for x in user_input.split(",")]
items_2 = [int(x.strip()) for x in user_input_2.split(",")]

result = merge_lists(items_1, items_2)
print(result)
