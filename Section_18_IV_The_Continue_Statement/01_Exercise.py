"""
Exercise No. 01

The list of compaines from the WIG.GAMES index is given with the closing price and currency:

    gaming = {
        '11B': [362.5, 'PLN'],
        'CDR': [74.25, 'USD'],
        'CIG': [0.85, 'PLN'],
        'PLW': [79.5, 'USD'],
        'TEN': [300.0, 'PLN']
    }

Using the continue statement, create a for loop that will change the closing price from USD to PLN in this dictionary.

Take USDPLN = 4.0.

In response, print the gaming dictionary to the console.

Expected result:

    {'11B': [362.5, 'PLN'], 'CDR': [297.0, 'USD'], 'CIG': [0.85, 'PLN'], 'PLW': [318.0, 'USD'], 'TEN': [300.0, 'PLN']}
"""
gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}

# Solution I

USDPLN = 4.0

for key, value in gaming.items():
    if value[1] == 'USD':
        value[0] *= USDPLN
        continue

print(gaming)

# Solution II
for key, value in gaming.items():
    if value[1] == 'PLN':
        continue
    value[0] = value[0] * 4.0
    value[1] = 'PLN'

print(gaming)
