# File readline .


#fo=open("511lines.txt","w")
fo=open("51lines.txt","a+")

print("Name of the file :",fo.name)
#print("pointer using write: ",fo.tell())

print("pointer using append: ",fo.tell())
#fo.seek(0,0)

str1=" This is line 1W. \n"
str2=" This is line 2W. \n"
str3=" This is line 3W. \n"

line=fo.write(str1)
line=fo.write(str2)
line=fo.write(str3)
current_location=fo.tell()
print("Current location of file :",current_location)
fo.seek(10,0)
print("After seek pointer place at :",fo.tell())
fo.write("Writting after going 10 seek pointer jjkjjjkjkjkjkjk")

fo.close()


'''
#####################################################
# Appending line at the last.
#append1="append line ."
#line=fo.write(append1)
#fo.close()


'''

###################################################
#File Reading Operations . 
# File reading .
fo=open("5lines.txt","r")
readline=fo.readlines()

#print(readline,end=" ")
for i in range(0,len(readline)):
  print (readline[i])
#print(readline[2])

fo.close()


