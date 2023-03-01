class Student:
    def __init__(self, name="Ivan", age = 18, groupNumber = "10a"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return "Student name is: %s" % self.name
    def getAge(self):
        return "Student age is: %s" % self.age
    def getGroupNumber(self):
        return "Student groupNumber is: %s" % self.groupNumber
    def setName(self, name):
        self.name=name
        return "New name is: %s" % self.name
    def setAge(self, age):
        self.age = age
        return "New age is: %s" % self.age
    def setGroupNumber(self, groupNumber):
        self.groupNumber=groupNumber
        return "New group number is: %s" % self.groupNumber

Johan = Student()
vika = Student("Victory", 23, "Pi3-1b")
sergey = Student("Sergay", 45, "ISIT4-4b")
victor = Student("Victor", 22, "Pi2-1b")
alex = Student("Alex", 18, "ISIT1-4b")
alina = Student("Alina", 67, "Pi10-1b")
zhamil = Student("Zhamil", 19, "ISIT44-1b")

print(Johan.setName("Johana"), Johan.setAge(41), Johan.setGroupNumber("FOP31-43b"))
print(sergey.getAge(), sergey.getName(), sergey.getGroupNumber())

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a+self.b
    def multiplication(self):
        return self.a*self.b
    def division(self):
        return self.a / self.b
    def substraction(self):
        return self.a-self.b

calc = Math(101,15)
print(calc.addition(),calc.multiplication(),calc.division(),calc.substraction())
class Car:
    color = "red"
    type = "hatchback"
    year = 1973
    isOn = False
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
    def start(self):
        if not self.isOn:
            self.isOn = True
            return "Vruuum"
        else:
            return "Engine already started"
    def stop(self):
        if self.isOn:
            self.isOn = False
            return "Shhhhhh"
        else:
            return "Engine already stopped"
    def setYear(self, year):
        self.year = year
        return "New year of production is %s" % self.year
    def setColor(self, color):
        self.color = color
        return "New color is %s" % self.color
    def setType(self, type):
        self.type = type
        return "New type is %s" % self.type

car = Car("anodised red", "supercar", "2022")
print(car.start(), car.start(), car.setYear('2020'), car.setColor('marine blue'), car.setType('hypercar'))