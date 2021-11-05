# search and replace regular expression .
'''
import re

phone = "2004-959-559 before # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print ("Phone Num : ", num)

'''



import re

phone = "2004-959-559 before # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*', "", phone)
print ("Phone Num : after removing #", num)

# Remove anything other than digits
#count is used to give how many places you want to replace.
num = re.sub(r'\D', "", phone)   
num1 = re.sub(r'\D', "", phone,count=1)    
print ("Phone Num : ", num)
print ("Phone Num : ", num1)
