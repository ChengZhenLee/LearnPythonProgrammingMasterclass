entries = [1, 2, 3, 4, 5]

# Returns True if all items in the list are True
print("all: {}".format(all(entries)))
# Returns True if any item in the list is True
print("any: {}".format(any(entries)))

print("Iteratble with a 'False' value")
entries_with_zero = [1, 2, 0, 4, 5]
print("all: {}".format(all(entries_with_zero)))
print("any: {}".format(any(entries_with_zero)))

print("=" * 80)
name = "Tim"
if name:
    print("Hello {}".format(name))
else:
    print("Welcome, person with no name")
