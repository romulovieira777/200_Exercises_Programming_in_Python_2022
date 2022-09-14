"""
Exercise No. 05

The geometric sequence is given with the following formula:

    an = 8 * 2^n - 1

Calculate the sum of the first six elements of this sequence. Print the result to the console as show below.

Expected result:

    The sum of the first 6 elements of the sequence is: 504.0
"""
a = 8
r = 2
n = 6

soma = (a * (r ** n - 1)) / (r - 1)

print(f'The sum of the first {n} elements of the sequence is: {soma}')
