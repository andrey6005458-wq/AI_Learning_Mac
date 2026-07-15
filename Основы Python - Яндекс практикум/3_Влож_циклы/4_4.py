n = int(input())
sum_digits = 0

for i in range(n):
    x = int(input())
    while x > 0:
        sum_digits += x % 10
        x //= 10
print(sum_digits)

a = 8 + 5 + 7 + 3 + 3 + 9 + 3 + 1 + 1 + 3 + 9 + 2 + 3

print(a)
