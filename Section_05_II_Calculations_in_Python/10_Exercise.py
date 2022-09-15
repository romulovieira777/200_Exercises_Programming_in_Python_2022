"""
Exercise No. 10

Calculate the geometric mean of the following numbers: 4, 3, 4.5, 5 and print the result to the console as shown below.

Expected result:

    Geometric average of the given numbers: 4.5
"""
numbers = [4, 3, 4.5, 5]

product = 1
for number in numbers:
    product *= number

geometric_mean = product ** (1 / len(numbers))

print(f'Geometric average of the given numbers: {geometric_mean:.2f}')
