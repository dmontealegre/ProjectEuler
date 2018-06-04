import math

file = open('p99.txt', 'r')

array = []
for line in file.readlines():
    number = []
    line += ','
    string = ''
    for char in line:
        if char != ',':
            string += char
        else:
            number.append(int(string))
            string = ''
    array.append(number)

array2 = [math.log(x[0]) * x[1] for x in array]

print(array2.index(max(array2)))
