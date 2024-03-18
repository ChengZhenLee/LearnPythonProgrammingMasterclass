import copy

animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

# Performs a shallow copy
things = animals.copy()     # Creates a new dictionary containing the same 
                            # mutable objects

# Perform a deep copy
# things = copy.deepcopy(animals)   # Creates a new dictionary with
                                    # new mutable objects

print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])

print() 

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])