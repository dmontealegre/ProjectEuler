# we solve the problem with recursion
# a[i] will be the number of ways to decompose length i
a = [0, 1, 2, 4, 8]

while len(a) < 51:
    a.append(a[-1]+a[-2]+a[-3]+a[-4])

print(a[50])