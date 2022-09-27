"""
Exercise No. 01

The following filename is given:

    filename = '01012020_sales.xlsx'

Check if the filename has the 'xlsx' extension. print to the console 'YES' if true, 'NO' if false.

Expected result:

    YES
"""
filename = '01012020_sales.xlsx'

# Solution 1
print('YES' if filename.endswith('.xlsx') else 'NO')

# Solution 2
if filename.endswith('.xlsx'):
    print('YES')
else:
    print('NO')
