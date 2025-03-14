# Напишите функцию char_frequency(s), которая создаёт словарь,
# где ключами являются символы строки, а значениями — количество раз, когда каждый символ встречается в строке.
# заюзать collections.Counter

from collections import Counter


def char_frequency(s):
    return dict(Counter(s))

user_input = input("Введите строку/слово: ")
res = char_frequency(user_input)

print(res)
