"""
Exercise No. 07

The follwoing dictionary is given:

    project_ids = {'01': 'open', '02': 'new', '03': 'in progress', '04': 'completed'}

Using the conditional statement, check if the project status with id = '02' is set to 'new'. If so, change its status
to 'open' and print the dictionary to the console.

Expected result:

    {'01': 'open', '02': 'open', '03': 'in progress', '04': 'completed'}
"""
project_ids = {'01': 'open', '02': 'new', '03': 'in progress', '04': 'completed'}
project_id = '02'

# Solution 1
if project_ids[project_id] == 'new':
    project_ids[project_id] = 'open'
print(project_ids)

# Solution 2
if project_ids['02'] == 'new':
    project_ids['02'] = 'open'
print(project_ids)
