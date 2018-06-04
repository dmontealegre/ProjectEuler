# # pythagorean triples:
# # a = k ( m^ 2 - n^ 2)
# # b = k (2mn)
# # c = k ( m^2 + n^2)
# # and m > n, with m, n coprime and not both odd
#
import math
bound = 1500001
length_solutions = [0 for i in range(bound)]
answer = 0
for m in range(2, int(math.ceil(math.sqrt(bound/2)))):
    for n in range(m-1, 0, -2):
        if math.gcd(m, n) == 1 and (m+n) % 2 == 1:
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
            p = a + b + c
            k = 1
            while p <= bound:
                length_solutions[p] += 1
                if length_solutions[p] == 1:
                    answer += 1
                if length_solutions[p] == 2:
                    answer -= 1
                p = p + a + b + c

print(answer)


