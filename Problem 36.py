import math

# takes a positive number n and it writes the base two (in a string)
def write_binary(n):
    base2 = ''
    length = math.ceil(math.log(n, 2))
    for i in range(length, -1, -1):
        if n >= math.pow(2, i):
            base2 += '1'
            n -= math.pow(2, i)
        else:
            base2 += '0'
    if base2[0] == '0':
        base2 = base2[1:]
    return base2

summation = 0

for i in range(1,1000000):
    if str(i) == str(i)[::-1] and write_binary(i) == write_binary(i)[::-1]:
        summation += i

print(summation)