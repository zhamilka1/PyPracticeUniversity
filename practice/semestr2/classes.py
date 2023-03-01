class Student:
    name = 'Ivan'
    age = 18
    groupNumber = '10a'
    def __Init__(self, name, age, groupNumber):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGroupNumber(self):
        return self.groupNumber
    def setName(self, name):
        self.name=name
        return "New name is: %s" % self.name
    def setGroupNumber(self, groupNumber):
        self.groupNumber=groupNumber
        return f"New group number for {self.name} is: {self.groupNumber}"
Dolboeb = Student()
print(Dolboeb.setGroupNumber('idiot'))