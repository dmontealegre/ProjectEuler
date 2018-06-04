import math
import time
def is_pandigital(number):
    string = str(number)
    digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    return digits == set(string)

fibs = [1, 1, 1]

while True:
    stop = time.time()
    if is_pandigital(int(str(fibs[-1])[:9])) and is_pandigital(int(str(fibs[-1])[-9:])):
        break
    else:
        fibs.append(fibs[-1]+fibs[-2])
    print(len(fibs), time.time()-stop)


