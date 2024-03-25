# equation = bytes((207, 128, 114, 194, 178))

# Defines a bytes object
# '\x' means the following character is in hex
# r is 114 in ASCII - or \x74
equation = b'\xcf\x80r\xc2\xb2'
print(equation)
print(type(equation))
print(len(equation))

# Python decodes the bytes into strings
for b in equation:
    print(b, end=', ')
print()

print(equation.decode('utf-8'))