# Regular expression
# Both Match () and search ()

import re

line = "Python is fun programming language ."

matchobj = re.match(r"programming",line, re.M|re.I)

if matchobj:

  print ("match -->matchobj.group()",matchobj.group())

else:

  print ("No match ! from match func")

  searchobj=re.search(r"PRogramming",line,re.M|re.I)

  if searchobj:
    print(" search obj.search.group()",searchobj.group())
    print("Search function able to find the programming word.")

  else:
    print (" Word is not present in whole string. ")
