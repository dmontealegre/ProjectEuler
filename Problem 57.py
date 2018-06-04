
# 3/2
# 7/5
# 17/12
# 41/29
# a / b
# (2b+a)/ (b+a)

a = [3]
b = [2]

for x in range(1,1000):
    a.append(2*b[x-1] + a[x-1])
    b.append(b[x-1] + a[x-1])

count = 0
for x in range(1000):
    if len(str(a[x])) > len(str(b[x])):
        count += 1


print(count)

