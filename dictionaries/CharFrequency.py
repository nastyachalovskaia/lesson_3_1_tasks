# Напишите функцию char_frequency(s), которая создаёт словарь,
# где ключами являются символы строки, а значениями — количество раз, когда каждый символ встречается в строке.

def char_frequency(s):
    result = {}

    for char in s:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    return result

user_input = input("Введите слово: ")
res = char_frequency(user_input)

print(res)
