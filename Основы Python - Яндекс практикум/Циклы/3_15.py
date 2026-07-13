n = int(input())
animal = 0

for i in range(n):
    text = input()
    if "зайка" in text:
        animal += 1
print(animal)
