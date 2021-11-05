# Invoking the Base Class constructor .

class student(object):

  def __init__(self,id1,name):

    self.id1 = id1
    self.name = name

  def showstudent(self):

    print("Id is :",self.id1)
    print ("Name is:",self.name)


class Teacher (object):

  def __init__ (self ,tect_id,tect_name,subject ):
    

    self.tect_id = tect_id
    self.tect_name = tect_name
    self.subject = subject

  def showteacher (self):

    print ("tech id :",self.tect_id)
    print ("tech name :",self.tect_name)
    print ("tech subject :",self.subject)


class school ( Teacher , student ):

  def __init__ (self,id1,name,tect_id,tect_name,subject,school_id):

    student.__init__(self,id1,name)
    Teacher.__init__(self,tect_id,tect_name,subject)
    self.sch_id=school_id


  def showschool(self):
      print("Id of the school :",self.sch_id)


# Main start .

sc=school (10,"Rahul",111,"Kumar","Computer Science",80)
sc.showstudent()
sc.showteacher()
sc.showschool()









    












  
