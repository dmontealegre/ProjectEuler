# Problem 5

import math
limit = 20

pointer = 1
answer = 1
while pointer <= limit:
    answer = (pointer * answer) // math.gcd(pointer, answer)
    pointer += 1


print("The smallest positive number that is evenly divisible by all of the numbers from 1 to %s is" % limit, answer)