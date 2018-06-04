# TODO make faster by only computing the numbers needed. 

import math

chain = {}

for x in range(2200000):
    number = str(x)
    temp = 0
    for char in number:
        temp += math.factorial(int(char))
    chain[x] = temp


length = {}
count = 0
for x in range(1000000):
    ans = x
    seen = []
    current = x
    while True:
        current = chain[x]
        if current not in seen:
            seen.append(current)
            x = current
        else:
            break
    length[ans] = len(seen)+1
    if len(seen) + 1 == 60:
        count += 1

print(count)


