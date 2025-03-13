# Напишите функцию get_unique_elements(lst),
# которая принимает список чисел или строк и возвращает новый список,
# содержащий только уникальные элементы из исходного списка.

def get_unique_elements(lst):
    new_list = sorted(set(lst))
    return new_list

usr_input = input("Введите список чисел или строк: ").replace(",", "").split()
res = get_unique_elements(usr_input)
print(res)
