"""
Exercise No. 05

The following password is given:

    password = 'cskdnjcasa#!'

Check if the password has at least 11 characters and contains the special character '!'.

If so, print 'Password correct', otherwise 'Password too short'.

Expected result:

    Password correct
"""
password = 'cskdnjcasa#!'

# Solution 1
print('Password correct' if len(password) >= 11 and '!' in password else 'Password too short')

# Solution 2
if len(password) >= 11 and '!' in password:
    print('Password correct')
else:
    print('Password too short')
