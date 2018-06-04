import math


def divisor_sum(n):
    answer = [1]
    for m in range(2, int(math.sqrt(n) + 1)):
        if n % m == 0:
            answer.append(m)
            if m != n // m:
                answer.append(n // m)
    return sum(answer)

dictionary = {}

for x in range(10001):
    dictionary[x] = divisor_sum(x)


answer = 0

for x in dictionary.keys():
    try:
        if dictionary[dictionary[x]] == x and dictionary[x] != x:
            answer += x
    except KeyError:
        continue

print(answer)
