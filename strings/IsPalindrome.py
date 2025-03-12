def is_palindrome(s):
    text = ''.join(char for char in s if char.isalnum())
    text = text.casefold()
    return True if text == text[::-1] else False

user_input = input("Введите строку: ")
palindrome = is_palindrome(user_input)
print(palindrome)
