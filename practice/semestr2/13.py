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

#s0 = Sphere(0.5) # test sphere creation with radius and default center
#print(s0.get_center()) # (0.0, 0.0, 0.0)
#print(s0.get_volume()) # 0.523598775598
#print(s0.is_point_inside(0 , -1.5, 0)) # False
#s0.set_radius(1.6)
#print(s0.is_point_inside(0, -1.5, 0)) # True
#print(s0.get_radius()) # 1.6

class SuperStr(str):
    def __init__(self, string):
        self.string = string
    def is_repeatance(self, string):
        if not (isinstance(string, str)):
            return False
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

#s = SuperStr("123123123123")
#print(s.is_repeatance("123")) # True
#print(s.is_repeatance("123123")) # True
#print(s.is_repeatance("123123123123")) # True
#print(s.is_repeatance("12312")) # False
#print(s.is_repeatance(123)) # False
#print(s.is_palindrom()) # False
#print(s) # 123123123123 (строка)
#print(int(s)) # 123123123123 (целое число)
#print(s + "qwe") # 123123123123qwe
#p = SuperStr("123_321")
#print(p.is_palindrom()) # True

class Cell:
    def __init__(self, coordinate):
        self.coordinate = coordinate
        self.value = 0
    def makeVisited(self, playerNumber):
        self.value = playerNumber

class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class Board:
    def __init__(self):
        self.cells = []
        for i in range(0,9):
            self.cells.append(Cell(i))
            self.cells[i].value = 0
    def showCells(self, *args, **kwargs):
        values = ['■' for i in range(0,9)]
        i = 0
        for i in range(0,9):
            if (self.cells[i].value == 1):
                values[i] = 'o'
            elif (self.cells[i].value == 2):
                values[i] = 'x'

        print(f"{values[0]}|{values[1]}|{values[2]} 1 2 3")
        print(f"{values[3]}|{values[4]}|{values[5]} 4 5 6")
        print(f"{values[6]}|{values[7]}|{values[8]} 7 8 9")
    def visitCell(self, cellCoordinate, playerNumber):
        if(self.cells[cellCoordinate].value == 0):
            self.cells[cellCoordinate].makeVisited(playerNumber)
    def allCellAreNotVisited(self):
        for cell in self.cells:
            if(cell.value == 0):
                return True
        return False
    def winCheck(self, playerNumber):
        if (self.cells[0].value==playerNumber) and (self.cells[4].value==playerNumber) and (self.cells[8].value==playerNumber):
            return True
        elif (self.cells[2].value==playerNumber) and (self.cells[4].value==playerNumber) and (self.cells[6].value==playerNumber):
            return True
        elif (self.cells[0].value==playerNumber) and (self.cells[3].value==playerNumber) and (self.cells[6].value==playerNumber):
            return True
        elif (self.cells[1].value == playerNumber) and (self.cells[4].value == playerNumber) and (self.cells[7].value == playerNumber):
            return True
        elif (self.cells[2].value==playerNumber) and (self.cells[5].value==playerNumber) and (self.cells[8].value==playerNumber):
            return True
        elif (self.cells[0].value == playerNumber) and (self.cells[1].value == playerNumber) and (self.cells[2].value == playerNumber):
            return True
        elif (self.cells[3].value == playerNumber) and (self.cells[4].value == playerNumber) and (self.cells[5].value == playerNumber):
            return True
        elif (self.cells[6].value == playerNumber) and (self.cells[7].value == playerNumber) and (self.cells[8].value == playerNumber):
            return True
        else:
            return False
    def getUnVisitedCells(self):
        for cell in self.cells:
            if cell.value == 0:
                return cell.coordinate

board = Board()
whatGame = int(input('Do you wanna play with bot(1) or 2 players(2)'))
if(whatGame == 1):
    playerFirst = Player('zhamilka', 1)
    playerSecond = Player('alexa', 2)
    board.showCells()
    while board.allCellAreNotVisited():
        firstPlayerMove = int(input("Type your cell from 1 to 9 Zha"))
        board.visitCell(firstPlayerMove-1, playerFirst.number)
        if(board.winCheck(playerFirst.number)):
            print(f"{playerFirst.name} win!")
            break
        board.showCells()
        secondPlayerMove = board.getUnVisitedCells()
        board.visitCell(secondPlayerMove, playerSecond.number)
        if (board.winCheck(playerSecond.number)):
            print(f"{playerSecond.name} win!")
            break
        board.showCells()
elif(whatGame == 2):
    playerFirst = Player('zhamilka', 1)
    playerSecond = Player('alex', 2)
    board.showCells()
    while board.allCellAreNotVisited():
        firstPlayerMove = int(input("Type your cell from 1 to 9 Zha"))
        board.visitCell(firstPlayerMove-1, playerFirst.number)
        if(board.winCheck(playerFirst.number)):
            print(f"{playerFirst.name} win!")
            break
        board.showCells()
        secondPlayerMove = int(input("Type your cell from 1 to 9 Alex"))
        board.visitCell(secondPlayerMove-1, playerSecond.number)
        if (board.winCheck(playerSecond.number)):
            print(f"{playerSecond.name} win!")
            break
        board.showCells()

