#Question 1- user should enter the readfilename ,
# check wheather the file is empty or not .

filename=input("Enter filename")
fileopen=open(filename,"w+")
lines=fileopen.readlines()

if len(lines)<=0:
    print("file is empty  .")

else:
    print("file is not empty ")
