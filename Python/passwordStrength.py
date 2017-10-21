import pyperclip, re

PW = str(pyperclip.paste())

minCharRegex = re.compile(r'(\w){8,}')
upperCaseRegex = re.compile(r'[A-Z]+')
lowerCaseRegex = re.compile(r'[a-z]+')
digitRegex = re.compile(r'(\d)+')

charCheck = minCharRegex.search(PW)
upperCheck = upperCaseRegex.search(PW)
lowerCheck = lowerCaseRegex.search(PW)
digitCheck = digitRegex.search(PW)

if charCheck is None:
    print('This password is not long enough.')
elif upperCheck is None:
    print('This password has no uppercase characters.')
elif lowerCheck is None:
    print('This password has no lowercase characters.')
elif digitCheck is None:
    print ('This password has no digits.')
else:
    print('This is a strong password.')
    
