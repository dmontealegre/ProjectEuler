
def pan_product(number):
    if '0' in str(number):
        return False
    answer = False
    digits = str(number)
    for x in range(2, number//2):
        if number % x == 0:
            y = number // x
            digits = digits + str(x) + str(y)
            if len(digits) == 9 and '0' not in digits and len(set(digits)) == 9:
                answer = True
                break
            else:
                digits = str(number)
    return answer

# an easy check tells us that the product must be at most 5 digits long.
count = 0
for x in range(1000, 99999):
    # first we check if x is even good:
    if len(str(x)) == len(set(str(x))) and '0' not in str(x):
        if pan_product(x):
            print(x)
            count += x

print(count)
