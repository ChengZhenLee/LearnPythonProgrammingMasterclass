import sys


# create a function with makes a generator
def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))
        yield start
        start += 1

# big_range = range(10000)
# the Function, which is using yield, is not called here immediately
big_range = my_range(5)
# _ = input("line 14")

print(next(big_range))
print("big_range is {}".format(sys.getsizeof(big_range)))

# create a list containing all the values in big range
big_list = []

# _ = input("line 22")
for val in big_range:
    # whenever the value is accessed from big_range which has it's
    # values generated by the function, every loop will execute a 'next'
    # function which will call the function for big_range and get the value
    # _ = input("line 24 - inside loop")
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)

print("looping again ... or not")
# since big_range has been 'accessed' already, it has run out of calls
# for the associated my_range function.
# Looping through it will not generate anything
# for i in big_range:

for i in my_range(5):
    print("i is {}".format(i))


# When my_range uses yield, it will create a generator and provide assign
# this generator to a variable when it is called.
# Using the next() function will call the values that are generated in
# the generator.
# Generators can have a limit to how many values can be generated or
# it can generate infinite amount of values.
# The values generated are not stored anywhere but will be generated
# when the next() function is called to retrieve the value