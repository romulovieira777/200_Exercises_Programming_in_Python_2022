"""
Exercise No. 02

Read the currencies.txt file. Each line has a different currencies pair. Create a list with the names of currency pairs
containing the 'USD' symbol.

Expected result:

    ['ARSUSD', 'AUDUSD']
"""
# Solution I
with open("../Files/currencies.txt") as file:
    lines = file.read().splitlines()
    currencies = []
    for line in lines:
        if "USD" in line:
            currencies.append(line)
    print(currencies)

# Solution II
with open("../Files/currencies.txt") as file:
    lines = file.read().splitlines()

indexes = [index for index in lines if "USD" in index]
print(indexes)
