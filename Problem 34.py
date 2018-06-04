import math

def is_digit_factorial(n):
    string = str(n)
    summation = 0
    for char in string:
        summation += math.factorial(int(char))
        if summation > n:
            break
    return summation == n

sums = 0

# when 9!*log_10(n) < n is the upper bound for the loop. around 2.5 million 
for i in range(10, 2500000):
    if is_digit_factorial(i):
        sums += i
        print(i)

print(sums)

