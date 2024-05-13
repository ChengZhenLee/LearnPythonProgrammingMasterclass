import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except EOFError:
            # Terminates the program with error code 1
            sys.exit(1)
        # Exception catches all exceptions
        except:
            print("Invalid number entered, please try again")
        # finally clause always comes after except clauses
        # always runs even if an exception is raised
        finally:
            print("The finally clause always executes")

first_number = getint("Please enter first number ")
second_number = getint("Please enter second number ")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("You can't divide by zero")
    # Terminates the program with error code 2
    sys.exit(2)
# else clause comes after except clause and before finally clause
# Only runs if no exceptions are raised
else:
    print("Division performed succesfully")
