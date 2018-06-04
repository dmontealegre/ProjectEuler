def area(n, k):
    return (k*(k+1)//2) * (n * (n+1) // 2)


error = 1000000000000000000000000000000000000
best_pair = [0, 0]
for n in range(1, 2002):
    for k in range(1, 2002):
        if error > abs(area(n, k) - 2000000):
            best_pair[0] = n
            best_pair[1] = k
            error = abs(area(n, k) - 2000000)
print(best_pair)