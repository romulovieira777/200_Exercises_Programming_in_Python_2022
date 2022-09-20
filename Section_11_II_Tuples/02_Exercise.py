"""
Exercise No. 02

The following tuple is given:

    dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
    dji2 = ('HD.US', 'GS.US', 'NKE.US')

Nest these tuples into one tuple as shown below and print the result to the console.

Expected result:

    (('AAPL.US', 'IBM.US', 'MSFT.US'), ('HD.US', 'GS.US', 'NKE.US'))
"""
dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
dji2 = ('HD.US', 'GS.US', 'NKE.US')

combine = (dji1, dji2)
print(combine)
