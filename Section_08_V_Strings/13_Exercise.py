"""
Exercise No. 13

The following text is given:

    text = '''Python is a general-purpose language. Python is popular.'''

Using the appropriate method, split the text into setences. Print the result as a list to the console.

Expected result:

    ['Python is a general-purpose language.', 'Python is popular.']
"""
text = """Python is a general-purpose language. Python is popular."""

# Solution I
print(text.splitlines())