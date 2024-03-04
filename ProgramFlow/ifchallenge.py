name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if 18 <= age < 31:
    print("Welcome to the holiday, {}".format(name))
else:
    print("Sorry, you are not welcome to the holiday")