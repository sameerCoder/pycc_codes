# different between write and append access mode.
''''
#write
with open("ashraf.txt","w") as ash:
    ash.writelines("This is line1\n This id line2 \n This is line3")
    list1=["11","22","3","4"]
    ash.write(str(list1)
    
'''

'''
with open("ashraf.txt","w") as ash:
    ash.writelines("This is singnal1\n This id singnal2 \n This is singnal3")
    list1=["1000","20000","3000","4000\n"]
    ash.write(str(list1))
'''

with open("ashraf.txt","a") as ash:
    ash.write("\n")
    ash.write("new data")
    ash.writelines("This is appendsingnal1\n This id appendsingnal2 \n This is appendsingnal3")
    list1=["ap1000","ap20000","ap3000","ap4000"]
    ash.write(str(list1))
