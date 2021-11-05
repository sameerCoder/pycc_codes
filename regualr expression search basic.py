# Regular expression search basic

import re

line = "Cats are smarter than dogs";

searchObj = re.search( r' are ', line, re.M|re.I)
searchObj = re.search( r'(.*) are (.*?) (.*)', line, re.M|re.I)

if searchObj:
   print ("searchObj.group() : ", searchObj.group())
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))
   print ("searchObj.group(3) : ", searchObj.group(3))
else:
   print ("Nothing found!!")
 

'''
#################################33
   # matching vs searching .

import re

line = "Cats are smarter than dogs";

matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
   print ("search --> searchObj.group() : ", searchObj.group())
else:
   print ("Nothing found!!"   )
'''
