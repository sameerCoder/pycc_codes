#Regular Expression Find all method ()

import re
a= "hello 23435324 world 787878 ok 1 ok 2332 alpha 8988 beta 9988jk "

print (re.findall (r"\d",a)) # Select only the each digit . ( for ex: ['2','3','4'])
print (re.findall ("\d+",a)) # Select each word of digits (continuous digits). ( for ex ['234']
# \d will find all the digits ,+ represents one or more previous characters .

'''
############################################
#list1=print (re.findall("\D+",a))
#####################
#\D+ search only the string values and give result.
list2=re.findall("\D+",a)
print("list2:",list2)
print ("list2:[2] ",list2[2])

#for i in list2:

  #print (i)
'''
