"""
Exercise No. 06

Implement a function called factorial() that calculates the factorial for a given number.

Example:

    [IN]: factorial(6)
    [OUT]: 720

    [IN]: factorial(10)
    [OUT]: 3628800

Note! You only need to define the function.
"""


# Solution I
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Solution II
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(6))
