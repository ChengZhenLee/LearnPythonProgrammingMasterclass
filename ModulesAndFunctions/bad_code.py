area = 0

def area_of_square(length: float):
    # Let python know that the variable area is a global variable
    global area
    area = length * length


area_of_square(30)
print(f'The area is {area}')