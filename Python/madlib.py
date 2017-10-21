import re, shelve, pyperclip, sys

openText = open('C:\\MyPythonScripts\\madlibsource.txt')

readText = openText.read()
sourceText = readText.split()
print(sourceText)


libRegex = re.compile('Adjective|Noun|Verb', re.I)
wordList = libRegex.findall(readText)

for i in range(len(sourceText)):
    for j in range(len(wordList)):
        if wordList[j] in sourceText[i]:
            newWord = input('Please enter a ' + sourceText[i] + '\n')
            if '.' in sourceText[i]:
                sourceText[i] = newWord + '.'
            else:
                sourceText[i] = newWord


finalText = ' '.join(sourceText)

print(finalText)
