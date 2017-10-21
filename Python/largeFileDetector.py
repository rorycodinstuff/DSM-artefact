#! python3
# largeFileDetector.py - Walks through a folder tree and searches for
# exceptionally large files or folders, prints absolute path of files
# to the screen.

import os, shutil

def findLargeFiles(folder):
    # os.path.getsize(path)
    for folderName, subfolders, files in os.walk(folder):
        print('Searching files in: ' + folderName)
        for file in files:
            name = os.path.join(folderName, file)
            if (os.path.getsize(name) > 10000000):
                print(name + ' is larger than 100MB.')
                
            
findLargeFiles(r'C:\Users\Rory\Documents\Allie Chapbook')
