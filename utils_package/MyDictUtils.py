def user_input():
    n = int(input("Введите количество пар ключ-значение: "))
    my_dict = {}

    for _ in range(n):
        key = input("Введите ключ: ")
        value = input("Введите значение: ")
        my_dict[key] = value

    return my_dict
