k = int(input())
min_name = input()
for i in range(k - 1):
    min_name = min(min_name, input())

print(min_name)

name = input("Как Вас зовут?\n")
print(f"Привет, {name}")
