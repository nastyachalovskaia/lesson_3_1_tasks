# Напишите функцию format_phone_number(digits),
# которая принимает строку из 10 цифр и возвращает её в формате (XXX) XXX-XXXX.

def format_phone_number(digits):

    formatted_phone = f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"
    return formatted_phone

def check_input():
    while True:
        phone = input("Введите номер телефона из 10 цифр: ")
        if len(phone) == 10 and phone.isdigit():
            return phone
        else:
            print("Введите 10 цифр")

user_phone = check_input()
result = format_phone_number(user_phone)
print(result)
