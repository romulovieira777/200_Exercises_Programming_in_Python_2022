"""
Exercise No. 06

The following list is given:

    stocks = [
        {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
        {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
        {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
    ]

Extract compaines from the 'mWIG40' index and print to the console.

Formatted result:

    [
        {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
        {'index': 'mWIG40', 'name': 'PLW', 'price': 309}
    ]

Expected result:

    [
        {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
        {'index': 'mWIG40', 'name': 'PLW', 'price': 309}
    ]
"""
stocks = [
    {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
]

mwig40 = list(filter(lambda x: x['index'] == 'mWIG40', stocks))
print(mwig40)
