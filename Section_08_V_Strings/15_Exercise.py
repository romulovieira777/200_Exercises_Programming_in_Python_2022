"""
Exercise No. 15

From the given url:

    url = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'

extract the slug after the last character '/'. The replace all dashes with spaces and print the result to the console as
shown below.

Expected result:

    sciezka data scientist machine learning engineer
"""
url = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'

# Solution I
print(url.split('/')[-1].replace('-', ' '))

# Solution II
print(url.rsplit('/', 1)[-1].replace('-', ' '))

# Solution
