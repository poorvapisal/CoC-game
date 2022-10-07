from src.person import Person
from src.headers import *
from src.input import *

class King(Person):
    def __init__(self, x, y):
        Person.__init__(self, x, y, 2, 20, 1)

    def king_show(self, grid):
        x = self.getx()
        y = self.gety()

        grid[y][x] = "K"
    
    def axe(self, grid):
        
        for i in range (self.getx()-5, self.getx()+5):
            for j in range (self.gety()-5, self.gety()+5):
                if grid[j][i] == "H":
                    print()

    def displayHealth(self):
        bar = '|'
        for i in range(int(self._health / 2)):
            bar += '■'

        for _ in range(int((20 - self._health) / 2)):
            bar += ' '
        bar += '|'
        print (bar)

    def move(self, temp, color_grid, grid):

        k1=0

        for i in range((int)(WIDTH/5)-7, (int)(WIDTH/5)+7):
            for j in range((int)(HT/2)-7, (int)(HT/2)+7):
                if (j == self.gety() and i == self.getx()):
                    self.healths(1)
                    k1=1
                    break
            if(k1==1):
                break
        
        k1=0

        for i in range((int)(3*WIDTH/5)-7, (int)(3*WIDTH/5)+7):
            for j in range((int)(5*HT/6)-7, (int)(5*HT/6)+7):
                if (j == self.gety() and i == self.getx()):
                    self.healths(1)
                    k1=1
                    break
            if(k1==1):
                break

        k1=0

        for i in range((int)(4*WIDTH/5)-7, (int)(4*WIDTH/5)+7):
            for j in range((int)(HT/3)-7, (int)(HT/3)+7):
                if (j == self.gety() and i == self.getx()):
                    self.healths(1)
                    break
            if(k1==1):
                break

        k1=0

        if(temp == 'w' and grid[self.gety()-1][self.getx()] == "."):

            grid[self.gety()][self.getx()] = "."
            grid[self.gety()-1][self.getx()] = "K"
            self.sety(self.gety()-1)

        elif(temp == 's' and grid[self.gety()+1][self.getx()] == "."):

            grid[self.gety()][self.getx()] = "."
            grid[self.gety()+1][self.getx()] = "K"
            self.sety(self.gety()+1)

        elif(temp == 'a' and grid[self.gety()][self.getx()-1] == "."):

            grid[self.gety()][self.getx()] = "."
            grid[self.gety()][self.getx()-1] = "K"
            self.setx(self.getx()-1)

        elif(temp == 'd' and grid[self.gety()][self.getx()+1] == "."):

            grid[self.gety()][self.getx()] = "."
            grid[self.gety()][self.getx()+1] = "K"
            self.setx(self.getx()+1)

        elif(temp == ' '):
            if(grid[self.gety()][self.getx()+1] == "#"):
                grid[self.gety()][self.getx()+1] = "."
            elif(grid[self.gety()][self.getx()-1] == "#"):
                grid[self.gety()][self.getx()-1] = "."
            elif(grid[self.gety()+1][self.getx()] == "#"):
                grid[self.gety()+1][self.getx()] = "."
            elif(grid[self.gety()-1][self.getx()] == "#"):
                grid[self.gety()-1][self.getx()] = "."

            if(grid[self.gety()][self.getx()+1] == "H"):
                for key, val in list(DICT1.items()):
                    # print(key)
                    for value in val:
                        if value == self.getx()+1:
                            n = key
                            # print(n)
                            obj_hut[n-1].hitpts(1,n)
                            obj_hut[n-1].hut_show(color_grid, grid)
                            if obj_hut[n-1]._hitpoints==0:
                                DICT1.pop(n)
                                DICT3.pop(n)
                            break

            elif(grid[self.gety()][self.getx()-1] == "H"):
                for key, val in list(DICT1.items()):
                    # print(key)
                    for value in val:
                        if value == self.getx()-1:
                            n = key
                            # print(n)
                            obj_hut[n-1].hitpts(1,n)
                            obj_hut[n-1].hut_show(color_grid, grid)
                            if obj_hut[n-1]._hitpoints==0:
                                DICT1.pop(n)
                                DICT3.pop(n)
                            break

            elif(grid[self.gety()+1][self.getx()] == "H"):
                for key, val in list(DICT1.items()):
                    # print(key)
                    for value in val:
                        if value == self.getx():
                            n = key
                            # print(n)
                            obj_hut[n-1].hitpts(1,n)
                            obj_hut[n-1].hut_show(color_grid, grid)
                            if obj_hut[n-1]._hitpoints==0:
                                DICT1.pop(n)
                                DICT3.pop(n)
                            break

            elif (grid[self.gety()-1][self.getx()] == 'H'):
                for key, val in list(DICT1.items()):
                    # print(key)
                    for value in val:
                        if value == self.getx():
                            n = key
                            # print(n)
                            obj_hut[n-1].hitpts(1,n)
                            obj_hut[n-1].hut_show(color_grid, grid)
                            if obj_hut[n-1]._hitpoints==0:
                                DICT1.pop(n)
                                DICT3.pop(n)
                            break

            if(grid[self.gety()][self.getx()+1] == "T"):
                for val in DICT2:

                    if val == self.getx()+1:
                        obj_townhall[0].hitpts(1,0)
                        obj_townhall[0].townhall_show(color_grid,grid)
                        if obj_townhall[0]._hitpoints==0:
                                DICT3.pop(6)
                        break

            elif(grid[self.gety()][self.getx()-1] == "T"):
                for val in DICT2:

                    if val == self.getx()-1:
                        obj_townhall[0].hitpts(1,0)
                        obj_townhall[0].townhall_show(color_grid,grid)
                        if obj_townhall[0]._hitpoints==0:
                                DICT3.pop(6)
                        break

            elif(grid[self.gety()+1][self.getx()] == "T"):
                for val in DICT2:

                    if val == self.getx():
                        obj_townhall[0].hitpts(1,0)
                        obj_townhall[0].townhall_show(color_grid,grid)
                        if obj_townhall[0]._hitpoints==0:
                                DICT3.pop(6)
                        break

            elif(grid[self.gety()-1][self.getx()] == "T"):
                for val in DICT2:

                    if val == self.getx():
                        obj_townhall[0].hitpts(1,0)
                        obj_townhall[0].townhall_show(color_grid,grid)
                        if obj_townhall[0]._hitpoints==0:
                                DICT3.pop(6)
                        break

        if temp == 'q':
            quit()
