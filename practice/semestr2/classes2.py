class Sphere():
    def __init__(self, radius=1, coordinatex=0, coordinatey=0, coordinatez=0):
        self.radius = radius
        self.coordinatex = coordinatex
        self.coordinatey = coordinatey
        self.coordinatez = coordinatez
    def get_volume(self):
        volume = 4/3 * 3.14 * self.radius*self.radius*self.radius
        return volume
    def get_square(self):
        square = 4 * 3.14 * self.radius()*self.radius()
        return square
    def get_radius(self):
        return self.radius
    def get_center(self):
        return tuple([self.coordinatex, self.coordinatey, self.coordinatez])
    def set_radius(self, radius = 1):
        self.radius = radius
        return 0
    def set_center(self, coordinatex=0, coordinatey=0, coordinatez=0):
        self.coordinatex = coordinatex
        self.coordinatey = coordinatey
        self.coordinatez = coordinatez
        return 0
    def is_point_inside(self, coordinatex, coordinatey, coordinatez):
        if(-self.coordinatex-self.radius<coordinatex<self.coordinatex+self.radius)\
                and(-self.coordinatey-self.radius<coordinatey<self.coordinatey+self.radius)\
                and(-self.coordinatez-self.radius <= coordinatez <= self.coordinatez+self.radius):
            return True
        return False

s0 = Sphere(0.5) # test sphere creation with radius and default center
print(s0.get_center()) # (0.0, 0.0, 0.0)
print(s0.get_volume()) # 0.523598775598
print(s0.is_point_inside(0 , -1.5, 0)) # False
s0.set_radius(1.6)
print(s0.is_point_inside(0, -1.5, 0)) # True
print(s0.get_radius()) # 1.6

class SuperStr:
    def __init__(self, string):
        self.string = string
    def __call__(self, *args, **kwargs):
        return self.string
    def is_repeatance(self, string):
        try:
            string = str(string)
        finally:
            print()
        while True:
            if(len(string)>len(self.string)):
                return False
            elif(len(string)<len(self.string)):
                string = string + string
                continue
            elif(len(string)==len(self.string) and (string == self.string)):
                return True
            else:
                break
    def is_palindrom(self):
        if(self.string == self.string[::-1]):
            return True
        else:
            return False
    def __int__(self):
        return int(self.string)

s = SuperStr("123123123123")
print(s.is_repeatance("123")) # True
print(s.is_repeatance("123123")) # True
print(s.is_repeatance("123123123123")) # True
print(s.is_repeatance("12312")) # False
print(s.is_repeatance(123)) # False
print(s.is_palindrom()) # False
print(s) # 123123123123 (строка)
print(int(s)) # 123123123123 (целое число)
print(s() + "qwe") # 123123123123qwe
p = SuperStr("123_321")
print(p.is_palindrom()) # True