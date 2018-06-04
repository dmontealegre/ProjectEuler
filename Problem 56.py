# not working. integers are too large

import math

def digital_sum(n):
    string = str(n)
    summation = 0
    for char in string:
        summation += int(char)
    return summation

maximum = 0

def power(a, b):
    power = a
    for _ in range(b):
        power *= a
    return power

for a in range(100):
    for b in range(100):
        maximum = max(digital_sum(power(a, b)), maximum)

print(maximum)

