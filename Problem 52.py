x = 1
while True:
    if set(str(x)) == set (str(2*x)):
        if set(str(2*x)) == set(str(3*x)):
            if set(str(3 * x)) == set(str(4 * x)):
                if set(str(4 * x)) == set(str(5 * x)):
                    if set(str(5 * x)) == set(str(6 * x)):
                        print(x)
                        break
    x += 1
