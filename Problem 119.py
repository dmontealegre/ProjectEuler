import math

def digit_sum(n):
    string = str(n)
    summation = 0
    for char in string:
        summation += int(char)
    return summation

a = []

n = 11

while True:
    print(a)
    if digit_sum(n) > 1:
        if math.log(n, digit_sum(n)) == int(math.log(n, digit_sum(n))):
            a.append(n)
    if len(a) > 9:
        break
    n += 1

