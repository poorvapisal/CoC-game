from src.person import Person
from src.headers import *
from src.input import *

class Queen(Person):
    def __init__(self, x, y):
        Person.__init__(self, x, y, 2, 20, 1)

    def queen_show(self, grid):
        x = self.getx()
        y = self.gety()

        grid[y][x] = "Q"

    def displayHealth(self):
        bar = '|'
        for i in range(int(self._health / 2)):
            bar += '■'

        for _ in range(int((20 - self._health) / 2)):
            bar += ' '
        bar += '|'
        print(bar)

    def move(self, temp, color_grid, grid):
    
        k1 = 0
        global x1, y1, x2, y2, arrow, tim

        for key, value in DICT4.items():
    
            for i in range(value[0]-7, value[0]+7):
                for j in range(value[1]-7, value[1]+7):
                    if (j == self.gety() and i == self.getx()):
                        self.healths(1)
                        k1=1
                        break
                if(k1==1):
                    break
            
            k1=0

        if(temp == 'w' and grid[self.gety()-1][self.getx()] == "."):

            grid[self.gety()][self.getx()] = "."
            grid[self.gety()-1][self.getx()] = "Q"
            self.sety(self.gety()-1)
            x1 = -8
            y1 = 0
            x2 = -16
            y2 = 0

        elif(temp == 's' and grid[self.gety()+1][self.getx()] == "."):

            grid[self.gety()][self.getx()] = "."
            grid[self.gety()+1][self.getx()] = "Q"
            self.sety(self.gety()+1)
            x1 = 8
            y1 = 0
            x2 = 16
            y2 = 0

        elif(temp == 'a' and grid[self.gety()][self.getx()-1] == "."):

            grid[self.gety()][self.getx()] = "."
            grid[self.gety()][self.getx()-1] = "Q"
            self.setx(self.getx()-1)
            x1 = 0
            y1 = -8
            x2 = 0
            y2 = -16

        elif(temp == 'd' and grid[self.gety()][self.getx()+1] == "."):

            grid[self.gety()][self.getx()] = "."
            grid[self.gety()][self.getx()+1] = "Q"
            self.setx(self.getx()+1)
            x1 = 0
            y1 = 8
            x2 = 0
            y2 = 16

        elif(temp == ' '):
            if(grid[self.gety()][self.getx()+1] == "#"):
                grid[self.gety()][self.getx()+1] = "."
            elif(grid[self.gety()][self.getx()-1] == "#"):
                grid[self.gety()][self.getx()-1] = "."
            elif(grid[self.gety()+1][self.getx()] == "#"):
                grid[self.gety()+1][self.getx()] = "."
            elif(grid[self.gety()-1][self.getx()] == "#"):
                grid[self.gety()-1][self.getx()] = "."

            
            for i in range(self.getx() - 2 + y1, self.getx() + 2 + y1 + 1):
                for j in range(self.gety() - 2 + x1, self.gety() + 2 + x1 + 1): 
                    print(grid[j][i])

                    if(i > 198):
                        i = 198

                    elif(i < 2):
                        i = 2

                    if (j > 38):
                        j = 38

                    elif(j < 2):
                        j = 2

                    if(grid[j][i] == 'H'):
                        print("here")
                        for key, val in list(DICT1.items()):
                            for value in val:
                                if value == i:
                                    n = key
                                    # print(n)
                                    obj_hut[n-1].hitpts(1, 6)
                                    obj_hut[n-1].hut_show(color_grid, grid)
                                    if obj_hut[n-1]._hitpoints == 0:
                                        DICT1.pop(n)
                                        DICT3.pop(n)
                                    break

                    if(grid[j][i] == "T"):
                        print(obj_townhall[0]._hitpoints)
                        for val in DICT2:
                            if val == i:
                                obj_townhall[0].hitpts(1, 6)
                                obj_townhall[0].townhall_show(color_grid, grid) 
                                if obj_townhall[0]._hitpoints == 0:
                                    DICT3.pop(8)
                            break

        elif(temp == 'z'):
            arrow=1
            
        if(tim == 600):
            if(grid[self.gety()][self.getx()+1] == "#"):
                grid[self.gety()][self.getx()+1] = "."
            elif(grid[self.gety()][self.getx()-1] == "#"):
                grid[self.gety()][self.getx()-1] = "."
            elif(grid[self.gety()+1][self.getx()] == "#"):
                grid[self.gety()+1][self.getx()] = "."
            elif(grid[self.gety()-1][self.getx()] == "#"):
                grid[self.gety()-1][self.getx()] = "."

            
            for i in range(self.getx() - 4 + y2, self.getx() + 4 + y2 + 1):
                for j in range(self.gety() - 4 + x2, self.gety() + 4 + x2 + 1): 
                    print(grid[j][i])

                    if(i > 198):
                        i = 198

                    elif(i < 2):
                        i = 2

                    if (j > 38):
                        j = 38

                    elif(j < 2):
                        j = 2

                    if(grid[j][i] == 'H'):
                        print("here")
                        for key, val in list(DICT1.items()):
                            for value in val:
                                if value == i:
                                    n = key
                                    # print(n)
                                    obj_hut[n-1].hitpts(1, 6)
                                    obj_hut[n-1].hut_show(color_grid, grid)
                                    if obj_hut[n-1]._hitpoints == 0:
                                        DICT1.pop(n)
                                        DICT3.pop(n)
                                    break

                    if(grid[j][i] == "T"):
                        print(obj_townhall[0]._hitpoints)
                        for val in DICT2:
                            if val == i:
                                obj_townhall[0].hitpts(1, 6)
                                obj_townhall[0].townhall_show(color_grid, grid) 
                                if obj_townhall[0]._hitpoints == 0:
                                    DICT3.pop(8)
                            break

            tim=0

            