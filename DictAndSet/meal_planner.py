from contents import pantry, recipes


def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """
    Add to a dictionary of `item` some `quantity`

    Arguments:
        data -- The dictionary to be modified
        item -- The key in the dictionary
        amount -- The amount to be added to `item` key
    """
    # if item in data:
    #     data[item] += quantity
    # else:
    #     data[item] = quantity
    data[item] = data.setdefault(item, 0) + amount


# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

shopping_list = {}
while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")
    
    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients...")
        ingredients = recipes[selected_item]
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_list, food_item, quantity_to_buy)

for things, quantity in shopping_list.items():
    print(f"{things}: {quantity}")