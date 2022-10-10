"""
Exercise No. 07

Count the number of ones in the binary representation of number:

    number = 234

Print the result to the console.

Tip: Use the bin() built-in function.

Expected result:

    5
"""
number = 234

# Solution I
print(bin(number).count('1'))

# Solution II
binary = bin(number)
binary = binary[2:]

print(binary.count('1'))
