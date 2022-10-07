"""
Exercise No. 01

Write a program that reads plaway.txt file containing Playway stock data, and then calculates the average closing price
(3-day average).

Print the resutl to the console as shown below.

Expected result:

    3-day average closing price:  xxx.xx
"""
# Solution I
with open("../Files/playway.txt") as f:
    lines = f.readlines()
    lines = lines[1:]
    closing_prices = []
    for line in lines:
        closing_prices.append(float(line.split(",")[4]))
    print(f'3-day average closing price: {sum(closing_prices) / len(closing_prices):.2f}')

# Solution II
with open("../Files/playway.txt") as file:
    lines = file.read().splitlines()

close = []
for idx, line in enumerate(lines):
    if idx > 0:
        continue
    close.append(int(line.split(",")[-2]))

close_avg = sum(close) / len(close)
print(f"3-day average closing price: {close_avg:.2f}")
