max_number = 0
while number > 0:
    max_number += number % 10
    number //= 10

for i in range(n - 1):
    name = input()
    number = int(input())
    x = 0
    while number > 0:
        x += number % 10
        number //= 10
    if x >= max_number:
        max_number = x
        max_name = name

print(max_name)
