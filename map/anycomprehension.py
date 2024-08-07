from data import people, plants_list, plants_dict

# people = []

# Check if people list exist and if there is a 'person' value
# for each item in the person namedtuple
if bool(people) and all([person[1] for person in people]):
    print("Sending email")
else:
    print("User must edit the list of recipients")

if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("This pack contains grass")
else:
    print("No grasses in this pack")

if any([plant.plant_type == "Grass" for plant in plants_dict.values()]):
    print("This pack contains grass")
else:
    print("No grasses in the dict")

if any(plants_dict[key].plant_type == "Grass" for key in plants_dict):
    print("This pack contains grass")
else:
    print("No grasses in this pack")
