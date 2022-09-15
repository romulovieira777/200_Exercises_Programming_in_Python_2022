"""
Exercise No. 11

An infinite geometric sequence is given with the following formula:

    1 + 1/2 + 1/4 + 1/8...

Calculate the sum of this sequence. Print the result to the console as show below.

Expected result:

    The sum of the sequence: 2.0
"""
a = 1
r = 1/2
n = 10

soma = (a * (r ** n - 1)) / (r - 1)

print(f'The sum of the sequence: {soma:.1f}')
