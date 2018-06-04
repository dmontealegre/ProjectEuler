# pythagorean triples are of the form
# a = k(m^2 - n^2)
# b = 2kmn
# c = k(m^2+n^2)
# for m > n coprime and not both odd. and k a positive int.

# then a+b+c = 2k(m^2 +mn) = 2km(m+n)


def pythagorean_solutions(number):
    sum = 0
    if number % 2 != 0:
        return 0
    else:
        number /= 2
        for k in range(1, int(number+1)):
            if number % k == 0:
                for m in range(1, int(number//k +1)):
                    if number// k % m == 0:
                        for n in range(1, m):
                            if number == k*m*(m+n) and m% 2 != n%2:
                                print(k,m,n)
                                sum += 1
    return sum

answer = 0
pointer = 0
for i in range(1, 1000):
    if answer < pythagorean_solutions(i):
        answer = pythagorean_solutions(i)
        pointer = i

print(pythagorean_solutions(12))
print(pointer)


