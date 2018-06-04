import math
import copy


# gives an array of the primes numbers less or equal to n. This function was not created by me. It is a well known
# algorithm called Eratosthenes sieve
def primes_sieve(limit):
    true_limit = limit + 1
    not_prime = [False] * true_limit
    primes = []

    for i in range(2, true_limit):
        if not_prime[i]:
            continue
        for f in range(i * 2, true_limit, i):
            not_prime[f] = True

        primes.append(i)

    return primes


# receives a factorization array, and checks if the corresponding number n has the property that d(n^2)>threshold.
def above_threshold(A, threshold):
    product = 1
    for x in range(0, len(A)):
        product = product * (2 * A[x][1] + 1)
    if product > threshold:
        return True
    else:
        return False


# given a number n with prime factorization n=p_1^(t_1)*p_2^(t_2)...*p_k^(t_k) it outputs [[p_i,t_i] for i=1,2,..,k]
# but it must receive a pool of prime numbers P.
def get_prime_factors(n, P):
    factors = []
    if n == 1:
        raise TypeError('1 does not have any prime factors')
    else:
        for x in P:
            if n % x == 0:
                cx = 0
                while n % x == 0:
                    cx = cx + 1
                    n = n // x
                factors.append([x, cx])
    return factors

def brute_force(threshold):
    solution = 1
    divisors_of_solution_square = 1
    while divisors_of_solution_square < 2*threshold-1:
        solution = solution + 1
        P = primes_sieve(solution*solution)
        divisors_of_solution_square = number_divisors(solution*solution,P)
    print('The minimal n such that the equation has more than', threshold, 'solutions is n =', solution)


def array_to_number(A):
    product = 1
    for x in range(0, len(A)):
        product = product * (A[x][0] ** A[x][1])
    return product


def number_divisors(n, P):
    factors = 1
    primes = get_prime_factors(n, P)
    for x in range(0, len(primes)):
        factors = factors * (primes[x][1] + 1)
    return factors


# A is a prime factorization array, and we are going to improve the answer
def best_swap(A, threshold, P):
    number_to_delete = A[len(A) - 1][0] ** A[len(A) - 1][1]
    value = False
    x = 2
    while value == False:
        A2 = copy.deepcopy(A)
        # we are going to delete the last number and replace it by x. since we want an improvement
        # we only run x up to the number we want to delete (otherwise we aren't improving)
        factors_x = get_prime_factors(x, P)
        # we get the array of the product of the number corresponding to A and x. Since we already have the numbers factored
        # it is faster to add exponents of the same primes.
        for y in range(0, len(factors_x)):
            for z in range(0, len(A2)):
                if factors_x[y][0] == A2[z][0]:
                    A2[z][1] = A2[z][1] + factors_x[y][1]
        A2.pop()
        x = x + 1
        value = above_threshold(A2, threshold)
    return A2


# we are going to give a function, such that given a threshold, it will find the smallest integer n, such that
# (d(n^2)+1)/2 > threshold.
def minimal_number(threshold):
    if type(threshold) != int:
        raise TypeError('input must be an integer')
    if threshold < 1:
        raise TypeError('input must be a positive integer')
    # we want d(n^2) to be greater than the following value
    true_threshold = 2 * threshold - 1
    # first, if the threshold is smaller than 6, then we do brute force:
    if threshold < 6:
        return brute_force(threshold)

    # we determine at most how many primes we will need:
    upper_bound_number_primes = math.ceil(math.log(true_threshold, 3))
    upper_bound_number_primes = int(upper_bound_number_primes)
    # find the bound_primes_sieve we will use in the Prime Number Theorem:
    bound_primes_sieve = 2 * upper_bound_number_primes * math.log(upper_bound_number_primes)
    bound_primes_sieve = int(bound_primes_sieve)
    P0 = primes_sieve(bound_primes_sieve)
    # since the above is an asymptotic, we trim it to get our actual desired lists of primes:
    P = [P0[x] for x in range(0, upper_bound_number_primes)]
    # by construction we have already that n := P[0]*...*P[len(P)-1] gives an n that works, but it might not be minimal.
    current_solution = 1
    for j in range(0, len(P)):
        current_solution = current_solution * (P[j])
    # the idea for the algorithm is to do swaps to improve the answer until it is no longer possible.
    current_solution_factorization = get_prime_factors(current_solution, P)
    room_improvement = True
    while room_improvement == True:
        candidate_factorization = best_swap(current_solution_factorization, true_threshold, P)
        candidate = array_to_number(candidate_factorization)
        if candidate < current_solution:
            current_solution = candidate
            current_solution_factorization = candidate_factorization
        else:
            room_improvement = False
    print('The minimal n such that the equation has more than', threshold, 'solutions is n =', current_solution)


minimal_number(3)
minimal_number(100)
minimal_number(1000)
minimal_number(4000000)
