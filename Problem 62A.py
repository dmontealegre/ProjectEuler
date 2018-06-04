import math


#the following is a function that converts a number into an array which corresponds to its digits. For example
#the number 1856 will outout [6,5,8,1]
def number_to_array(n):
    array = []
    while n != 0:
        array.append(n-(n//10)*10)
        n = n//10
    return array


def round_up(n):
    m = n
    treshold = math.ceil(math.log10(n*n*n))
    while math.ceil(math.log10(m*m*m)) == treshold:
        m = m+1
    if (m-1) % 10 == 0:
        m= m-1
    return m-1


def permutation_cube_array(n):
    #first we need to round up our given number. see remark below.
    n = round_up(n)
    #we are going to keep 3 arrays. One with the numbers, one with the corresponding set of digits of the number,
    #and third one that keeps track of the number of times we have used a given set of digits (meaning the permutations).
    number = []
    seen_permutations = []
    multiplicity_permutations = []
    for x in range(1,n+1):
        y = x*x*x
        A = number_to_array(y)
        A.sort()
        if A not in seen_permutations:
            seen_permutations.append(A)
            multiplicity_permutations.append(1)
            number.append(x)
        else:
            for t in range(0,len(seen_permutations)):
                if seen_permutations[t] == A:
                    multiplicity_permutations[t] = multiplicity_permutations[t]+1
    return seen_permutations, multiplicity_permutations, number


def find_multiplicities_below(multiplicities, n):
    if type(n)!= int:
        raise TypeError('n must be an integer')
    if n<1:
        raise TypeError('n must be positive')
    if type(multiplicities) != int:
        raise TypeError('multiplicities must be an integer')
    if multiplicities < 1:
        raise TypeError('multiplicities must be positive')
    Result = permutation_cube_array(n)
    print('The following is a complete list of numbers that are below(', n, ')^3 and have exactly ', multiplicities, 'cubic permutations:')
    for t in range(0, len(Result[0])):
        if Result[1][t] == multiplicities:
            print('The number n =(', Result[2][t], ')^3 has the property that n^3 contains exactly', multiplicities , 'cubic permutations')

find_multiplicities_below(5,10000)

#remark: the printed numbers are the smallest representatives for the permutation class. For example {1,2,5} has two cubic permutations
# 125 and 512, but the code will give 5^3 as a number with 2 cubic permutations, but it will not write 8^3.