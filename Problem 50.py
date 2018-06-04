import itertools

def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

my_list = primes2(1000000)
# length =[ i for i in range(len(my_list))]
#
# maximum = 0
# for i in itertools.permutations(length, 2):
#     if sum(my_list[i[0]:i[1]]) in my_list:
#         if maximum < i[1]-i[0]:
#             print(my_list[i[0]:i[1]])
#             maximum = max(maximum, i[1]-i[0])


longest_so_far = 0

for i in range(len(my_list)):
    for j in range(i+longest_so_far, len(my_list)):
        if sum(my_list[i:j]) > 1000000:
            break
        elif sum(my_list[i:j]) in my_list:
            longest_so_far = max(j-i, longest_so_far)
            print(sum(my_list[i:j]))
        elif sum(my_list[i:j])> my_list[len(my_list)-1]:
            break
