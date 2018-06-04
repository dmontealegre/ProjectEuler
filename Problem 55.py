
def is_lychrel(number):
    counter = 0
    while counter < 50:
        number += int(str(number)[::-1])
        if str(number) == str(number)[::-1]:
            return True
        counter += 1
    return False

summation = 0

for x in range(1,10000):
    if not is_lychrel(x):
        print(x)
        summation += 1

print(summation)
print(is_lychrel(4994))