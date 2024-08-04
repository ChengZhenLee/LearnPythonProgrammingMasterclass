area = 0
length = 30

def area_of_square():
    # Let python know that the variable area is a global variable
    global area
    area = length * length


area_of_square()
print(f'The area is {area}')