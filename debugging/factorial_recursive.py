#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Recursively calculates the factorial of a given number.
        The factorial of a number n is the product of all positive
        integers less than or equal to n.

    Parameters:
        n (int): A non-negative integer whose factorial will be calculated.

    Returns:
        int: The factorial value of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Retrieve the number from the command-line argument,
# compute its factorial, and store the result in variable f
f = factorial(int(sys.argv[1]))

# Print the calculated factorial
print(f)