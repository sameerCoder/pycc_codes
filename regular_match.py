# Regualr Expression
# Match () function .
# finding out the matching string .
#The group(n) method returns entire match or speicific subgroup n and groups() method returns all matching subgroups in a tuple or empty if there weren't any matches .

import re

line = "Python is fun language ."


#matchobj = re.match(r"fun", line , re.M | re.I)

matchobj = re.match(r"Python",line,re.M | re.I)

#matchobj = re.match(r" No Python is ",line,re.M | re.I)


if matchobj:

  print ( "match -- > matchobj.group()" , matchobj.group())
  print("Match Found.")

else:

  print ("No match !")
