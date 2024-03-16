available_parts = [("computer", 2000),
                ("monitor", 150),
                ("keyboard", 70),
                ("mouse", 30),
                ("mouse mat", 20),
                ("hdmi cable", 10),
                ("dvd drive", 5)
                ]
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = [] # create an empty list

available_parts.sort()

total_price = 0

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index][0]
        chosen_price = available_parts[index][1]
        if chosen_part in computer_parts:
            # it#s already in, so remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
            total_price -= chosen_price
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
            total_price += chosen_price
        print("Your list now contains: {}".format(computer_parts))
        print("The total price is: {}".format(total_price))
    else:
        print("Please add options from the list below: ")
        for number, (part, price) in enumerate(available_parts):
            print("{0}: {1:20} {2}".format(number + 1, part, price))
        print("0: to finish")

    current_choice = input()

print(computer_parts)
print(total_price)
