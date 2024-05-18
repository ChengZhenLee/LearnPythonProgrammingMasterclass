# *args in parameter tells the function to expect multiple parameters
# and then save it as a tuple
def average(*args):
    # the tuple will be saved as a variable `args`
    print(type(args))
    print("Args is: {}".format(args))
    # * operator in the function unpacks the tuple `args`
    print("*args is:", *args)
    mean = 0
    for arg in args:
        mean += arg
    
    return mean / len(args)


print(average(1, 2, 3, 4))


# challenge function
def build_tuple(*args):
    """ returns a tuple of the multiple parameters inputted """
    return args


message_tuple = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")
print(type(message_tuple))
print(message_tuple)