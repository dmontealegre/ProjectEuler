# the idea is that we have 1, 3,5,7,9 (those are +2), 13,17,21,25 (those are +4), and so on

current = 1
answer = 0
counter = 0
stepsize = 2

while current < 1001**2+1:
    answer += current
    current += stepsize
    counter += 1
    if counter == 4:
        stepsize += 2
        counter = 0

print(answer)



