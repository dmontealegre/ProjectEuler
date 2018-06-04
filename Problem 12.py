import time
start_time = time.time()

def number_divisors(n):
    current = n
    divisor = 2
    answer = 1
    while current > 1:
        if current % divisor == 0:
            temp = 1
            while current % divisor == 0:
                current /= divisor
                temp += 1
            answer *= temp
        divisor += 1
    return answer

n = 1
while True:
    triangular_n = n*(n+1)/2
    if number_divisors(triangular_n) > 500:
        print(int(triangular_n))
        break
    n += 1

print(time.time() - start_time)