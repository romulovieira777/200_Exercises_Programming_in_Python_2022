"""
Exercise No. 03

From the following text:

    string = '1 0 0 1 0 1'

remove spaces using slicing. Then convert the result to decimal notation and print it to the console.

Expected result:

    Number found: 37
"""
string = '1 0 0 1 0 1'

# Solution I
solution = string.replace(' ', '')
solution = int(solution, 2)

print(f'Number found: {solution}')

# Solution II
solution = string.split(' ')
solution = ''.join(solution)
solution = int(solution, 2)

print(f'Number found: {solution}')

# Solution III
binary = string[::2]
number = int(binary, 2)
print(f'Number found: {number}')
