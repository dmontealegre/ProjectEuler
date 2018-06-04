def is_curious(x,y):
    # takes two 2-digit numbers x < y, and we check if we can 'cancel' and get the correct answer
    x_str = str(x)
    y_str = str(y)

    if x_str[1] == '0' or y_str[1] == '0':
        # this are the trivial examples.
        return False
    x_str = [x_str[i] for i in range(len(x_str))]
    y_str = [y_str[i] for i in range(len(y_str))]
    for char in x_str:
        if char in y_str:
            x_str.remove(char)
            y_str.remove(char)
            new_x = int(x_str[0])
            new_y = int(y_str[0])
            return new_x/new_y == x/y
    return False


for x in range(11, 100):
    for y in range(x+1, 100):
        if is_curious(x,y):
            print(x,y)
