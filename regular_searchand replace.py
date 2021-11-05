# sub Regular Expression .

# SEarch and Replace .

import re

zipcode = "2004 -959-AAA559"

# Remove anything other than digits .

num=re.sub(r'\D',"*",zipcode)
print("zipcode :",num)

num2 =re.sub(r'\D',"*",zipcode,count=2)


# Here \D is Regular Expression Patterns which matches NONDigits.

print("zipcode :",num2)
