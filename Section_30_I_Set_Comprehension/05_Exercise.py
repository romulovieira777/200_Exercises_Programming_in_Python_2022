"""
Exercise No. 05

Calculate the probability than in three throws of symmetrical cubic dice, the sum of the squares of points will be
divisible by 3. Use set comprehension. Round the result to fourth decimal place and print the result to the console as
shown below.

Expected result:

    Probability: x.xxxx
"""

# Solution I
cubic = {x for x in range(1, 7)}
omega = {(x, y, z) for x in cubic for y in cubic for z in cubic}

a = {(x, y, z) for x, y, z in omega if (x ** 2 + y ** 2 + z ** 2) % 3 == 0}
probability = round(len(a) / len(omega), 4)

print(f'Probability: {probability}')


# Solution II
omega = {
    (i, j, k)
    for i in range(1, 7)
    for j in range(1, 7)
    for k in range(1, 7)
}

a = {
    (x, y, z)
    for x, y, z in omega
    if (x ** 2 + y ** 2 + z ** 2) % 3 == 0
}

probability = round(len(a) / len(omega), 4)

print(f'Probability: {probability}')
