"""
Exercise No. 04

The following list is given:

    filenames = ['view.jpg', 'bear.jpg', 'ball.jpg']

Add the file 'phone.jpg' to this list at the beginning. Then delete the file 'ball.jpg'. In response, print the
filenames list to the console.

Expected result:

    ['phone.jpg', 'view.jpg', 'bear.jpg']
"""
filenames = ['view.jpg', 'bear.jpg', 'ball.jpg']

filenames.insert(0, 'phone.jpg')
filenames.remove('ball.jpg')
print(filenames)
