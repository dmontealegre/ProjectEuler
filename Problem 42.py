import string

file = open('p42.txt', 'r')

words = file.readline()

words = words.split(",")   # list of 1786 words

# format the words correctly
for i in range(len(words)):
    words[i] = words[i][1:-1]

# create a dictionary with the value of each letter
# assumes all the letters are upper case.
alphabet = string.ascii_uppercase
dictionary = {}

for i in range(len(alphabet)):
    dictionary[alphabet[i]] = i+1

# compute the numerical value of each word
def value(word):
    answer = 0
    for char in word:
        answer += dictionary[char]
    return answer

values = list(map(value,words))

# a quick search shows that the max word value is 192. Create a set which contains all the triangular numbers < 192
triangular = []
n = 1
while True:
    tri_number = n*(n+1)//2
    triangular.append(tri_number)
    if tri_number > 192:
        break
    n += 1
triangular = set(triangular)

count = 0
for value in values:
    if value in triangular:
        count += 1

print('Number of triangular words is equal to ', count)