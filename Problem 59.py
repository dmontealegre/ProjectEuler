import string
import itertools
from collections import Counter

file = open('p59.txt', 'r')

line = file.readline()

numbers = line.split(',')

numbers = [int(i) for i in numbers]

print(numbers)



# for a character we do ord(character) to obtain the ascii value
# for a number to obtain the character we do chr(number)


def decode(message, key):
    # message is an array of numbers
    t = len(message)
    while len(key) < len(message):
        key += key
    key = key[:t]
    return [chr(message[i] ^ ord(key[i])) for i in range(len(message))]


letters = string.ascii_lowercase
letters = [char for char in letters]
# data = Counter(numbers)
# print(data.most_common())
# # 79 is the most common. probably corresponds to e.
# # hence, we want 79 XOR (ord[key[0]) = 101

for letter in letters:
    testkey = [letter,letter,letter]
    print(letter, 'the message is ' , end='')
    decoded = decode(numbers, testkey)
    for i in range(0,len(decoded), 3):
        print(decoded[i], end= '')
    print('')

# first letter of the key is g, since it gives the only reasonable line
print('NEXT ANALYSIS -------------------')
for letter in letters:
    testkey = [letter,letter,letter]
    print(letter, 'the message is ' , end='')
    decoded = decode(numbers, testkey)
    for i in range(1,len(decoded), 3):
        print(decoded[i], end= '')
    print('')
# second letter must be o
print('NEXT ANALYSIS -------------------')
for letter in letters:
    testkey = [letter,letter,letter]
    print(letter, 'the message is ' , end='')
    decoded = decode(numbers, testkey)
    for i in range(2,len(decoded), 3):
        print(decoded[i], end= '')
    print('')
# third letter is d

# key is god

print(decode(numbers, ['g','o','d']))

answer = sum(map(ord,decode(numbers, ['g','o','d'])))
print(answer)
