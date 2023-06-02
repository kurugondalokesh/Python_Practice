class Python:
    # def __init__(self,t1,t2):
    #     self.t1=t1
    #     self.t2=t2
    def pd(self):
        print('datatypes')
        print('oops')
class HTML:
    # def __init__(self,t1,t2):
    #     self.t1=t1
    #     self.t2=t2
    def hd(self):
        print('forms')
        print('tables')
class Student(Python, HTML):
    def __init__(self,name,id):
        # Python.__init__(self,'oops','datatypes')
        # HTML.__init__(self,'forms','tables')
        self.name=name
        self.id=id
    def det(self):
        print(self.name)
        print(self.id)
stu1=Student('loki',1231)
stu1.pd()
stu1.hd()