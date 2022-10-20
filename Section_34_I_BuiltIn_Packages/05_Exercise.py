"""
Exercise No. 05

Using the built-in module for regular expressions, find all alphanumeric characters in the following text:

    string = '!@#$%^&45wc'

Print the result to the console.

Tip: Use the findall() function and the regular exprerssion '\w'.

Expected result:

    ['4', '5', 'w', 'c']
"""
import re

# Solution I
string = '!@#$%^&45wc'
print(re.findall('\w', string))


# Solution II
string = '!@#$%^&45wc'
result = re.findall(pattern=r'\w', string=string)
print(result)
