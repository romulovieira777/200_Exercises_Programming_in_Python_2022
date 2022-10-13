"""
Exercise No. 08

The following list is given:

    items = ['P-1', 'R-2', 'D-4', 'F-6']

Using the map() and the lambda expression, get ride of the '-' (dash) from each element and print items list on the
console.

Expected result:

    ['P1', 'R2', 'D4', 'F6']
"""
items = ['P-1', 'R-2', 'D-4', 'F-6']

items = list(map(lambda x: x.replace('-', ''), items))
print(items)
