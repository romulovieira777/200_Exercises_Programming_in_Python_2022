"""
Exercise No. 06

The following tuple is given:

    techs = ('Python', 'Java', 'sql', 'aws')

Sort this tuple from a to z and print it to the console.

Tip: Tuples are immutable. You have to create a new one.

Expected result:

    ('aws', 'java', 'python', 'sql')
"""
techs = ('python', 'java', 'sql', 'aws')

# Solution 1
techs = list(techs)
techs.sort()
techs = tuple(techs)
print(techs)

# Solution 2
techs = ('python', 'java', 'sql', 'aws')
techs = tuple(sorted(techs))
print(techs)
