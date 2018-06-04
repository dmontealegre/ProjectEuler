import math
n = 28123


def divisors(n):
    answer = [1]
    for m in range(2,int(math.sqrt(n)+1)):
        if n % m == 0:
            answer.append(m)
            if m != n // m:
                answer.append(n//m)
    return answer


abundant = []
for i in range(1, n+1):
    if sum(divisors(i)) > i:
        abundant.append(i)

# now we compute all the possible sums:
sums = []
for i in range(len(abundant)):
    for j in range(len(abundant)):
        sums.append(abundant[i]+abundant[j])

# make it a set so we delete repetitions and fast queues

sums = set(sums)

# now we count what is missing

answer = 0
for i in range(1,n+1):
    if i not in sums:
        answer += i

print(answer)