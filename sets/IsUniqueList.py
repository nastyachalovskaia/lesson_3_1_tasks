# Напишите функцию **`is_unique_list(lst)`**, которая принимает список и возвращает **`True`**,
# если все элементы списка уникальны, и **`False`**, если есть повторения.

def is_unique_list(lst):
    return len(lst) == len(set(lst))

usr_input = input("Введите список чисел или строк: ").replace(",", "").split()
res = is_unique_list(usr_input)
print(res)