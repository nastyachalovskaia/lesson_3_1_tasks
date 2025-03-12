def longest_word(s):
    return max(s, key=len)

user_input = input("Введите строку: ").split()
longest_word_in_user_str = longest_word(user_input)
print(longest_word_in_user_str)
