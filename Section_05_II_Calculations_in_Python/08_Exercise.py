"""
Exercise No. 08

Calculate the distance of two points A = (3, 2). B = (-1, -1) and print result to the console as shown below.

Expected result:

    The distance between points A and B: 5.0
"""
a = (3, 2)
b = (-1, -1)

x = (a[0] - b[0]) ** 2
y = (a[1] - b[1]) ** 2

distance = (x + y) ** 0.5

print(f'The distance between points A and B: {distance}')
