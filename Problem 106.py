import itertools


n = 12
pool = [i for i in range(1, n+1)]

def dominates(A,B):
    answer = True
    for i in range(len(A)):
        if A[i] < B[i]:
            answer = answer and False
    return answer



def is_good(array):
    answer = 0
    t1 = len(array)
    for i in range(2, t1):
        for B in itertools.combinations(array,i):
            B = set(B)
            complement = set(array) - B
            for C in itertools.combinations(complement, i):
                B = list(B)
                C = list(C)
                if not dominates(C,B) and B[0]<C[0]:
                    answer += 1
                    print(B,C)
    return answer



def count(array):
    count = 0
    test = []
    answer = True
    trivial = 0
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
                    count += 1
                    if len(C) != len(B):
                        trivial += 1
                        B = list(B)
                        C = list(C)
                    else:
                        B = list(B)
                        C = list(C)
                        B.sort()
                        C.sort()
                        if dominates(B,C) or dominates(C,B):
                            trivial += 1
                            print(B,C)
    print(trivial/2)
    print(count/2)
    print(count/2 - trivial / 2)
    return answer

print(count(pool))
