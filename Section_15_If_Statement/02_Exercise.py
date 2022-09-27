"""
Exercise No. 02

The following code is given:

    code = 'DSVNDOICSN'

Check if the code variable has only uppercase letters. If so, pront 'YES' to the console.

Expected result:

    YES
"""
code = 'DSVNDOICSN'

# Solution 1
print('YES' if code.isupper() else 'NO')

# Solution 2
if code.isupper():
    print('YES')
else:
    print('NO')
