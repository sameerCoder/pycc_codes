class school():
    def getschooldetail(self,schname):
        self.schname=schname


class student(school):
    def getstudentdetail(self,sname):
        self.sname=sname

class test(student):
    def getanddisplay(self,marks):
        self.marks=marks
        print(self.schname)
        print(self.sname)
        print(self.marks)

t1=test()
t1.getschooldetail('dav')
t1.getstudentdetail('sam')
t1.getanddisplay(200)
