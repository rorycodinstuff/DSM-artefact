#imports
import re, shelve, pyperclip, sys, os

file_list = []
stored_text = []

# Get folder and user regex

folder_name = input('Enter a folder filepath. Add a slash at the end of the path.\n')
search_term = input('Enter an expression you wish to search for.\n')
sregex = re.compile(search_term, re.I)


# Check if folder exists

if os.path.isdir(folder_name) == False:
    print('The folder you specified does not exist.')
else:
    file_list = os.listdir(folder_name)

# Open all text files in folder, save to a list.

for file in file_list:
    file_path = os.path.join(folder_name, file)
    text = open(file_path).readlines()
    stored_text.insert(len(stored_text), text[0])


# Search for user supplied regular expression and print results

for i in range(len(stored_text)):
    mo = sregex.search(stored_text[i])
    if mo:
        print('"' + mo.group() + '" found in ' + file_list[i])


