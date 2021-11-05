# File copying from one file to another file .


file1 = input ( " Enter the name of source file : ")
file2 = input ( "Enter the name of destination file :")

fileread = open (file1,"r")


filewrite =open ( file2, "w")

for line in fileread.readlines():
  filewrite.write(line)

print( "New file created and content copied .")
fileread.close()
filewrite.close()
