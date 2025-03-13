def generate_squares(n):
    numbers = [x ** 2 for x in range(1, n + 1)]
    return numbers

user_numbers = int(input("Введите число: "))
result = generate_squares(user_numbers)
print(result)
