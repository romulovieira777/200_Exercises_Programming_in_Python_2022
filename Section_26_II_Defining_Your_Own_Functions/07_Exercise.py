"""
Exercise No. 07

Implement a function count_str(), which returns the number of str objects in an iterable object (list, tuple, set).

Example:

    [IN]: count_str(['p', 2, 4.3, None])
    [OUT]: 1

    [IN]: count_str({'p', 4.3, True, 'True', None})
    [OUT]: 2

Note! You only need to define the function.
"""


# Solution I
def count_str(iterable):
    count = 0
    for i in iterable:
        if type(i) == str:
            count += 1
    return count


# Solution II
def count_str(items):
    total = 0
    for item in items:
        if isinstance(item, str):
            total += 1
    return total


print(count_str(['p', 2, 4.3, None]))
