# Problem 2


# create a list of the fibonacci numbers less than n
def create_fibs(n):
    f = [1, 2]
    while f[len(f)-2]+f[len(f)-1] < n:
        f.append(f[len(f)-2]+f[len(f)-1])
    return f

bound = 4000000
A = create_fibs(bound)

answer = 0
for i in range(0, len(A)):
    if A[i] % 2 == 0:
        answer += A[i]

print("The sum of the even Fibonacci numbers less than %s is " % bound, answer)
