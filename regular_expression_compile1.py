# Regular Expression Compile function.

'''
################ Compile example #############
import re
#string1="python"
print("type('python'):",type("python"))
pattern=re.compile("python")
print("type(re.compile('python'))",type(pattern))
'''

'''
############################ re.finditer()###########

import re
pattern=re.compile("py")
count=0
allmatch=pattern.finditer("pythonispythonandgreatpython.")
for matchone in allmatch:
    count+=1
    print("matches are:",matchone)
    print("Start Index value of matchword is:",matchone.start())
    print("end Index value of matchword is:",matchone.end()-1)

print("")    
print("Total match found:",count)
'''
'''
######################START,END & GROUP WITH FORMAT ##################################
import re
pattern=re.compile("py")
count=0
allmatch=re.finditer(pattern,"pythonisgreatforpythoner")
for match in allmatch:
    count+=1
    print('start:{},end:{},group:{}'.format(match.start(),match.end()-1,match.group()))

print("Total match are:",count)
'''


# For having static pattern we can create string and store it
# But for dyanmic pattern like any lowercase alphabet , any digit present.
# any non digit number any symbol WE HAVE TO USE CHARACTER CLASSES.
# CHARACTER CLASSES BELOW.
#[abc] = select any a or b or c alphabet pattern in string .
#[^abc] = Except abc any other pattern to select.
#[0-9] = any digit select .
#[A-Z] = Uppercase A to Z any uppercase alphabet.
#[^0-9a-zA-Z] = select except any digit any alphabet i.e select symbol.

import re
#pattern=[abc]
matchabc=re.finditer("[abc]","apple is @ best for health.")
for m in matchabc:
    print(type(m))
    print("matches are:-",m.group())


'''
# PREDEFINE CHARACTER CLASSES BELOW .
\s = space character # to count how many space is there in sentence.
\S = Except space character .
\d = any digit = [0-9]
\D = Except digit select other alphabet & symbol. = [^0-9]
\w = word selection i.e select any alphabet , any digit . [0-9a-zA-Z]
\W = select symbol = [^0-9a-zA-Z]
. = select all the symbol , alphabet , digit.
'''

import re

matches=re.finditer("\w","This is python class \n 67we have89 great student.")
for m in matches:
    print(m.group())
    # Question put all the character in single line ?










