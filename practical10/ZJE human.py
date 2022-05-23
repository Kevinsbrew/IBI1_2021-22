class Staff (object):
    def __init__(self,first_name,Last_name,location,role):
        self.f = first_name
        self.L =Last_name
        self.l =location
        self.r = role
    def print_flr (self):
     print("full name:",self.f,self.L,"location:",self.l,"role:",self.r)
Robert_Fripp = Staff("Robert","Fripp","International Campus","leadership")
print(Robert_Fripp.r)
print(Robert_Fripp.print_flr())