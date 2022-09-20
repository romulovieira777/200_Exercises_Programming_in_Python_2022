"""
Exercise No. 05

Sort the given tuple (from A to Z):

    names = ('Monica', 'Tom', 'John', 'Michael')

Print the sorted tuple to the console as shown below.

Expected result:

    ('John', 'Michael', 'Monica', 'Tom')
"""
names = ('Monica', 'Tom', 'John', 'Michael')

# Solution 1
print(tuple(sorted(names)))

# Solution 2
sorted_names = tuple(sorted(names))
print(sorted_names)
