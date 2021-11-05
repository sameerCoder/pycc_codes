# reading operation of file handling.

'''
file1=open("file1.txt","r")
lines=file1.readlines()
for l in lines:
    print(l)

file1.close()
'''

with open("file1.txt","r") as file1:
    lines=file1.readlines()
    for l in lines:
        print(l)

        
