# Regular Expression match function.

'''
# match function only check at the beginning by default.


import re

matches= re.match("python","python Wonderful language is python.")

if matches:
    print("matches are index :",matches.start())

else:
    print("matches are not found.")

'''
'''
# Fullmatch , complete string should match.

import re
matches=re.fullmatch("python","python")
if matches:
    print("Full String will be matched.")
else:
    print("Full string didn't matched.")
'''

'''
# search function only check at any place .
import re
matches=re.search("python","wonderful  language is python.")

if matches:
    print("matches are index:",matches.start())

else:
    print("matches are not found.")
'''


# findall method. # findall will return result as a list element.

import re
matches=re.findall("[0-9]","sa78ekj239k5,1")
if matches:
    print("matches are:{}".format(matches))
else:
    print("matches not found.")



