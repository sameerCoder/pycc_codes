# File handling Byte File.


fileobj=open("image.jpg","rb")
filecontent=fileobj.read()

print(filecontent)

fileobj.close()


'''
with open("image.jpg",mode="rb") as file:
    filecontent=file.read()
    print(filecontent)
    
    

with open("creatingwrite.txt",mode='w+')as file2:
    filec=file2.write("This is first line.")
    print(file2.read())
'''
