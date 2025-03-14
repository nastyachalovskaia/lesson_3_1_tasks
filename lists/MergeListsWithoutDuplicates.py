# Напишите функцию **`merge_lists(list1, list2)`**, которая объединяет два списка, удаляя дубликаты.
# - Функция должна принимать два аргумента: списки **`list1`** и **`list2`**.
# - Используйте множество (**`set`**) для удаления дубликатов.
# - Верните объединённый список.

def merge_lists(list1, list2):
    list1 = list(list1)
    list2 = list(list2)
    new_list = list1.copy()
    new_list.extend(list2)
    res = list(set(new_list))
    return res

user_input = input("Введите строку 1: ")
user_input_2 = input("Введите строку 2: ")
unique_print = merge_lists(user_input, user_input_2)

print(unique_print)
