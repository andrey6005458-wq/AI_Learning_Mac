# Скрипт с сортировкой выбором

user_input = input("Введите числа через пробел: ")

try:
    numbers = [float(num) for num in user_input.split()]

    # Сортировка выбором
    n = len(numbers)

    for i in range(n):
        # Находим индекс минимального элемента в неотсортированной части
        min_idx = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_idx]:
                min_idx = j

        # Меняем местами текущий элемент с найденным минимальным
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    print("Отсортированные числа:", numbers)

except ValueError:
    print("Ошибка: Пожалуйста, введите только числа, разделенные пробелами.")
