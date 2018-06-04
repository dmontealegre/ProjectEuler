numbers = set()

for x in range(1,12001):
    for y in range(1,12001):
        if x/y > 1/3 and x/y < 1/2:
            numbers.add(x/y)

print(len(numbers))
