# Problem 1

bound = 1000
count = 0
for x in range(1, bound):
    if x % 5 == 0 or x % 3 == 0:
        count += x

print("The sum of the multiples of 3 and 5 below %s is " % bound, count)

