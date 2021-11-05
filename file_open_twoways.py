# Two ways to open the file by python .


fo=open("filename.txt","r")
fo.readline()
fo.close()

with open ("filename.txt","r") as fo:
    fo.readline()


    
