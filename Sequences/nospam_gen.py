menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# Remove spam from each list, thep rint the list
# Approach 1
# for meal in menu:
#     top_index = len(meal) - 1
#     for index, ingredient in enumerate(reversed(meal)):
#         if ingredient == "spam":
#             del meal[top_index - index]
#     print(meal)

# Approach 2
for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(meal)

print()

# Print out the items in each list, as long as it's not spam
for meal in menu:
    for ingredient in meal:
        if ingredient != "spam":
            print(ingredient, end=" ")
    print()

print()

# Using generative expressions
for meal in menu:
    items = ", ".join((item for item in meal if item != "spam"))
    print(items)