
collatz = [None]*1000001
collatz[0] = 0
collatz[1] = 1

def length_sequence(number):
    length = 1
    while number > 1:
        if number % 2 == 0:
            length += 1
            number /= 2
        else:
            length += 1
            number = 3*number + 1
    return length


for i in range(2, 1000001):
    number = i
    temp = 0
    while number >= i:

        if number % 2 == 0:
            number /= 2
        else:
            number = 3*number + 1
        temp += 1
    temp += collatz[int(number)]
    collatz[i] = temp

print(collatz.index(max(collatz)))

print(length_sequence(837799))