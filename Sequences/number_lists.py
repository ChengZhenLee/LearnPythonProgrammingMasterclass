empty_list = []
even  = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)    # creates a new list
print(sorted_numbers)
print(numbers)

digits = list("432985617")          # creates a new list
print(digits)

# more_numbers = list(numbers)      # creates a new list
# more_numbers = numbers[:]         # creates a new list
more_numbers = numbers.copy()       # creates a new list
print(more_numbers)
print(numbers is more_numbers)      # checks if they are the same list
print(numbers == more_numbers)      # checks if the contents are the same

# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))

# print(len(even))
# print(len(odd))

# print()
# print("mississippi".count("issi"))

# even.extend(odd)
# print(even)
# another_even = even
# print(another_even)

# even.sort()
# print(even)

# even.sort(reverse=True)
# print(even)
# print(another_even)