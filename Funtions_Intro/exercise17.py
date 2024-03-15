def fizz_buzz(number: int) -> str:
    """
    Play Fizz Buzz

    Arguments:
        number: the number to check

    return:
        'fizz' if the number is divisible by 3
        'buzz' if the number is dividisble by 5
        'fizz buzz' if the number is divisible by 3 and 5
        the number if it is not divisible by either
    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)

# for i in range(1, 101):
#     print(fizz_buzz(i))

games = 1
input("Play Fizz Buzz.  Press ENTER to start")
print()
while games != 100:
    print("The number is {}".format(games))
    answer = fizz_buzz(games)
    guess = input("Please enter the 'fizz', 'buzz', 'fizz buzz' or the number: ")
    # guess = answer        for testing the code
    if guess == answer:
        games += 1
        # print(answer)     for testing the code
    else:
        print("That's not the answer! The correct answer was {}".format(answer))
        break
else:
    print("Well done, you reached {}".format(games))