"""
Exercise No. 02

The following list of hashtags is given:

    hashtags = ["holiday", "sport", "fit", None, "fashion"]

Check if all objects in the list are of str type. If so, print True, otherwise print False. Use the break statement in
your solution.

Expected result:

    False
"""
hashtags = ["holiday", "sport", "fit", None, "fashion"]

# Solution I
for hashtag in hashtags:
    if type(hashtag) != str:
        print(True)
        break
    else:
        print(False)
        break

# Solution II
for hashtag in hashtags:
    if not isinstance(hashtag, str):
        result = True
        break

print(result)
