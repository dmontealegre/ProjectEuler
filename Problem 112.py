def bouncy(number):
    increasing = True
    decreasing = True
    string = str(number)
    for x in range(len(string)-1):
        if int(string[x]) > int(string[x+1]):
            increasing = False
        if int(string[x]) < int(string[x+1]):
            decreasing = False
    return not increasing and not decreasing

proportion = .99
pointer = 1
bouncies = 0
while True:
    if bouncy(pointer):
        bouncies += 1
    if bouncies / pointer == proportion:
        print(pointer)
        break
    pointer += 1
