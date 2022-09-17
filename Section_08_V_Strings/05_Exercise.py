"""
Exercise No. 05

The following paths are given:

    path1 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
    path2 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-deep-learning-engineer'
    path3 = 'https://e-smartdata.teachable.com/p/sciezka-bi-analyst-data-analyst'

Using the appropriate method, find the word 'scientist' in the given paths, returning the index for the first letter of
the word. If the word is not in the path, the method should return -1. Print the result to the console as shown below.

Expected result:

    path1: 49
    path2: 49
    path3: -1
"""
path1 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
path2 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-deep-learning-engineer'
path3 = 'https://e-smartdata.teachable.com/p/sciezka-bi-analyst-data-analyst'

# Solution I
print(f"path1: {path1.find('scientist')}")
print(f"path2: {path2.find('scientist')}")
print(f"path3: {path3.find('scientist')}")

# Solution II
print(f"path1: {path1.index('scientist') if 'scientist' in path1 else -1}")
print(f"path2: {path2.index('scientist') if 'scientist' in path2 else -1}")
print(f"path3: {path3.index('scientist') if 'scientist' in path3 else -1}")

# Solution III
print(f"path1: {path1.index('scientist') if path1.find('scientist') != -1 else -1}")
print(f"path2: {path2.index('scientist') if path2.find('scientist') != -1 else -1}")
print(f"path3: {path3.index('scientist') if path3.find('scientist') != -1 else -1}")

# Solution IV
print(f"path1: {path1.index('scientist') if path1.count('scientist') != 0 else -1}")
print(f"path2: {path2.index('scientist') if path2.count('scientist') != 0 else -1}")
print(f"path3: {path3.index('scientist') if path3.count('scientist') != 0 else -1}")
