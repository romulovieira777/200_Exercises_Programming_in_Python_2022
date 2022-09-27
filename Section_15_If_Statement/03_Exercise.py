"""
Exercise No. 03

The following variable is given:

    number = 1.0

Test whether the variable is an instance of the built-in class int. Print 'YES' if true, 'NO' if false.

Expected result:

    NO
"""
number = 1.0

# Solution 1
print('YES' if isinstance(number, int) else 'NO')

# Solution 2
if isinstance(number, int):
    print('YES')
else:
    print('NO')
