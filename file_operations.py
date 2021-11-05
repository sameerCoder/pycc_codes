# File Operation and Attribute2 .

'''
fo = open (" abc.txt", "w")
print ( "Name of the file :",fo.name)
#fo.close()
print ( "Closed or not:", fo.closed)

print ( "Opening mode : ",fo.mode )


##############################
#file.tell()
#tells the correct pointer location .
#!/usr/bin/python3

fo = open("ftell888.txt", "w+")
print ("Name of the file: ", fo.name)
fo.write("line write")
print(fo.tell())
fo.seek(3,0)
print(fo.tell())
line = fo.read()
#line = fo.readline()
print("line:",line)
print ("Read Line: %s" % (line))
print("file current location.")
fo.tell()
fo.seek(0,0) # After using this line it will go to 0 position.
            # in seek first value is pointer value .# second value always 0

pos=fo.tell()
print (" first current position : ",pos)

line1 = fo.readline()
print("line1 :",line1)
fo.seek(5,0)
pos1=fo.tell()
print (" second current position : ",pos1)
line2 = fo.readline()
print("line2 :",line2)


# Close opened file
fo.close()
'''

'''
############################

#question ?
#if fseek.txt is present,

#fseek.txt-
line1 - python is great.
line2 - java is also good.

#if fseekravi.txt is not present.

fo = open("fseek.txt", "r+")
foo=open("fseekravi.txt",'r') # File not found .
print("Name of the file: ", fo.name)
'''




# Seek operation .

fo = open("fseek.txt", "r+")
#foo=open("fseekravi.txt",'r') # File not found .
print("Name of the file: ", fo.name)


# Assuming file has following 5 lines
fo.write("This is 1st line \n")
fo.write("This is 2nd line\n")
fo.write("This is 3rd line\n")
fo.write("This is 4th line\n")
fo.write("This is 5th line\n")
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line
#fo.close()

line=fo.read(171)
#print("Read line: %s" % (line))

# Again set the pointer to the beginning
#fo.seek(0,0)# pointer will go to 0 byte i.e initial of file.
fo.seek(70,0) # pointer will go to 70 byte
line = fo.readline()
linebyte=fo.read(100) # This will read upto 100 byte
print("line :",line)
print ("Read Line: after seek %s" % (line))
print("Read by bytes value %s"%(linebyte))

# Close opend file
fo.close()


alllines=fo.readlines()
for particularline in alllines:
    print("current line:",particularline)
