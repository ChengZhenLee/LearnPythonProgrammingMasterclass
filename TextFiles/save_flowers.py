data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# plants_filename = "flowers_print.txt"

# with open(plants_filename, "w") as plants:
#     for plant in data:
#         # Print the text into the file (with conversions by print)
#         print(plant, file=plants)

# new_list = []
# with open(plants_filename) as plants:
#     for plant in plants:
#         new_list.append(plant.rstrip())

# print(new_list)

# plants_filename = "flowers_write.txt"

# with open(plants_filename, "w") as plants:
#     for plant in data:
#         # Write the text into the file (without any conversions like print)
#         plants.write(plant)

# print(data)
# string_representation = data.__str__()
# print(type(string_representation))

filename = "test_numbers.txt"
with open(filename, "w") as test:
    for i in range(10):
        # Print will convert to string representation `__str__`
        print(i, file=test)

# Overwrites the file
with open(filename, "w") as test:
    for i in range(10):
        # Write only accepts str
        test.write(str(i) + "\n")