# Скрипт с максимальным числом

numbers = []
while n := input("Введите число (пустая строка для выхода): "):
    numbers.append(int(n))

if numbers:
    print(f"Максимальное число: {max(numbers)}")
else:
    print("Числа не введены")
