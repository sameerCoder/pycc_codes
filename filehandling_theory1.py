# File Handling theory.

'''
AS we want to do all our works through python programming skills ,
so the files or folder which are permentatly store in  our system
or in external storage should be operatored through our python coding.

i.e we can do all the operation of files & folder through our python
coding skills like reading , writing , appending , creating ,deleting etc
operation on files .
For folder we can create do operation like reading , renaming , creating ,
deleting etc to our folder .

This operations are known as file handling.

'''


# 2 ways of dealing with files through python.

#1 - way.
fileobj=open("varshita_uma2.txt","w+")
fileobj.writelines("\n")
fileobj.writelines("aline1")
fileobj.writelines("\n")
fileobj.writelines("aline2")

lines=fileobj.readlines()
for l in lines:
    print(l)
    
fileobj.close()


# 2 - way
with open("varshita_uma2way.txt","w+") as fileobj2:
    #fileobj2.readlines()
    fileobj.writelines("\n")
    fileobj.writelines("aline1")
    fileobj.writelines("\n")
    fileobj.writelines("aline2")
    







































