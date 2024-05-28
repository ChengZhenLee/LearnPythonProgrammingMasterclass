print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

# This is a list comprehension
# squares = [number ** 2 for number in numbers]

# This is a set comprehension
# squares = { number ** 2 for number in numbers }

squares = [number ** 2 for number in range(1, 7)]

print(squares)