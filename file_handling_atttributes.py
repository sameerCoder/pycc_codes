# File handling attributes

fo = open ("abc.txt", "w")
print ( "Name of the file :",fo.name)
#fo.close()
print ( "Closed or not:", fo.closed)

print ( "Opening mode : ",fo.mode )


import os
#os.rename("newabc.txt","new2abc.txt")
os.remove("abc.txt")
print("Before chdir",os.getcwd())
#os.mkdir("Newdirectory")
os.chdir("Newdirectory")
print("After changing folder:",os.getcwd())
os.mkdir("newfolder")
print(os.rmdir("newfolder"))


