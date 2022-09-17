"""
Exercise No. 02

The following text is given:

    text = "python is a popular programing language."

Using the appropriate method count the number of occurrents of the letter 'p' and print the result to the console as
show below.

Expected result:

    Number of occurrences: 4
"""
text = "python is a popular programing language."

# Solution I
print("Number of occurrences: {}".format(text.count('p')))

# Solution II
print("Number of occurrences: {}".format(len([i for i in text if i == 'p'])))

# Solution III
print("Number of occurrences: {}".format(text.count('p', 0, len(text))))

# Solution IV
print("Number of occurrences: {}".format(text.count('p', 0, len(text) - 1)))

# Solution V
print("Number of occurrences: {}".format(text.count('p', 0, len(text) - 2)))

# Solution VI
print("Number of occurrences: {}".format(text.count('p', 0, len(text) - 3)))

# Solution VII
print("Number of occurrences: {}".format(text.count('p', 0, len(text) - 4)))

# Solution VIII
print("Number of occurrences: {}".format(text.count('p', 0, len(text) - 5)))

# Solution IX
print("Number of occurrences: {}".format(text.count('p', 0, len(text) - 6)))

# Solution X
print("Number of occurrences: {}".format(text.count('p', 0, len(text) - 7)))

# Solution XI
print(f"Number of occurrences: {text.count('p')}")
