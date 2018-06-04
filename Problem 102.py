file = open('p102.txt', 'r')

integers = lambda array: [int(x) for x in array]

triangles = []

for lines in file.readlines():
    triangles.append(integers(lines.split(',')))

# a triangle is an array of length 6, where the entries are the coordinates of the triangle.
def contains_origin(triangle):
    # going to use y = m(x-x_1)+y_1, and we will let x = 0
    if (triangle[0] < 0 and triangle[2] < 0 and triangle[4] < 0) or (triangle[0] > 0 and triangle[2] > 0 and triangle[4] > 0):
        return False
    number3 = (triangle[3]-triangle[1])/(triangle[2]-triangle[0]) * (-(triangle[0]))+triangle[1]
    if triangle[2] * triangle[0] > 0 :
        number3 = 0
    # print(number3)
    number2 = (triangle[5]-triangle[1])/(triangle[4]-triangle[0]) * (-(triangle[0]))+triangle[1]
    if triangle[4]*triangle[0]> 0:
        number2 = 0
    # print(number2)
    number1 = (triangle[5]-triangle[3])/(triangle[4]-triangle[2]) * (-(triangle[2]))+triangle[3]
    if triangle[4] * triangle[2] >0:
        number1 = 0
    # print(number1)
    positive = False
    negative = False
    if number1 > 0 or number2 > 0 or number3 > 0:
        positive = True
    if number1 < 0 or number2 < 0 or number3 < 0:
        negative = True
    return positive and negative

count = 0

for x in triangles:
    if contains_origin(x):
        count += 1

print(count)