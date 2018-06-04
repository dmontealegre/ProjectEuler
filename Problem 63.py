# we want m^n to have n digits. clearly m has to be less than 10.
# for a bound on n, we need ceil(n*log(m)) = n
# if we write it as ceil((1-epsilon) n) = ceil(n - epsilon n)
# so if epsilon *n is more than 1 then above cant be equal to n
# hence, the max n can be is 22.
import math
count = 0
for n in range(1, 23):
    for m in range(1, 10):
        if len(str(int(math.pow(m,n)))) == n:
            count += 1

print(count)