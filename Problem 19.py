# counts how many sundays fall on the first of the month given if we are on a leap or not.
# and returns the starting day for the next year
def sunday_count(start, leap):
    # start is a number 0 to 6. 0 is sunday, 1 monday, etc
    if not leap:
        first_days = [start,
                      start + 31,
                      start + (31 + 28),
                      start + (31 + 28 + 31),
                      start + (31 + 28 + 31 + 30),
                      start + (31 + 28 + 31 + 30 + 31),
                      start + (31 + 28 + 31 + 30 + 31 + 30),
                      start + (31 + 28 + 31 + 30 + 31 + 30 + 31),
                      start + (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31),
                      start + (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30),
                      start + (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31),
                      start + (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30),
                      start + (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31)
                      ]
    if leap:
        first_days = [start,
                      start + 31,
                      start + (31 + 29),
                      start + (31 + 29 + 31),
                      start + (31 + 29 + 31 + 30),
                      start + (31 + 29 + 31 + 30 + 31),
                      start + (31 + 29 + 31 + 30 + 31 + 30),
                      start + (31 + 29 + 31 + 30 + 31 + 30 + 31),
                      start + (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31),
                      start + (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30),
                      start + (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31),
                      start + (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30),
                      start + (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31)
                      ]
    count = 0
    for t in range(12):
        if first_days[t] % 7 == 0:

            count += 1
    return count, first_days[12] % 7


# january 1 1901 was a tuesday, so 2
year = 1901
starting = 2
count = 0


def is_leap(t):
    if t % 4 == 0:
        if t % 100 != 0:
            return True
        else:
            if t % 400 == 0:
                return True
    return False

while year < 2001:
    count += sunday_count(starting, is_leap(year))[0]
    starting = sunday_count(starting, is_leap(year))[1]
    year += 1

print(count)