"""
Exercise No. 01

Write a program that prints to the console the first ten prime numbers separated by a comma.

Tip: Use a while loop with break statement.

Expected result:

    2, 3, 5, 7, 11, 13, 17, 19, 23, 29
"""
counter = 0
numbers = 2
prime_numbers = []

while counter < 10:
    for i in range(2, numbers):
        if numbers % i == 0:
            break
    else:
        prime_numbers.append(str(numbers))
        counter += 1
    numbers += 1

print(','.join(prime_numbers))
