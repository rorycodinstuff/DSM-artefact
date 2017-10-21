import re

source = str('        aaaaaaaaWind your way around the wallaaaa        ')



def regexStrip(text, c=None):
    if c is None:
        regex = re.compile(r'^(\s)*|(\s)*$')
        newtext = regex.sub('', text)
        print(newtext)
    else:
        regex = re.compile(''+c+'*')
        newtext = regex.sub('', text)
        print(newtext)

regexStrip(source, 'aaaa')
        
