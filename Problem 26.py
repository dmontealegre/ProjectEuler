import math
import time


def is_here(trailing, expansion):
    # receives a trailing expasion of length t and checks if we have seen it before
    t = len(trailing)
    #print(len(expansion))
    for x in range(len(expansion)-t-1,0,-1):
        if trailing == expansion[x:x+t]:
            return True, len(expansion) - x - t
    return False, None


def division(d):
    t = math.ceil(math.log(d, 10))
    expansion = [0]
    numerator = 1
    while True:
        #print(expansion)
        numerator *= 10
        expansion.append(numerator // d)
        numerator = numerator % d
        # we check the conditions on when to stop:
        trailing = expansion[-t:]
        if numerator == 0:
            return 0
        check = is_here(trailing, expansion)
        if check[0]:
            return check[1]
            break

start = time.time()
best = 0
longest = 0
for d in range(3, 1001, 2):
    temp = division(d)
    if temp > longest:
        best = d
        longest = temp

print(best)
print(time.time()-start)





