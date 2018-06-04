file = open('p13.txt', 'r')

summation = 0
for lines in file.readlines():
    lines = lines[:-7]
    summation += int(lines)

print(str(summation)[:10])
file.close()