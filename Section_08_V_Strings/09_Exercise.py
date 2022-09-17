"""
Exercise No. 09

The following text is given:

    text = "   Google Colab     "

Using the appropriate method remove whitespace characters around the text. Print the result to the console.

Expected result:

    Google Colab
"""
text = "   Google Colab     "

# Solution I
print(text.strip())

# Solution II
print(text.strip().lstrip().rstrip())
