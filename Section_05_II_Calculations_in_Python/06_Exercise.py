"""
Exercise No. 06

The quadratic equation is given with the following formula:

    x^2 + 5x + 4 = 0

Using Vieta's formulas calculate the sum and product of the roots of this equation. Print the result to the console as
show below.

Expected result:

    x1 + x2 = -5.0
    x1*x2 = 4.0
"""
x = 1
y = 5
z = 4

soma = -y / x
produto = z / x

print(f'x1 + x2 = {soma}\nx1x2 = {produto}')
