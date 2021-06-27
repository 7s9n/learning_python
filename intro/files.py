import os

#https://realpython.com/working-with-files-in-python/

# with open('../Desktop/c2.txt','r') as file:
#     content = file.read()
#     print(content)

# cnt = 0
# for dir , subdir , files in os.walk(os.getcwd()):
#     for file in files:
#         if file.endswith('.py'):
#             cnt += 1
#
# print(cnt)
# print(os.getcwd())
# with open('./intro/files.py','r') as file:
#     for line in file:
#         if not line.startswith('#') and line.strip():
#             print(line)

# with open ('../Desktop/output3.jpg','rb') as image:
#     content = image.read()
#     with open('./intro/img.jpg','wb') as out_image:
#         out_image.write(content)


# with open('../Desktop/test.txt','a') as test_file:
#     test_file.write('Hello , I\'m Hussein Sarea.\nHow are you\n')
#     test_file.write('\nEdited by: hussein sarea')

# cnt = 0
# for dir , subdirs , files in os.walk('../Desktop/tst'):
#     for file in files:
#         if file.endswith('.txt'):
#             with open(dir + '/' + file , 'a') as text_file:
#                 text_file.write('\nEdited by Hussein from python')
#             cnt += 1
#
# print(cnt)

# cnt = 0
# for dir , subdirs , files in os.walk('../Desktop'):
#     for file in files:
#         if file.endswith('.txt'):
#             cnt += 1
#
# print(cnt)

# Directory Listing in Legacy Python Versions
# In versions of Python prior to Python 3,
# os.listdir() is the method to use to get a directory listing:

# os.listdir() returns a Python list containing the names of the files and subdirectories in the directory given by the path argument:
print(os.listdir())

# A directory listing like that isn’t easy to read.
# Printing out the output of a call to os.listdir() using a loop helps clean things up:

entries = os.listdir('.') #current dir

for entry in entries:
    print(entry)

# Directory Listing in Modern Python Versions
# In modern versions of Python,
# an alternative to os.listdir() is to use os.scandir() and pathlib.Path().
#
# os.scandir() was introduced in Python 3.5 and is documented in PEP 471.
# os.scandir() returns an iterator as opposed to a list when called:

entries = os.scandir('.')
print(entries) #<nt.ScandirIterator object at 0x000001795350D7A0>

# The ScandirIterator points to all the entries in the current directory.
# You can loop over the contents of the iterator and print out the filenames:

with os.scandir('.') as entries:
    for entry in entries:
        print(entry.name)

# Here, os.scandir() is used in conjunction with the with statement
# because it supports the context manager protocol.
# Using a context manager closes the iterator ,
# and frees up acquired resources automatically after the iterator has been exhausted.
# The result is a print out of the filenames in my current directory just like in the os.listdir() example:

#Another way to get a directory listing is to use the pathlib module:

from pathlib import Path

#The objects returned by Path are either PosixPath or WindowsPath objects depending on the OS.
entries = Path('.')
for entry in entries.iterdir():
    print(entry.name)

# Listing All Files in a Directory

# List all files in a directory using os.listdir

for entry in os.listdir('.'):
    if os.path.isfile( os.path.join('.' , entry) ):
        print(entry)

# An easier way to list files in a directory is to use os.scandir() or pathlib.Path():

# List all files in a directory using scandir()
with os.scandir('.') as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)

# Here’s how to list files in a directory using pathlib.Path():

root = Path('.')

for file in root.iterdir():
    if file.is_file():
        print(file.name)

files_in_current_dir = [entry for entry in root.iterdir() if entry.is_file()]

print(files_in_current_dir) #[WindowsPath('test.txt')]

for file in files_in_current_dir:
    print(file.name)
