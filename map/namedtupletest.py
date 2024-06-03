from data import basic_plants_list, plants_list

print(plants_list[0])

# for plants in basic_plants_list:
#     print(plants[0])

for plant in plants_list:
    print(plant.name, plant[1])

print()

example = plants_list[0]
print(example)
# replace the 'lifecycles' with the value Annual field in this Plant namedtuple
example = example._replace(lifecycles='Annual')
print(example)