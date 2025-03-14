def is_anagram(s1, s2):
    list_1 = list(s1)
    list_2 = list(s2)

    list_1.sort()
    list_2.sort()

    position = 0
    matches = True

    while position < len(s1) and matches:
        if list_1[position] == list_2[position]:
            position += 1
        else:
            matches = False
    return matches

user_input_1 = input("Введите строку1: ").casefold()
user_input_2 = input("Введите строку2: ").casefold()
anagram = is_anagram(user_input_1, user_input_2)
print(anagram)
