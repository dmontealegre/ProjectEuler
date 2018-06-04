file = open('p67.txt', 'r')

array = []
for lines in file.readlines():
    lines += ' '
    line = []
    number = ''
    for char in lines:
        if char != ' ':
            number += char
        else:
            line.append(int(number))
            number = ''
    array.append(line)

print(array)

for x in range(1,len(array)):
    array[x][0] += array[x-1][0]
    array[x][-1] += array[x-1][-1]
    for y in range(1,len(array[x])-1):
        array[x][y] = array[x][y] + max(array[x-1][y-1],array[x-1][y])


print(max(array[len(array)-1]))