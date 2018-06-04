import math
s = ''
for i in range(1000000):
    s += str(i)

answer = 1
for i in range(7):
    answer *= int(s[int(math.pow(10,i))])

print(answer)