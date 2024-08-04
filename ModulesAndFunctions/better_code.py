def area_of_square(length: float) -> float:
    return length * length


# Check if this code is being run directly, or if it's imported as a module
# If it is imported as a module, the condition will be false
if __name__ == '__main__':
    area = area_of_square(30)
    print(f'The area is {area}')

    print(f'in better_code.py, __name__ is {__name__}')