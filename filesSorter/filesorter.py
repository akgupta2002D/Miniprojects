import os
import shutil

# We need the path name of the directory that needs to get sorted.

path = 'C:/Users/ankit/Desktop/Downloads'

# The rest of the program to sort the above directory

# We need a list of filename that is there in the directory - path

listOfFileNames = os.listdir(path)

# Go through each and every file

for filename in listOfFileNames:
    # When used on os.path, splitext splits the extension of the file.
    name, ext = os.path.splitext(filename)
    # To see its output
    # print(ext)

    ext = ext[1:]
    # print(ext)

    # We need to skip it is a folder/directory
    if ext == '':
        continue

    # Move the file to the directory where the name of 'ext' already exists.
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+filename, path+'/'+ext+'/'+filename)

    # If the directory doesn't exist, make one and then move.
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+filename, path+'/'+ext+'/'+filename)
