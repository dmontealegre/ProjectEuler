# not super fast, but it did the trick 

import math


bound = 10**6

def divisor_sum(n):
    answer = [1]
    for m in range(2, int(math.sqrt(n) + 1)):
        if n % m == 0:
            answer.append(m)
            if m != n // m:
                answer.append(n // m)
    return sum(answer)


dictionary = {}
longest = 0


for x in range(bound):
    seen = []
    current = x
    while True:
        try:
            new = dictionary[current]
        except KeyError:
            dictionary[current] = divisor_sum(current)
        new = dictionary[current]
        if new > bound:
            break
        if new not in seen:
            seen.append(new)
            current = new
        else:
            break
        if seen[-1] == x:
            if len(seen)>longest:
                print('Best so far starts at ', x)
                print(seen)
                longest = len(seen)

print('done')