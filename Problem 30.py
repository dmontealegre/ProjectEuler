answer = 0
for x in range(2,1000000):
    str_x = str(x)
    count = 0
    for char in str_x:
        count += int(char)**5
    if count == x:
        answer += x

print(answer)
