"""
Exercise No. 02

Write a program that calculates the future value of 1000 USD with an annual rate of 3%, annual capitalization and a
5-year investment period. Round the result to the nearest cent.

Tip: Use compound capitalization of interest.

Print the result to the console as show below.

Expected result:

    The future value of the investment: 1159.27 USD
"""
value = 1000
rate = 0.03
years = 5

future_value = value * (1 + rate) ** years

print(f'The future value of the investment: {future_value:.2f} USD')
