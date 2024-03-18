small_ints = set(range(21))
print(small_ints)

# Clear all items in the set
# small_ints.clear()
# print(small_ints)

small_ints.discard(10)
small_ints.remove(11)
print(small_ints)

small_ints.discard(99)  # Does nothing if 99 is not in the set
print(small_ints)

small_ints.remove(99)  # Crashes if 99 is not in the set
print(small_ints)