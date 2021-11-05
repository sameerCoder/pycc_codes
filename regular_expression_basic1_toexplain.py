

# compile fucntion in regular expression.

'''
str1="apple"

sentence = "apple is good for health."

if str1 in sentence:
    print("apple is present.")

else:
    print("apple is not present.")
'''
import re

str1="apple"
print(str1)
print(type(str1))

regular=re.compile(str1)
print(type(regular))


