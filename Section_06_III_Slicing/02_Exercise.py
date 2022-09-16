"""
Exercise No. 02

From the following text:

    string = 'PKV-89415-PLN'

extract the code containing the first three and last three characters. Print the result to the console.

Expected result:

    PKVPLN
"""
string = 'PKV-89415-PLN'

# Solution I
print(string[:3] + string[-3:])

# Solution II
solution = string[:3] + string[-3:]
print(solution)
