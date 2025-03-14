# - Функция должна принимать один аргумент: строку **`s`**.
# - Верните **`True`**, если все символы уникальны, иначе — **`False`**.

def is_unique(s):
    set_s = set(s)
    return len(s) == len(set_s)

user_input = input("Введите строку: ").replace(" ", "")
unique = is_unique(user_input)
print(unique)
