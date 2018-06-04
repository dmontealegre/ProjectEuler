# Problem 3

# let current be the number you want to find the highest prime divisor of.
current = 600851475143

print("The highest prime divisor of %s is " % current, end= "")

answer = 2
while current > 1:
    if current % answer == 0:
        while current % answer == 0:
            current /= answer
    answer += 1

print(answer-1)




