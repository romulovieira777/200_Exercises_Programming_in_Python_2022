"""
Exercise No. 03

The following text is given:

    text = 'Python programming'

Standardize the text (replace uppercase letters with lowercase). Then create a list of unique characters in the text.
Remove the space from this list and sort from a to z. After all print the result to the console.

Tip: You can use a set to generate unique characters.

Expected result:

    ['a', 'g', 'h', 'i', 'm', 'n', 'o', 'p', 'r', 't', 'y']
"""
text = 'Python programming'

# Solution 1
text = text.lower()
text = set(text)
text = list(text)
text.remove(' ')
text.sort()
print(text)

# Solution 2
text = 'Python programming'
text = text.lower()
characters = list(set(text))
characters.remove(' ')
characters.sort()
print(characters)
