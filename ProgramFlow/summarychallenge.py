options = ["1.\tLearn Python", "2.\tLearn Java", "3.\tGo swimming", "4.\thave dinner", "5.\tGo to bed", "0.\tExit"]

choice = 6

while choice != 0:
    if 1 <= choice <= 5:
        print("You chose {}".format(options[choice - 1]))
    else:
        print("Choose an option from the list below: ")
        for option in options:
            print(option)
    choice = int(input("Enter an option: "))