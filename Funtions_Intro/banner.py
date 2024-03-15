def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    Print a string centered with ** on either side

    Keyword Arguments:
        text -- The string to print. An asterisk (*) will result in a row of 
        asterisks. The default will print a blank line, with a ** border at 
        the left and right edges. (default: {" "})

        screen_width -- The overall width to print within (including the 4 
        spaces for the ** either side). (default: {80})

    Raises:
        ValueError: If the supplied string is too long to fit
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))
    
    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)


banner_text("*", 60)
banner_text("Always look on the bright side of life...", 60)
banner_text("If life seems jolly rotten,", 60)
banner_text("There's something you've forgotten!", 60)
banner_text("And that's to laugh and smile and dance and sing,", 60)
banner_text(screen_width=60)
banner_text("When you're feeling in the dumps", 60)
banner_text("Don't be silly chumps,", 60)
banner_text("Just purse your lips and whistle - that's the thing!", 60)
banner_text("And... always look on the bright side of life...", 60)
banner_text("*", 60)

# Returns none as the function does not return any values
result = banner_text("Nothing is returned", 60)
print(result)

numbers = [4, 2, 7, 5, 8, 3, 9, 6, 1]
print(numbers.sort())