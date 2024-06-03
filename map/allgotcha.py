entries = []

if entries:
    # any still returns True for an empty list
    print("all: {}".format(all(entries)))
else:
    print(False)
print("any: {}".format(any(entries)))

result = bool(entries and all(entries))
print(result)