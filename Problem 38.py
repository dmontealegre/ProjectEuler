def is_pandigital(number):
    string = str(number)
    length = len(string)
    digits = {str(i) for i in range(1, length+1)}
    return digits == set(string)


def prod(seq, number):
    answer = ''
    for i in range(len(seq)):
        answer += str(seq[i] * number)
    return int(answer)


maximum = 0
for i in range(9, 1, -1):
    sequence = [j for j in range(1, i+1)]
    for t in range(int(10**(10//i)), 1, -1):
        if is_pandigital(prod(sequence, t)):
            maximum = max(maximum, prod(sequence, t))
            break

print(maximum)