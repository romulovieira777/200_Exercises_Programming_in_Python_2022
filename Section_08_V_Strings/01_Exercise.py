"""
Exercise No. 01

The following text is given:

    text = "python is a popular programing language."

Use the appropriate method to replace the first letter of the text with uppercase. Print the result to the console.

Expected result:

    Python is a popular programing language.
"""
text = "python is a popular programing language."

# Solution I
print(text.capitalize())

# Solution II
print(text[0].upper() + text[1:])

# Solution III
print(text.replace('p', 'P', 1))
