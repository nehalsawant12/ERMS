class Employee:
    #constructor
    def __init__(self,eid="",ename="",esalary="",eimage = ""):
        self.eid = eid
        self.ename = ename
        self.esalary = esalary
        self.eimage =eimage


    # To convert object into string.
    def __repr__(self):
        return f'{self.eid} {self.ename} {self.esalary} {self.eimage}'