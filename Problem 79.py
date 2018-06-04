file = open('p79.txt', 'r')

numbers = []
for lines in file.readlines():
    numbers.append(str(int(lines)))

numbers = list(set(numbers))


def get_character():
    char = numbers[0][0]
    for x in range(len(numbers)):
        if char in numbers[x] and char != numbers[x][0]:
            char = numbers[x][0]
    return char


while True:
    if len(numbers) == 0:
        break
    else:
        char = get_character()
        for x in range(len(numbers)):
            if char in numbers[x] and char == numbers[x][0]:
                numbers[x] = numbers[x][1:]
        print(char)

    numbers = list(filter(lambda x: x != '', numbers))


