import math
bound = int(math.pow(10,5))

def f(l, N):
    a = [1] + [0] * N
    for i in l:
        for j in range(N - i + 1):
            a[i + j] += a[j]

    return a

array = [i for i in range(1,bound)]

print(f(array, bound ))

for i in range(len(array)):
    if array[i] % 1000000 == 0:
        print(i)