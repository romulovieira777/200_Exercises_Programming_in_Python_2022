"""
Exercise No. 04

The following paths are given:

    path1 = 'youtube.com/watch?v=5EhRztVxums'
    path2 = 'google.com/search?q=car'

Using the appropriate method check if the paths referto YouTube (e.g. start with 'youtube'). Print the result to the
console as shown below.

Expected result:

    path1: True
    path2: False
"""
path1 = 'youtube.com/watch?v=5EhRztVxums'
path2 = 'google.com/search?q=car'

# Solution I
print(f"path1: {path1.startswith('youtube')}")
print(f"path2: {path2.startswith('youtube')}")

# Solution II
print(f"path1: {path1[:7] == 'youtube'}")
print(f"path2: {path2[:7] == 'youtube'}")

# Solution III
print(f"path1: {path1.split('.')[0] == 'youtube'}")
print(f"path2: {path2.split('.')[0] == 'youtube'}")
