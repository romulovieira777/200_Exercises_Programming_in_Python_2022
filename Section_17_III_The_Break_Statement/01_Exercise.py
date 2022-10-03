"""
Exercise No. 01

Write a program that compares two lists and returns True if the lists contain at least one of the same element.
Otherwise, it will return False.

Use break statement in the solution and print result to the console.

Lists:

    list1 = [1, 2, 0]
    list2 = [4, 5, 6, 1]

Expected result:

    True
"""
list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]

# Solution I
for element in list1:
    if element in list2:
        print(True)
        break
    else:
        print(False)
        break

# Solution II
for element in list1:
    if element in list2:
        result = True
        break

print(result)
