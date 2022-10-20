"""
Exercise No. 07

Using the built-in module for regular expressions, split the following text by whitspace (spaces):

    text = 'Programming in Python - from A to Z'

Print the result to the console.

Tip: Use the re.split() function and the regular exprerssion '\s+'.

Expected result:

    ['Programming', 'in', 'Python', '-', 'from', 'A', 'to', 'Z']
"""
import re

# Solution I
text = 'Programming in Python - from A to Z'
print(re.split('\s+', text))


# Solution II
text = 'Programming in Python - from A to Z'
result = re.split(pattern=r'\s+', string=text)
print(result)
