n = int(input())
sum_digits = 0

for i in range(n):
    x = int(input())
    while x > 0:
        sum_digits += x % 10
        x //= 10
print(sum_digits)
