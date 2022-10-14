"""
Exercise No. 03

Implement a generator named dayname() that accepts the index of the element from the following list:

    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

and allows us to iterate over 3 days (previous day, present day, next day).

Example:

    [IN]:
        for pair in dayname(0):
        print(pair)

    [OUT]:
        Sun
        Mon
        Tue

Note! All You have to do is define a generator.
"""


# Solution I
def dayname(index):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    yield days[index - 1]
    yield days[index]
    yield days[index + 1]


print(list(dayname(0)))


# Solution II
def dayname(index):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for i in range(index - 1, index + 2):
        yield days[i]


print(list(dayname(0)))


# Solution III
def dayname(index):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    yield days[index - 1]
    yield days[index]
    yield days[(index + 1) % 7]


print(list(dayname(0)))
