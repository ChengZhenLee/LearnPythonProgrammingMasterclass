# numbers = {*""}   # Another way to declare a set
numbers = set()

print(numbers, type(numbers))

# numbers.add(1)
# print(numbers)

# Length of the set won't increase unless a unique number is entered
# while len(numbers) < 4:     
#     next_value = int(input("Please enter your next value: "))
#     numbers.add(next_value)
# print(numbers)

data = [ "blue", "red", "blue", "green", "red", "blue", "white"]

# Create a set from the list, to remove duplicates
# unique_data = set(data)
# Removes duplicates using a set, and then generates a sorted list
# The original order is not preserved
unique_data = sorted(set(data)) 
print(unique_data)

# Create a list of unique colours, keeping the order they appeared
# This is done by making a dict instead of a set
unique_data = list(dict.fromkeys(data))
print(unique_data)

print()
print(dict.fromkeys(data))