"""
Exercise No. 16

Dot product of vectors v, w:

    v = [v1,..., vn] e R^n
    w = [w1,..., wn] e R^n

We define as:

    v.w = v1w1 + v2w2 + ... + vnw1

Implement a function called dot_product() that takes two lists of the same length (vectors) and calculate the dot
product. We assume that the user gives a correctly defined vector.

Example:

    [IN]: dot_product([1, 2], [5, 2])
    [OUT]: 9

Note: You only need to implement this function.
"""


# Solution I
def dot_product(v, w):
    return sum([v[idx] * w[idx] for idx in range(len(v))])


# Solution II
def dot_product(v, w):
    return sum([v * w for v, w in zip(v, w)])
