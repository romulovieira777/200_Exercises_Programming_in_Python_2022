"""
Exercise No. 03

Consider the two-roll of the dice. Create the probability space (omega) and calculate the probability of getting a sum
of squares higher or equal to 45. Use set comprehension. Round the rsult to two decimal places and print the result to
the console as shown below.

Expected result:

    Probability: 0.22
"""

# Solution I
omega = {(x, y) for x in range(1, 7) for y in range(1, 7)}
a = {(x, y) for x in range(1, 7) for y in range(1, 7) if x ** 2 + y ** 2 >= 45}
probability = len(a) / len(omega)

print(f"Probability: {probability:.2f}")


# Solution II
omega = {(i, j) for i in range(1, 7) for j in range(1, 7)}
a = {(x, y) for x, y in omega if x ** 2 + y ** 2 >= 45}
probability = round(len(a) / len(omega), 2)

print(f'Probability: {probability}')
