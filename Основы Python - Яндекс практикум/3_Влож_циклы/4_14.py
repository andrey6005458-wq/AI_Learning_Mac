h = int(input())
m = int(input())

for i in range(h):
    for j in range(m):
        number = i + j * h + 1
        if j == 0:
            print(number, end="")
        else:
            print("", number, end="")
    print()
