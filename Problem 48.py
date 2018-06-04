import math
sum = 0


def power_truncated(i):
    power = 1
    for j in range(i):
        power *= i
        while power > math.pow(10,10):
            power -= math.pow(10,10)
    return power

for i in range(1, 1001):
    print(i)
    sum += power_truncated(i)
    while sum > math.pow(10,10):
        sum -= math.pow(10,10)

print(sum)

