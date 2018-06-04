# not super fast, but solves it.

import collections
import itertools
import math

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
file = open('p98.txt', 'r')

line = file.readline()
line = line.split(',')
words = tuple([word[1:-1] for word in line])


dictionary = {}
for word in words:
    count = collections.Counter()
    for char in word:
        count[char] += 1
    dictionary[word] = count

pairs = []


# we find the pairs of anagrams.
for x in dictionary.keys():
    for y in dictionary.keys():
        if x != y and dictionary[x] == dictionary[y]:
            pairs.append([x, y])


# for each word, and encoding, we return whether it is a square, and if it is we return that value.
def value_square(word, dictionary):
    if dictionary[word[0]] == 0:
        return False, 0
    value = ''
    for char in word:
        value += str(dictionary[char])
    return math.floor(math.sqrt(int(value))) == math.sqrt(int(value)), (int(value))


best = 0
# perhaps a way to make it run better:
# look at pair[0], and check which encoding makes it a perfect square
# then we only test pair[1] at those encondings.
# right now we check every enconding, and check if it makes both words a square, which is wasteful.
for pair in pairs:
    characters = tuple([i for i in pair[0]])
    for permutation in itertools.permutations(digits, len(characters)):
        encode = {}
        for i in range(len(characters)):
            encode[characters[i]] = permutation[i]
        if value_square(pair[0], encode)[0] and value_square(pair[1], encode)[0]:
            if value_square(pair[0], encode)[1] > best or value_square(pair[1], encode)[1] > best:
                print('New best value of ', max(value_square(pair[0], encode)[1], value_square(pair[1], encode)[1]))
                print(pair[0], pair[1], encode)
                best = max(value_square(pair[0], encode)[1], value_square(pair[1], encode)[1])
