import math


number = 1
for x in range(7830457):
    print(x)
    number *= 2
    while number > math.pow(10, 10):
        number -= math.pow(10, 10)

number = 28433 * number + 1
while number > math.pow(10, 10):
    number -= math.pow(10, 10)
# take last 10 digits of the following output
print(number)
