# File  close , write  and read operation .


fo = open ( "abc2.txt" ,"w")

fo.write ( " Programming with python is fun . \n let's try python \n")
print( " Two lines are written . By default file.write() don't contain new line .")


fo.close()

print ( " file is closed .")



