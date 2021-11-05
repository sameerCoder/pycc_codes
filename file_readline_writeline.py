# File operation with reading each line and writing each line .

'''
 #First file creation and writting .
fo = open ( "first31.txt ", "w")

#fo=open("first.txt","r+")

seq= [ "First Line \n ", "Second Line \n" , "Third Line \n" ,"Fourth Line \n " ]
#,"Fifth line \n "\n,"sixth line "\n , "seventh line \n"]

fo.writelines(seq)

fo.close()
'''



# Open the file in read mode .

fo = open ("first31.txt" , "r")

#lines=fo.readlines()

#print("readlines():",lines)

line1=fo.readline()
print("readline():",line1)

#Below line of code will go to next line and will read how many characters to read.
line2=fo.readline(5)

print("readlines(1):",line2)

# close of the file .
fo.close()

