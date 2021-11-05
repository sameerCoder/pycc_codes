# File readline .

############## File creating and printing name of file .
fo=open("5lines.txt","w")
#fo=open("5lines.txt","a")

print("Name of the file :",fo.name)

'''
##################### Whole lines of files are reading .
# File reading .
fo=open("5lines.txt","r")
readline=fo.readlines()

#print(readline,end="")

for i in readline:
  print (i)

'''

  

#fo.seek(0,0)

####################### File writting operation .
str1=" This is line 1. \n"
str2=" This is line 21. \n"
str3=" This is line 31. \n"
str4=" This is line 41. \n"

line=fo.write(str1)
print("number of character in line1 ",line)
line=fo.write(str2)
line=fo.write(str3)
line=fo.write(str4)
print("number of character in lineend ",line)



#####################################################
# Appending line at the last.
append1="append line3 \n ."
line=fo.write(append1)


fo.close()
