class school():
    def getschooldetail(self,schname):
        self.schname=schname


class student(school):
    def getstudentdetail(self,sname):
        self.sname=sname
        print("school name:",self.schname)
        print("student name:",self.sname)

class teacher(school):
    def getanddisplay(self,tname):
        self.tname=tname
        print(self.schname)
        print(self.tname)


t1=teacher()

t1.getschooldetail("DAV school") #parent function
t1.getanddisplay("Science Teacher")


s1=student()
s1.getschooldetail("DAV school")
s1.getstudentdetail("class2 student")

