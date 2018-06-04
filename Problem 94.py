from decimal import *
import math

getcontext().prec = 30
def area(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    s = Decimal((a+b+c)/2)
    num = s*(s-a)*(s-b)*(s-c)
    return num.sqrt()

is_int = lambda x: x - math.floor(x) == 0
lenghts = []
for x in range(2, 1000000000//3):
    if x % 3 == 0:
        continue
    if x % 2 == 0:
        continue
    case1 = [x,x,x-1]
    case2 = [x,x,x+1]
    if is_int(area(case1)):
        print(case1)
        lenghts + case1
        x *= 3
    if is_int(area(case2)):
        print(case2)
        lenghts + case2
        x *= 3

print(sum(lenghts))

# better idea: Go throught the squares