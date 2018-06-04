fibs = [0, 1, 1]
pointer = 2
while True:
    fibs.append(fibs[pointer]+fibs[pointer-1])
    pointer += 1
    if len(str(fibs[pointer]))>= 1000:
        break

print(pointer)
