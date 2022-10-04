"""
Exercise No. 02

The list of names is given (one is missing):

    names = ['Jack', 'Leon', 'Alice', None, 'Bob']

Using the continue statement, print only the correct names to the console as shown below.

Expected result:

    Jack
    Leon
    Alice
    Bob
"""
names = ['Jack', 'Leon', 'Alice', None, 'Bob']

# Solution I

for name in names:
    if name is None:
        continue
    print(name)

# Solution II
for name in names:
    if not isinstance(name, str):
        continue
    print(name)
