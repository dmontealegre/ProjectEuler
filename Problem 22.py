import string
file = open('p22.txt', 'r')
line = file.readline()
names = line.split(",")

# format the words correctly
for i in range(len(names)):
    names[i] = names[i][1:-1]

alphabet = string.ascii_uppercase
dictionary = {}
names.sort()
for i in range(len(alphabet)):
    dictionary[alphabet[i]] = i+1

def value(word):
    answer = 0
    for char in word:
        answer += dictionary[char]
    return answer

count = 0
for i in range(len(names)):
    count += value(names[i]) * (i+1)

print(count)