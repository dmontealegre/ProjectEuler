import itertools
import math

indices = [i for i in range(2, 101)]
my_list = []

for i in itertools.product(indices,repeat=2):
    my_list.append(int(math.pow(i[0],i[1])))

my_list = list(set(my_list))

print(len(my_list))