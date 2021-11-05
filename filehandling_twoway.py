# file handling.

# 2 ways to handle file in python
 #1-
fileobj=open("abc27777.txt","w")

lines=fileobj.readlines()

for l in lines:
    print("current line:",l)


fileobj.close()


#2 way of reading.
with open("abc2.txt","r") as fileob2:
    lines=fileob2.readlines()
    for l in lines:
        if l.startswith("P"):
            print("current:",l)

        
