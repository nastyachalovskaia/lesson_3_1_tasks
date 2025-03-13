def remove_duplicates(lst):
    result = []
    seen = set()

    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result

user_input = input("Введите строку: ")
items = [item.strip() for item in user_input.split(",")]
unique_print = remove_duplicates(items)
print(unique_print)
