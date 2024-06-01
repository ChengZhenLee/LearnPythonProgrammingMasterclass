# In the section on Functions, we looked at 2 different ways to calculate the factorial
# of a number.  We used an iterative approach, and also used a recursive function.
#
# This challenge is to use the timeit module to see which performs better.
#
# The two functions appear below.
#
# Hint: change the number of iterations to 1,000 or 10,000.  The default
# of one million will take a long time to run.
 
import timeit
from statistics import mean, stdev

# fact_test = """\
# def fact(n):
#     result = 1
#     if n > 1:
#         for f in range(2, n + 1):
#             result *= f
#     return result

# x = fact(100)
# """

# factorial_test = """\
# def factorial(n):
#     # n! can also be defined as n * (n-1)!
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# y = factorial(100)
# """
    
# print(timeit.timeit(fact_test, number=10000))
# print(timeit.timeit(factorial_test, number=10000))

def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result

def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
if __name__ == "__main__":
    # We can directly write the 'string' code into the timeit function
    # and also pass the relevant function into setup from our __main__ program
    # in this case the 'timeitchallenge' file
    # print(timeit.timeit("x = fact(130)", setup="from __main__ import fact", number = 10000))
    # print(timeit.timeit("x = factorial(130)", setup="from __main__ import factorial", number = 10000))

    # use the repeat function to repeat the test multiple times
    list1 = timeit.repeat("x = factorial(130)", setup="from __main__ import factorial", number = 10000, repeat=6)
    list2 = timeit.repeat("x = factorial(130)", setup="from __main__ import factorial", number = 10000, repeat=6)

    # Calculate the mean and standard deviation of each list
    # from the statistics module
    print(mean(list1), stdev(list1))
    print(mean(list2), stdev)