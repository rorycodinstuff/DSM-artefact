spam = ['apples', 'bananas', 'tofu', 'cats']

def commaCode(aList):
    for i in range(len(aList)):
        if (i == len(aList) - 1):
            print('and ' + aList[i])
        else:
            print(aList[i] + ', ', end="")

commaCode(spam)

