array = {}

for n in range(10000001):
    print(n)
    chain = [n]
    while True:
        string = str(chain[-1])
        sum = 0
        for char in string:
            sum += int(char)**2
        if sum in array.keys():
            array[n] = array[sum]
            break
        if sum in chain and 89 in chain:
            chain.append(sum)
            array[n] = True
            break
        if sum in chain and 89 not in chain:
            chain.append(sum)
            array[n] = False
            break
        chain.append(sum)

count = 0
for x in array.keys():
    if array[x]:
        count += 1

print(count)

