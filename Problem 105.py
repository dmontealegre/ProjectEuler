import itertools

file = open('p105.txt', 'r')


def is_good(array):
    answer = True
    t1 = len(array)
    for i in range(1, t1+1):
        # pick a set B with i elements.
        for B in itertools.combinations(array,i):
            # now pick a set C disjoint from B:
            B = set(B)
            complement = set(array) - B
            t2 = t1 - i
            for j in range(1,t2+1):
                for C in itertools.combinations(complement, j):
                    if sum(C) == sum(B):
                        return False
                    if len(C) > len(B) and sum(C) <= sum(B):
                        return False
    return answer

answer = 0
for line in file.readlines():
    array = line.split(',')
    array = [int(i) for i in array]
    if is_good(array):
        answer += sum(array)
        print(array)

print(answer)