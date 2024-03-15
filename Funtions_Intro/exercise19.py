def sum_numbers(*numbers: float) -> float:
    """
    Sums up all the numbers.

    Returns:
        The sum of all the numbers.
    """
    total = 0
    
    for i in numbers:
        total += i
    
    # Solution using builtin functions
    # total = sum(numbers)
    
    return total


print(sum_numbers(1, 2, 3))            # 6
print(sum_numbers(8, 20, 2))           # 30
print(sum_numbers(12.5, 3.147, 98.1))  # 113.747
print(sum_numbers(1.1, 2.2, 5.5))      # 8.8