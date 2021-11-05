# Hierachical inheritance.


class school():
    def getdata(self,schoolname):
        self.schoolname=schoolname



class student(school):
    def getstudentdata(self,roll):
        self.roll=roll
        print("roll:",self.roll)
        print("my schoolname inside student:",self.schoolname)



class teacher(school):
    def getteacherdata(self,teachid):
        self.teachid=teachid
        print(self.schoolname)


schoolname=school()
schoolname.getdata("JNTU")
stud1=student()
stud1.getdata("JNTU")
stud1.getstudentdata(4)
tech1=teacher()
tech1.getdata("JNTU")
tech1.getteacherdata(78)







        
