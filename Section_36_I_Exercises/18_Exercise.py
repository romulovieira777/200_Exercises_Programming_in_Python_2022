"""
Exercise No. 18

Implement a function called top_n() which extracts top n largest values from the given list.

Arguments:
    - array - list of values
    - n - top elements to extract

Example:

    [IN]: top_n([4, 5, 2, 9, 5, 2, 8, 2, 8, 10], 3)
    [OUT]: [10, 9, 8]

Note: You only need to implement this function.
"""


# Solution I
def top_n(array, n):
    return sorted(array, reverse=True)[:n]


# Solution II
def top_n(array, n):
    array.sort(reverse=True)
    return array[:n]
