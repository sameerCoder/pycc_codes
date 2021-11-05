# Dictionary


dict1={'a':10,'b':100,'c':78}


#print("Original dictionary :",dict1)
#print("all keys :",dict1.keys())
#print("all values :",dict1.values())
#print("Dictionary items :",dict1.items())

#print("has key :",dict1.has_key('a'))#### it was working in python 2.7



#exit()

dict2={'aa': 100, 'key2': [3,30]}
#print("Original dictionary 2 :",dict2)


dict3={'[a,3]':200}
#print(dict3.keys())
#print(dict3.values())
#print("Original dictionary 3 :",dict3)


#setting default.

dict11={'Name:':'Tom'}
#print(dict11.setdefault('Name:'))
print(dict11.setdefault('Phone',0)) # dict11={'Phone':0}
#print(dict11.setdefault('address')) # None as value as i didn't initiated it. 
#print(dict11.keys())
#print(dict11.values())
#print(dict11.items())

# Adding the key and value pair in existing dictionary.
dict11['newkey4']=25

print("After adding new key dict11['newkey4']=25 ",dict11.items())
dict11['newkey4']=15

print("After doing dict11['newkey4']=15 ",dict11.items())


# CReated one more key phone and setting default value 0

#print(dict11.keys())
#print(dict11.values())
print(dict11['Name:'])
print(dict11['Phone'])


#print(dict11.items())

# Adding the key and value pair in existing dictionary.




# Making dictionary from List.

list1 = ['Name1','Age','Height']
dictlist=dict.fromkeys(list1)
print(dictlist.items())
dictlist['Name1']="Python"
dictlist['Age']=22
dictlist['Height']=6.2

print(dictlist.items())


'''
'''

'''
# Making dictionary from List.

list1 = ['Name1','Age','Height']
dictlist=dict.fromkeys(list1)
print(dictlist.items())

dictlist['Name1']="Python"
dictlist['Age']=22
dictlist['Height']=6.2

print(dictlist.items())
'''
