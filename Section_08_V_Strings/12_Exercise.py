"""
Exercise No. 12

The following text is given:

    text = 'Open,High,Low,Close'

Using the appropriate method split the text by comma. Print the result as a list to the console as shown below.

Expected result:

    ['Open', 'High', 'Low', 'Close']
"""
text = 'Open,High,Low,Close'

# Solution I
print(text.split(','))

# Solution II
print([i for i in text.split(',')])

# Solution III
print([i for i in text.split(',') if i])

# Solution IV
print([i for i in text.split(',') if i != ''])

# Solution V
print([i for i in text.split(',') if i.isalpha()])

# Solution VI
print([i for i in text.split(',') if not i.isnumeric()])

# Solution VII
print([i for i in text.split(',') if not i.isnumeric() and not i.isspace()])

# Solution VIII
print([i for i in text.split(',') if not i.isnumeric() and not i.isspace() and not i == ''])

# Solution IX
print([i for i in text.split(',') if not i.isnumeric() and not i.isspace() and not i == '' and not i == ','])

# Solution X
print([i for i in text.split(',') if not i.isnumeric() and not i.isspace() and not i == '' and not i == ',' and not i == ' '])
