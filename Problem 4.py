# Problem 4

# Function which returns if a number is a palydrome
is_palindrome = lambda n: str(n)[::-1] == str(n)


def is_product(n):
    current = 100
    while current < 1000:
        if n/current == int(n/current) and len(str(int(n/current))) == 3:
            return True
        else:
            current += 1
    return False

number = 1000000

while True:
    if is_palindrome(number) and is_product(number):
        print("The largest palindrome made from the product of two 3-digit numbers is ", number)
        break
    else:
        number -= 1