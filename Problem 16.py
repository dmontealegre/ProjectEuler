import math

x = int(math.pow(2, 1000))

def digit_sum(n):
    s = str(n)
    sum = 0
    for t in s:
        sum += int(t)
    return sum

y = int(math.factorial(100))

print(digit_sum(y))