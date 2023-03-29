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
        return tuple(self.coordinatex, self.coordinatey, self.coordinatez)
    def set_radius(self, radius = 1):
        self.radius = radius
        return 0
    def set_center(self, coordinatex=0, coordinatey=0, coordinatez=0):
        self.coordinatex = coordinatex
        self.coordinatey = coordinatey
        self.coordinatez = coordinatez
        return 0
    def is_point_inside(self, coordinatex, cordinatey, coordinatez):
        if(-self.coordinatex<=coordinatex<=self.coordinatex):
            return 0