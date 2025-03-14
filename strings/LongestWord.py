import re


def longest_word(s):
    s = s.strip()
    if not s:
        return "Введите не пустую строку"
    words = re.findall(r'\b\w+\b', s)
    return max(words, key=len)

punctuation_pattern = r'[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]'

user_input = input("Введите строку: ")
cleaned_input = re.sub(punctuation_pattern, "", user_input)
longest_word_in_user_str = longest_word(cleaned_input)

print(longest_word_in_user_str)
