"""
Exercise No. 06

We roll the symmetrical dice three times. Calculate the probability of the following:
    - A - odd number of points in each roll

Use set comprehension. Round the result to three decimal places and print the result to the console as shown below.

Expected result:

    Probability: 0.125
"""
roll = {x for x in range(1, 7)}
omega = {(x, y, z) for x in roll for y in roll for z in roll}
a = {(x, y, z) for x, y, z in omega if x % 2 != 0 and y % 2 != 0 and z % 2 != 0}
probability = round(len(a) / len(omega), 3)

print(f'Probability: {probability}')
