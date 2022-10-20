"""
Exercise No. 04

Using the built-in module for regular expressions, find all digits in the following text:

    string = 'Python 3.8'

Print the result to the console.

Tip: Use the findall() function and the regular exprerssion '\d'.

Expected result:

    ['3', '8']
"""
import re

# Solution I
string = 'Python 3.8'
print(re.findall('\d', string))


# Solution II
string = 'Python 3.8'
result = re.findall(pattern=r'\d', string=string)
print(result)
