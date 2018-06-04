import math

def is_decomposable(n):
    y=int(math.sqrt(n))
    if y*(y+1) == n:
        return True
    else:
        return False



def is_there_a_half(n):
    denominator = n*(n-1)
    numerator = denominator//2
    if is_decomposable(numerator) == True:
        return True
    else:
        return False


n = 927538920

while n <100:
    if is_there_a_half(n) == False:
        n=n+1
    else:
        print(n)
        n = int(5.828427122143373647174424069262318319470283447*n)
