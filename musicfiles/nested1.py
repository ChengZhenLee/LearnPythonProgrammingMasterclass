burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "beans", "spam"]

# The left burger loop is considered first before the right topping
for meals in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meals)

print()

# for burger in burgers:
#     for topping in toppings:
#         print((burger, topping))

# The outer topping loop is considered first before the inner burger loop
for nested_meals in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(nested_meals)

print()

for nested_meals in [[(burger, topping) for topping in toppings] for burger in burgers]:
    print(nested_meals)