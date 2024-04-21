a_string = "this is\na string split\t\tand tabbed"
print(a_string)

# This is a raw string
raw_string = r"this is\na string split\t\tand tabbed"
print(raw_string)

b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)

backslash_string = "this is a backslash \followed by some text"
print(backslash_string)

backslash_string = "this is a baclslash \\followed by some text"
print(backslash_string)

# Python is escaping with a backslash at the end,
# so it's not a complete string
# python raw string doesn't process it when 
# the backslash is at the end of the string
# error_string = r"this string ends with \"
error_string = r"this string ends with \\"      # this string is fixed

