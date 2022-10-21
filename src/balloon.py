from src.person import Person
from src.headers import *
from src.input import *


class Balloon(Person):
    def __init__(self, x, y):
        Person.__init__(self, x, y, 2, 6, 2)
        self.flag = 0
        self.current_char = '.'
        self.current_char_color = 'w' 
        self.__color = Fore.GREEN

    def balloon_show(self, color_grid, grid):
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
        grid[y][x] = "O"

    def move(self, color_grid, grid):

        dist = 500
        num = 0
        temp = 0
        k1 = 0
        building_x = 0
        building_y = 0
        flag = 0

        if(len(DICT4) == 0 and len(DICT3) == 0):
            return

        if(len(DICT4) != 0):
            for key, value in DICT4.items():
                point1 = np.array([self.getx(), self.gety()])
                point2 = np.array([value[0], value[1]])
                temp = np.linalg.norm(point1 - point2)

                if temp < dist:
                    dist = temp
                    num = key

            building_x = DICT4[num][0]
            building_y = DICT4[num][1]
            flag = 0

        elif(len(DICT3) != 0):
            for key, value in DICT3.items():
                point1 = np.array([self.getx(), self.gety()])
                point2 = np.array([value[0], value[1]])
                temp = np.linalg.norm(point1 - point2)

                if temp < dist:
                    dist = temp
                    num = key

            building_x = DICT3[num][0]
            building_y = DICT3[num][1]
            flag = 1

        if building_y < self.gety():

            if (self.gety()-1) == building_y and (self.getx() == building_x):
                if grid[self.gety()-1][self.getx()] == (Fore.YELLOW + "$" + Fore.RESET ) or grid[self.gety()-1][self.getx()] == (Fore.MAGENTA + "W" + Fore.RESET):
                    for key, value in DICT4.items():
                        if (self.gety()-1) == value[1] and self.getx() == value[0]:
                            dest_build[key-1].hitpts(4, 6)
                            dest_build[key-1].show(grid)

                            if dest_build[key-1]._hitpoints <= 0:
                                DICT4.pop(key)
                                #dest_build.pop(key)
                            break
                    
                elif grid[self.gety()-1][self.getx()] == 'H':         #O is to below the hut
                    for key, val in list(DICT1.items()):
                        # print(key)
                        for value in val:
                            if value == self.getx():
                                n = key
                                # print(n)
                                obj_hut[n-1].hitpts(4, 6)
                                obj_hut[n-1].hut_show(color_grid, grid)
                                if obj_hut[n-1]._hitpoints == 0:
                                    DICT1.pop(n)
                                    DICT3.pop(n)
                                break

                elif grid[self.gety()-1][self.getx()] == 'T':
                    for val in DICT2:
                        if val == self.getx():
                            obj_townhall[0].hitpts(4, 6)
                            obj_townhall[0].townhall_show(color_grid, grid)
                            if obj_townhall[0]._hitpoints == 0:
                                DICT3.pop(8)
                            break
                    
            else: #if (self.get_x()-1) != building_x:
                # reset the char that was previously in the position the balloon is in
                grid[self.gety()][self.getx()] = self.current_char
                color_grid[self.gety()][self.getx()] = self.current_char_color

                # save the char in the position the balloon will move to 
                self.current_char = grid[self.gety()-1][self.getx()]
                self.current_char_color = color_grid[self.gety()-1][self.getx()]

                # move the balloon to that position
                grid[self.gety()-1][self.getx()] = 'O'
                color_grid[self.gety()-1][self.getx()] = 'w'

                self.sety(self.gety()-1)

        if building_y > self.gety():
    
            if (self.gety()+1) == building_y and (self.getx() == building_x):
                if grid[self.gety()+1][self.getx()] == (Fore.YELLOW + "$" + Fore.RESET ) or grid[self.gety()+1][self.getx()] == (Fore.MAGENTA + "W" + Fore.RESET):
                    for key, value in DICT4.items():
                        if (self.gety()+1) == value[1] and self.getx() == value[0]:
                            dest_build[key-1].hitpts(4, 6)
                            dest_build[key-1].show(grid)

                            if dest_build[key-1]._hitpoints <= 0:
                                DICT4.pop(key)
                                #dest_build.pop(key)
                            break
                    
                elif grid[self.gety()+1][self.getx()] == 'H':         #O is to below the hut
                    for key, val in list(DICT1.items()):
                        # print(key)
                        for value in val:
                            if value == self.getx():
                                n = key
                                # print(n)
                                obj_hut[n-1].hitpts(4, 6)
                                obj_hut[n-1].hut_show(color_grid, grid)
                                if obj_hut[n-1]._hitpoints == 0:
                                    DICT1.pop(n)
                                    DICT3.pop(n)
                                break

                elif grid[self.gety()+1][self.getx()] == 'T':
                    for val in DICT2:
                        if val == self.getx():
                            obj_townhall[0].hitpts(4, 6)
                            obj_townhall[0].townhall_show(color_grid, grid)
                            if obj_townhall[0]._hitpoints == 0:
                                DICT3.pop(8)
                            break
                    
            else: #if (self.get_x()-1) != building_x:
                # reset the char that was previously in the position the balloon is in
                grid[self.gety()][self.getx()] = self.current_char
                color_grid[self.gety()][self.getx()] = self.current_char_color

                # save the char in the position the balloon will move to 
                self.current_char = grid[self.gety()+1][self.getx()]
                self.current_char_color = color_grid[self.gety()+1][self.getx()]

                # move the balloon to that position
                grid[self.gety()+1][self.getx()] = 'O'
                color_grid[self.gety()+1][self.getx()] = 'w'

                self.sety(self.gety()+1)

        elif building_x < self.getx():
            if (self.gety()) == building_y and ((self.getx()-1) == building_x):
                if grid[self.gety()][self.getx()-1] == (Fore.YELLOW + "$" + Fore.RESET ) or grid[self.gety()][self.getx()-1] == (Fore.MAGENTA + "W" + Fore.RESET):
                    for key, value in DICT4.items():
                        if (self.gety()) == value[1] and (self.getx()-1) == value[0]:
                            dest_build[key-1].hitpts(4, 6)
                            dest_build[key-1].show(grid)

                            if dest_build[key-1]._hitpoints <= 0:
                                DICT4.pop(key)
                                #dest_build.pop(key)
                            break
                    
                elif grid[self.gety()][self.getx()-1] == 'H':         #O is to below the hut
                    for key, val in list(DICT1.items()):
                        # print(key)
                        for value in val:
                            if value == self.getx()-1:
                                n = key
                                # print(n)
                                obj_hut[n-1].hitpts(4, 6)
                                obj_hut[n-1].hut_show(color_grid, grid)
                                if obj_hut[n-1]._hitpoints == 0:
                                    DICT1.pop(n)
                                    DICT3.pop(n)
                                break

                elif grid[self.gety()][self.getx()-1] == 'T':
                    for val in DICT2:
                        if val == self.getx()-1:
                            obj_townhall[0].hitpts(4, 6)
                            obj_townhall[0].townhall_show(color_grid, grid)
                            if obj_townhall[0]._hitpoints == 0:
                                DICT3.pop(8)
                            break
                    
            else: #if (self.get_x()-1) != building_x:
                # reset the char that was previously in the position the balloon is in
                grid[self.gety()][self.getx()] = self.current_char
                color_grid[self.gety()][self.getx()] = self.current_char_color

                # save the char in the position the balloon will move to 
                self.current_char = grid[self.gety()][self.getx()-1]
                self.current_char_color = color_grid[self.gety()][self.getx()-1]

                # move the balloon to that position
                grid[self.gety()][self.getx()-1] = 'O'
                color_grid[self.gety()][self.getx()-1] = 'w'

                self.setx(self.getx()-1)

        elif building_x > self.getx():
            if (self.gety()) == building_y and ((self.getx()+1) == building_x):
                if grid[self.gety()][self.getx()+1] == (Fore.YELLOW + "$" + Fore.RESET ) or grid[self.gety()][self.getx()+1] == (Fore.MAGENTA + "W" + Fore.RESET):
                    for key, value in DICT4.items():
                        if (self.gety() == value[1] and (self.getx()+1) == value[0]):
                            dest_build[key-1].hitpts(4, 6)
                            dest_build[key-1].show(grid)

                            if dest_build[key-1]._hitpoints <= 0:
                                DICT4.pop(key)
                                #dest_build.pop(key)
                            break
                    
                elif grid[self.gety()][self.getx()+1] == 'H':         #O is to below the hut
                    for key, val in list(DICT1.items()):
                        # print(key)
                        for value in val:
                            if value == self.getx()+1:
                                n = key
                                # print(n)
                                obj_hut[n-1].hitpts(4, 6)
                                obj_hut[n-1].hut_show(color_grid, grid)
                                if obj_hut[n-1]._hitpoints == 0:
                                    DICT1.pop(n)
                                    DICT3.pop(n)
                                break

                elif grid[self.gety()][self.getx()+1] == 'T':
                    for val in DICT2:
                        if val == self.getx()+1:
                            obj_townhall[0].hitpts(4, 6)
                            obj_townhall[0].townhall_show(color_grid, grid)
                            if obj_townhall[0]._hitpoints == 0:
                                DICT3.pop(8)
                            break
                    
            else: #if (self.get_x()-1) != building_x:
                # reset the char that was previously in the position the balloon is in
                grid[self.gety()][self.getx()] = self.current_char
                color_grid[self.gety()][self.getx()] = self.current_char_color

                # save the char in the position the balloon will move to 
                self.current_char = grid[self.gety()][self.getx()+1]
                self.current_char_color = color_grid[self.gety()][self.getx()+1]

                # move the balloon to that position
                grid[self.gety()][self.getx()+1] = 'O'
                color_grid[self.gety()][self.getx()+1] = 'w'

                self.setx(self.getx()+1)
