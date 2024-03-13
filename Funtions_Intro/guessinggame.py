import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin)
    The function will cotinue looping, and prompting
    the user, until a valid `int` is entered.

    Arguments:
        prompt -- The String that the user will see, when they're prompted to enter the value.

    Returns:
        The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{0} is not a valid number".format(temp))


help(get_integer)

highest = 10
# answer = 5
answer = random.randint(1, highest)
# print(answer)   # TODO: Remove after testing

print("Please guess number between 1 and {}: ".format(highest))
guess = "-"

# if guess == answer:
#     print("You got it first time")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:   # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")


# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    else:
        print("Well done, you guessed it")
        break
