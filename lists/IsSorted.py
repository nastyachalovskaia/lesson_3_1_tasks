def is_sorted(lst):
    s = lst[0]
    for l in lst[1:]:
        if l <= s:
            return False
        s = l
    return True

user_input = input("Введите числа: ")
items = [item.strip() for item in user_input.split(",")]
result = is_sorted(items)
print(result)
