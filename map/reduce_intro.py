import timeit
import functools

def calc_values(x, y: int):
    return x * y

numbers = [2, 3, 5, 8, 13]

# Apply the function on a list of values and return one result
reduced_values = functools.reduce(calc_values, numbers)
print(reduced_values)
# print(sum(numbers))

result = 1
for x in numbers:
    result *= x
print(result)


# This is what reduce() is essentially doing
result = calc_values(2, 3)
result = calc_values(result, 5)
result = calc_values(result, 8)
result = calc_values(result, 13)
print(result)