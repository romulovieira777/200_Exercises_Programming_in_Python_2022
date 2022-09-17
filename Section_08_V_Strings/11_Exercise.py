"""
Exercise No. 11

The following text is given:

    text = '340-23-245-235'

Using the appropriate method remove all dashes from the text. Print the result to the console.

Expected result:

    34023245235
"""
text = '340-23-245-235'

# Solution I
print(text.replace('-', ''))

# Solution II
print(''.join(text.split('-')))

# Solution III
print(''.join([i for i in text if i != '-']))

# Solution IV
print(''.join([i for i in text if i.isnumeric()]))

# Solution V
print(''.join([i for i in text if not i.isalpha() and not i.isspace() and not i == '-']))

# Solution VI
print(''.join([i for i in text if i.isnumeric() or i.isalpha()]))
