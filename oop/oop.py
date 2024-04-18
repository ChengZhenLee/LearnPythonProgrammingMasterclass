# a = 12
# b = 4
# print(a + b)
# __add__ is a method of `a`
# print(a.__add__(b))


# Declare a Kettle object
class Kettle(object):

    # Create class attribute that is same in all instances
    power_source = "electricity"

    # This is a constructor
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    # This is a method. There will always be a `self` parameter
    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics
Object: an instance of a class.
Instantiate: create an instance of a class
Method: a functions defined in a class
Attribute: a variable bound to an instance of a class
"""

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

# Alternative way to call a method
Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

print("*" * 80)

# Creating a data attribute for the kenwood object
# This is an "Instance Variable"
kenwood.power = 1.5
print(kenwood.power)
# hamilton instance doesnt have `power` instance variable
# print(hamilton.power)

# Since the `power_source` class attribute was initialized
# in Kettle class and not the instances, the instance has to
# find the `power_source` class attribute in the Kettle class itself
# If the class_attribute is changed in Kettle, it will change in all
# instances as well
print("Switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)