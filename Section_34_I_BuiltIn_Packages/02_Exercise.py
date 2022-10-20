"""
Exercise No. 02

Using the calendar built-in module, print a calendar for the June to the console.

Expected result:

        June 2020
    Mo Tu We Th Fr Sa Su
     1  2  3  4  5  6  7
     8  9 10 11 12 13 14
    15 16 17 18 19 20 21
    22 23 24 25 26 27 28
    29 30
"""
import calendar

# Solution I
print(calendar.TextCalendar().formatmonth(2020, 6))


# Solution II
print(calendar.month(2020, 6))
