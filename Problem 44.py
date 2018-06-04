# p_n = n* (3n - 1) / 2
import itertools
limit = 2500

# TODO the shitty trivial solution gave a solution in a few minutes while I thought of something else.
# TODO modify to create a more clever algo :-)

pentagonals = [n*(3*n - 1) // 2 for n in range(limit)]

for i in range(1, limit):
    #print('i', i)
    for j in range(i+1, limit):
        if pentagonals[j]-pentagonals[i] in pentagonals and pentagonals[i]+pentagonals[j] in pentagonals:
            print(i, j)
            break

