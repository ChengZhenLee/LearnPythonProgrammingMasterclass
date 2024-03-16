vehicles = {
    'dream': 'Honda 250T',
    # 'roadster': 'BMW R1100'
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triump Street Triple', # Replaces the value 'BMW R1100'
}

# my_car = vehicles['fiesta']     # will crash the program if the key is not found
# print(my_car)

# commuter = vehicles['virago']
# print(commuter)

# learner = vehicles.get("ER5")   # .get() will return None if the key is not found
# print(learner)

vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"

# Upgrade the Virago
vehicles["virago"] = "Yamaha XV535"

del vehicles["starfighter"]
# del vehicles["f1"]
result = vehicles.pop("f1", None)    # Returns the second argument if the value is not found
print(result)
plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "not present")
print(bike)
print()

# for key in vehicles:
#     print(key, vehicles[key], sep=", ")
for key, value in vehicles.items():
    print(key, value, sep=", ")
