import math
bound = 100

def f(l, N):
    a = [1] + [0] * N
    for i in l:
        for j in range(N - i + 1):
            a[i + j] += a[j]

    return a

array = [i for i in range(1,bound)]

print(f(array, bound)[100])
