import math

number = 3/7
best = 0

for x in range(8,1000001):
    if x % 7 != 0 :
        if best < math.floor(number * x) / x:
            print(math.floor(number * x), '/', x)
            best = math.floor(number * x) / x