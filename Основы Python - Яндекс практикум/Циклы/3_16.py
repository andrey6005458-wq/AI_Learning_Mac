animal = 0

while True:
    text = input()
    if text == "Приехали!":
        break
    if "зайка" in text:
        animal += 1
print(animal)
