from src.person import Person
from src.headers import *
from src.input import *


class Archer(Person):
    def __init__(self, x, y):
        Person.__init__(self, x, y, 2, 3, 2)
        self.flag = 0
        self.__color = Fore.GREEN
        range = 7

    def archer_show(self, color_grid, grid):
        x = self.getx()
        y = self.gety()

        color_char = 'w'

        print(self._health)

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
        grid[y][x] = "A"

    def move(self, color_grid, grid):

        dist = 500
        num = 0
        temp = 0
        k1 = 0

        if(len(DICT3) == 0):
            return

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
                grid[self.gety()-1][self.getx()] = 'A'
                grid[self.gety()][self.getx()] = '.'
                self.sety(self.gety()-1)

            elif (grid[self.gety()-1][self.getx()] == '#'):
                grid[self.gety()-1][self.getx()] = '.'

        elif building_y > self.gety():
            if (grid[self.gety()+1][self.getx()] == '.'):
                grid[self.gety()][self.getx()] = '.'
                grid[self.gety()+1][self.getx()] = 'A'
                self.sety(self.gety()+1)

            elif (grid[self.gety()+1][self.getx()] == '#'):
                grid[self.gety()+1][self.getx()] = '.'

        elif building_x < self.getx():
            if(grid[self.gety()][self.getx()-1] == '.'):
                grid[self.gety()][self.getx()] = '.'
                grid[self.gety()][self.getx()-1] = 'A'
                self.setx(self.getx()-1)

            elif grid[self.gety()][self.getx()-1] == '#':
                grid[self.gety()][self.getx()-1] = '.'

        elif building_x > self.getx():
            if(grid[self.gety()][self.getx()+1] == '.'):
                grid[self.gety()][self.getx()] = '.'
                grid[self.gety()][self.getx()+1] = 'A'
                self.setx(self.getx()+1)

            elif(grid[self.gety()][self.getx()+1] == '#'):
                grid[self.gety()][self.getx()+1] = '.'

        for i in range(self.getx() - 10, self.getx() + 10):
            for j in range(self.gety() - 10, self.gety() + 10):

                if(i > 198):
                    i = 198

                elif(i < 2):
                    i = 2

                if (j > 38):
                    j = 38

                elif(j < 2):
                    j = 2

                if(grid[j][i] == 'H'):
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
