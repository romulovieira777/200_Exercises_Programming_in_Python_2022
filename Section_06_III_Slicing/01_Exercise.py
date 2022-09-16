"""
Exercise No. 01

From the given file name:

    filename = 'view.jpg'

extract extension and print it to the console.

Expected result:

    jpg
"""
filename = 'view.jpg'

# Solution I
print(filename.split('.')[1])

# Solution II
print(filename[-3:])

# Solution III
print(filename[filename.find('.')+1:])

# Solution IV
print(filename[filename.rfind('.')+1:])

# Solution V
print(filename[filename.index('.')+1:])

# Solution VI
print(filename[filename.rindex('.')+1:])

# Solution VII
print(filename[5:])
