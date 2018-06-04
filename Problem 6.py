# Problem 6

square_sum = lambda n: n * (n+1) * (2*n + 1) // 6
linear_sum = lambda n: n * (n+1) // 2

print("The difference between the sum of the squares of the first one hundred natural numbers and the square ", end="")
print("of the sum is ", linear_sum(100)**2 - square_sum(100))
