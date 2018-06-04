file = open('p11.txt', 'r')
array = []
for lines in file.readlines():
    lines = lines[:-7]
    array.append(lines.split(' '))


for x in range(len(array)):
    for y in range(len(array[x])):
        array[x][y] = int(array[x][y])

#brute force solution works super fast.

best_side = 0

for y in range(20):
    for x in range(17):
        sideways = array[y][x] *array[y][x+1] *array[y][x+2] *array[y][x+3]
        best_side = max(best_side, sideways)

best_vertical = 0

for y in range(17):
    for x in range(20):
        vertical = array[y][x]*array[y+1][x] *array[y+2][x] *array[y+3][x]
        best_vertical = max(best_vertical, vertical)

best_diag_dr = 0

for y in range(17):
    for x in range(17):
        diag = array[y][x] *array[y+1][x+1] *array[y+2][x+2] *array[y+3][x+3]
        best_diag_dr = max(best_diag_dr, diag)

best_diag_dl = 0

for y in range(17):
    for x in range(3,20):
        diag = array[y][x] *array[y+1][x-1] *array[y+2][x-2] *array[y+3][x-3]
        best_diag_dl = max(diag, best_diag_dl)

print(max(best_vertical, best_side, best_diag_dr, best_diag_dl))

file.close()