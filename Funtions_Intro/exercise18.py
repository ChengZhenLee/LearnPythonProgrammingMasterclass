def factorial(number: int) -> int:
    """
    Calculates the factorial of a number.

    Arguments:
        number -- The number whose factorial is calculated.

    Returns:
        The factorial of the number.
    """
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial


for i in range(0, 36):
    print("{0}  {1}".format(i, factorial(i)))