"""
Exercise No. 01

The following list of words is given:

    stocks = ['playway', 'boombit', 'cd projekt']

Using the map() fucntion and the lambda expression, transform the given list into a list containing the lengths of each
word and print it to the console.

Expected result:

    [7, 7, 10]
"""
stocks = ['playway', 'boombit', 'cd projekt']

# Solution I
print(list(map(lambda x: len(x), stocks)))


# Solution II
length = list(map(lambda stock: len(stock), stocks))
print(length)
