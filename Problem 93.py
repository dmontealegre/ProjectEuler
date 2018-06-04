import itertools
import math
all_digits = [1,2,3,4,5,6,7,8,9]
Operations = [1,2,3,4]


def po(num1, num2, label):
    if label == 1:
        return num1 + num2
    if label == 2:
        return num1 - num2
    if label == 3:
        return num1 * num2
    if label == 4:
        return num1 / num2


def longest(array):
    if array[0] != 1:
        return 0
    else:
        pointer = 1
        while True:
            if pointer + 1 == array[pointer]:
                pointer += 1
            else:
                break
        return pointer


best = 0
for digits in itertools.combinations(all_digits, 4):
    results = []
    for subset in itertools.permutations(digits):
        for operations in itertools.product(Operations, repeat=3):
            try:
                results.append(po(po(po(subset[0],subset[1], operations[0]), subset[2], operations[1]), subset[3], operations[2]))
                results.append(po(po(subset[0], subset[1], operations[0]), po(subset[2],subset[3],operations[1]), operations[2]))
            except ZeroDivisionError:
                continue
    results = [int(i) for i in results if i > 0 and math.floor(i) == i]
    results = list(set(results))
    results.sort()
    temp = longest(results)
    if temp > best:
        print('Best so far is ', digits)
        best = temp



print('done')