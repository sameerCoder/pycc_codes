
# File handling basic


fo=open("filename.txt","w")
fo.close()
##############

with open("secondway.txt","w") as fout:
    fout.write("hello")
