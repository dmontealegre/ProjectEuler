# we will solve each color recursively
# the arrays will include the all 1's solution.
red = [0, 1, 2]
while len(red) < 51:
    red.append(red[-1]+red[-2])

green = [0, 1, 1, 2]
while len(green) < 51:
    green.append(green[-1]+green[-3])

blue = [0,1,1,1,2]
while len(blue) < 51:
    blue.append(blue[-1]+blue[-4])

print(red[50]+green[50]+blue[50]-3)