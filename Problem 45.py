import math


# h_n = n(2n-1)
def is_hexagonal(number):
    # we want to check if there is a t
    # such that 2t^2 - t = number
    root_1 = (1 - math.sqrt(1 - 4*2*(-number))) / (2*2)
    root_2 = (1 + math.sqrt(1 - 4*2*(-number))) / (2*2)
    if root_1 == int(abs(root_1)) or root_2 == int(abs(root_2)):
        return True
    else:
        return False


# p_n = n(3n-1)/2
def is_pentagonal(number):
    # want to solve 3n^2/2 - n/2 - number = 0
    root_1 = (1/2 - math.sqrt(1/4 - 4 * (3/2) * (-number))) / (2 * (3/2))
    root_2 = (1/2 + math.sqrt(1/4 - 4 * (3/2) * (-number))) / (2 * (3/2))
    if root_1 == int(abs(root_1)) or root_2 == int(abs(root_2)):
        return True
    else:
        return False

n = 286
while True:
    triangular_n = n*(n+1)/2
    if is_pentagonal(triangular_n) and is_hexagonal(triangular_n):
        print(int(triangular_n), n)
        break
    n += 1

print(is_pentagonal(7906276))