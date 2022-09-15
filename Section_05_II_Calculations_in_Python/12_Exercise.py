"""
Exercise No. 12

Calculate the standard deviation (biased) of the following set of data: 10, 11, 9.

Print the result to the console as shown below.

Expected result:

    The standard deviation: 0.82
"""
number1 = 10
number2 = 11
number3 = 9

soma = number1 + number2 + number3
media = soma / 3
variancia = ((number1 - media) ** 2 + (number2 - media) ** 2 + (number3 - media) ** 2) / 3
desvio_padrao = variancia ** 0.5

print(f'The standard deviation: {desvio_padrao:.2f}')
