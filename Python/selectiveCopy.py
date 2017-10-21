#! python 3
# selectiveCopy.py - Write a program that walks through a folder tree
# and searches for files with a certain file extension. Copy these files
# from whatever location they are in to a new folder.

import zipfile, os, re, shutil

def selectiveCopy(folder, extension):
    # Create the new folder to copy into
    folder = os.path.abspath(folder)
    new_folder = folder + extension + ' files only'
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    # TODO: Search and copy files.
    for folderName, subfolders, filenames in os.walk(folder):
        print('Searching ' + folderName + ' for files with ' + extension + ' extension.')

        for subfolder in subfolders:
            print('Searching subfolder of ' + folderName + ': ' + subfolder)

            for filename in filenames:
                if extension in filename:
                    shutil.copy(filename, new_folder)
                    print('Copied ' + filename + ' to ' + new_folder)

selectiveCopy('C:\\testing', 'txt')
                    

        
