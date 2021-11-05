# Regular expression basic

import re
line = "Catss s are smarter than dogs"
#matchobj1=re.match("smarter",line,re.I)
matchobj1=re.match("catss",line,re.I)
#print(matchobj1)

if matchobj1:
   print("match1:",matchobj1.group())

   
#matchObj = re.match( r'(.*) are (.*) ', line, re.M|re.I)
matchObj = re.match( r'(.*) smarter (.*?) .*', line, re.M|re.I)


if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
   # group 0= full line, 1= just left of pattern , 2= just right of pattern.
   
else:
   print ("No match!!")

