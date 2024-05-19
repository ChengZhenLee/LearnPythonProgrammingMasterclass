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


# ===== KWargs =====
# def print_backwards(*args, **kwargs):
#     # kwargs is a dictionary
#     print(kwargs)
#     kwargs.pop('end', None)
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs)

def print_backwards(*args, **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for word in args[:0:-1]:    # change the range to not print the first word
        print(word[::-1], end=sep_character, **kwargs)
    print(args[0][::-1], end=end_character, **kwargs)   # and print the first word separately
    # print(end=end_character)  # which means we don't need this line


def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)

with open("backwards.txt", 'w') as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')
    print("Another String")


print()
print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
backwards_print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print("=" * 10)