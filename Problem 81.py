file = open('p81.txt', 'r')

matrix = []
for lines in file.readlines():
    lines += ','
    array = []
    number =''
    for char in lines:
        if char != ',':
            number += char
        else:
            array.append(int(number))
            number = ''
    matrix.append(array)

min_matrix = matrix

#
# print(matrix[0][0:3])
# print(matrix[1][0:3])
# print(matrix[2][0:3])
#
# print('====================')

# do the first row:
min_matrix[0][0] = matrix[0][0]
for j in range(1, 80):
    min_matrix[0][j] += min_matrix[0][j-1]


# do the first column:
for i in range(1,80):
    min_matrix[i][0] += min_matrix[i-1][0]

for i in range(1, 80):
    for j in range(1,80):
        min_matrix[i][j] += min(min_matrix[i-1][j], min_matrix[i][j-1])
#
# print(min_matrix[0][0:3])
# print(min_matrix[1][0:3])
# print(min_matrix[2][0:3])

print(min_matrix[79][79])