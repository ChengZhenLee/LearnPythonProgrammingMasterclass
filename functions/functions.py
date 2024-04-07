def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


# def centre_text(*args, sep=' ', end='\n', file=None, flush=False):
def centre_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    # print(" " * left_margin, text, end=end, file=file, flush=flush)
    return " " * left_margin + text


# with open("centred", mode="w") as centred_file:

# # call the function
#     # python_food()
#     centre_text("spam and eggs", file=centred_file)
#     centre_text("spam, spam and eggs", file=centred_file)
#     centre_text(12, file=centred_file)
#     centre_text("spam, spam, spam and spam", file=centred_file)

#     # print("first", "second", 3, 4, "spam")
#     centre_text("first", "second", 3, 4, "spam", sep=':', file=centred_file)

with open("menu", "w") as menu:
    s1 = (centre_text("spam and eggs"))
    print(s1, file=menu)
    s2 = (centre_text("spam, spam and eggs"))
    print(s2, file=menu)
    print(centre_text(12), file=menu)
    print(centre_text("spam, spam, spam and spam"), file=menu)
    s5 = (centre_text("first", "second", 3, 4, "spam", sep=':'))
    print(s5, file=menu)

print("m" + str(12 * 3))
print(sorted(["b", "d", "c", "a"]))