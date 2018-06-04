# ugly but works fast :/
import itertools

bound = 10000

tri = lambda n: n * (n + 1) // 2
sqr = lambda n: n ** 2
pen = lambda n: n * (3 * n - 1) // 2
hex = lambda n: n * (2 * n - 1)
hep = lambda n: n * (5 * n - 3) // 2
oct = lambda n: n * (3 * n - 2)


def create_sets(function):
    answer = []
    i = 1
    while True:
        if function(i) < bound:
            if function(i) > 1000:
                answer.append(function(i))
        else:
            break
        i += 1
    return answer


numbers = {
    3: create_sets(tri),
    4: create_sets(sqr),
    5: create_sets(pen),
    6: create_sets(hex),
    7: create_sets(hep),
    8: create_sets(oct)
 }

def get_candidates(num, pool):
    return [i for i in pool if i // 100 == num]

for permutation in itertools.permutations([3, 4, 5, 6, 7, 8]):
    for num0 in numbers[permutation[0]]:
        candidates1 = get_candidates(num0 - (num0//100)*100, numbers[permutation[1]])
        for num1 in candidates1:
                candidates2 = get_candidates(num1 - (num1//100) * 100, numbers[permutation[2]])
                for num2 in candidates2:
                        candidates3 = get_candidates(num2 - (num2 // 100) * 100, numbers[permutation[3]])
                        for num3 in candidates3:
                                candidates4 = get_candidates(num3 - (num3 // 100) * 100, numbers[permutation[4]])
                                for num4 in candidates4:
                                        candidates5 = get_candidates(num4 - (num4 // 100) * 100, numbers[permutation[5]])
                                        # we check that it loops around
                                        for num5 in candidates5:
                                                if num5 - (num5//100)*100 == num0//100:
                                                    print(num0,num1,num2,num3,num4,num5, ' and their sum is', num0+num1+num2+num3+num4+num5)