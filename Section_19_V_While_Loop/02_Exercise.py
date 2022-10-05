"""
Exercise No. 02

Using the while loop, calculate how many years you have to wait for the return on the investiment describeb below to at
least double (we only into account full periods).

Description:

    n - number of periods (in years).
    pv - present value.
    r - interest rate (annual).
    fv - future value.

Investiment parameters:

    pv = 1000
    r = 0.04

Print result to the console as shown below.

Expected result:

    Future value: 2025.82 USD. Number of periods: 18 years.
"""
pv = 1000
r = 0.04
fv = pv * (1 + r)
n = 1

while fv <= 2000:
    fv = fv * (1 + r)
    n += 1

print(f'Future value: {fv:.2f} USD. Number of periods: {n} years.')
