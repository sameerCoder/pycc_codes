# File create .

import os

fo=open("file22.txt","a")

# For creation we need to set write mode .
fo.write("\n")
fo.write("appendFirst line.\n")
fo.write("appendSecond line.")
print("name of file:",fo.name)
fo.close()
check_close=fo.closed
print("file closed or not :",check_close)

os.remove("file22.txt")
#print("file got deleted .")



#fo.close()
