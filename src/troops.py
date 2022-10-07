from src.person import Person
from src.headers import *
from src.input import *


class Troop(Person):
    def __init__(self, x, y):
        Person.__init__(self, x, y, 2, 5, 1)
        self.flag = 0
        self.__color = Fore.GREEN

    def troop_show(self, color_grid, grid):
        x = self.getx()
        y = self.gety()

        color_char = 'w'

        if self._health <= 5 and self._health > 3:
            self.__color = Fore.GREEN
            color_char = 'g'

        if self._health <= 3 and self._health > 1:
            self.__color = Fore.YELLOW
            color_char = 'y'

        if self._health <= 1 and self._health > 0:
            self.__color = Fore.RED
            color_char = 'r'

        color_grid[y][x] = color_char
        grid[y][x] = "B"

    def move(self, color_grid, grid):

        dist = 500
        num = 0
        temp = 0
        k1=0

        if(len(DICT3) == 0):
            return

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

        for key, value in DICT3.items():
            point1 = np.array([self.getx(), self.gety()])
            point2 = np.array([value[0], value[1]])
            temp = np.linalg.norm(point1 - point2)

            if temp < dist:
                dist = temp
                num = key

        building_x = DICT3[num][0]
        building_y = DICT3[num][1]

        if building_y < self.gety():
            if (grid[self.gety()-1][self.getx()] == '.'):
                grid[self.gety()-1][self.getx()] = 'B'
                grid[self.gety()][self.getx()] = '.'
                self.sety(self.gety()-1)

            elif (grid[self.gety()-1][self.getx()] == '#'):
                grid[self.gety()-1][self.getx()] = '.'

            elif (grid[self.gety()-1][self.getx()] == 'H'):
                for key, val in list(DICT1.items()):
                    # print(key)
                    for value in val:
                        if value == self.getx():
                            n = key
                            # print(n)
                            obj_hut[n-1].hitpts(1, 6)
                            obj_hut[n-1].hut_show(color_grid, grid)
                            if obj_hut[n-1]._hitpoints == 0:
                                DICT1.pop(n)
                                DICT3.pop(n)
                            break

            elif(grid[self.gety()-1][self.getx()] == "T"):
                for val in DICT2:

                    if val == self.getx():
                        obj_townhall[0].hitpts(1, 6)
                        obj_townhall[0].townhall_show(color_grid, grid)
                        if obj_townhall[0]._hitpoints == 0:
                            DICT3.pop(6)
                        break

        elif building_y > self.gety():
            if (grid[self.gety()+1][self.getx()] == '.'):
                grid[self.gety()][self.getx()] = '.'
                grid[self.gety()+1][self.getx()] = 'B'
                self.sety(self.gety()+1)

            elif (grid[self.gety()+1][self.getx()] == '#'):
                grid[self.gety()+1][self.getx()] = '.'

            elif(grid[self.gety()+1][self.getx()] == "H"):
                for key, val in list(DICT1.items()):
                    # print(key)
                    for value in val:
                        if value == self.getx():
                            n = key
                            # print(n)
                            obj_hut[n-1].hitpts(1, 6)
                            obj_hut[n-1].hut_show(color_grid, grid)
                            if obj_hut[n-1]._hitpoints == 0:
                                DICT1.pop(n)
                                DICT3.pop(n)
                            break

            elif(grid[self.gety()+1][self.getx()] == "T"):
                for val in DICT2:

                    if val == self.getx():
                        obj_townhall[0].hitpts(1, 6)
                        obj_townhall[0].townhall_show(color_grid, grid)
                        if obj_townhall[0]._hitpoints == 0:
                            DICT3.pop(6)
                        break

        elif building_x < self.getx():
            if(grid[self.gety()][self.getx()-1] == '.'):
                grid[self.gety()][self.getx()] = '.'
                grid[self.gety()][self.getx()-1] = 'B'
                self.setx(self.getx()-1)

            elif grid[self.gety()][self.getx()-1] == '#':
                grid[self.gety()][self.getx()-1] = '.'

            elif(grid[self.gety()][self.getx()-1] == "H"):
                for key, val in list(DICT1.items()):
                    # print(key)
                    for value in val:
                        if value == self.getx()-1:
                            n = key
                            # print(n)
                            obj_hut[n-1].hitpts(1, 6)
                            obj_hut[n-1].hut_show(color_grid, grid)
                            if obj_hut[n-1]._hitpoints == 0:
                                DICT1.pop(n)
                                DICT3.pop(n)
                            break
            elif(grid[self.gety()][self.getx()-1] == "T"):
                for val in DICT2:

                    if val == self.getx()-1:
                        obj_townhall[0].hitpts(1, 6)
                        obj_townhall[0].townhall_show(color_grid, grid)
                        if obj_townhall[0]._hitpoints == 0:
                            DICT3.pop(6)
                        break

        elif building_x > self.getx():
            if(grid[self.gety()][self.getx()+1] == '.'):
                grid[self.gety()][self.getx()] = '.'
                grid[self.gety()][self.getx()+1] = 'B'
                self.setx(self.getx()+1)

            elif(grid[self.gety()][self.getx()+1] == "H"):
                for key, val in list(DICT1.items()):
                    # print(key)
                    for value in val:
                        if value == self.getx()+1:
                            n = key
                            # print(n)
                            obj_hut[n-1].hitpts(1, 6)
                            obj_hut[n-1].hut_show(color_grid, grid)
                            if obj_hut[n-1]._hitpoints == 0:
                                DICT1.pop(n)
                                DICT3.pop(n)
                            break

            elif(grid[self.gety()][self.getx()+1] == "T"):
                for val in DICT2:

                    if val == self.getx()+1:
                        obj_townhall[0].hitpts(1, 6)
                        obj_townhall[0].townhall_show(color_grid, grid)
                        if obj_townhall[0]._hitpoints == 0:
                            DICT3.pop(6)
                        break

            elif(grid[self.gety()][self.getx()+1] == '#'):
                grid[self.gety()][self.getx()+1] = '.'
