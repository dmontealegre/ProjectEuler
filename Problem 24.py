import itertools

string = '0123456789'
counter = 1
for i in itertools.permutations(string):
    print(counter)
    print(i)
    if counter == 1000000:
        break
    counter += 1