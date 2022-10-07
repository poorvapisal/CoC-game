from src.building import *
from src.headers import *
town_hall = [list("TTT"),
             list("T T"),
             list("T T"),
             list("TTT")]

class townhall(Building):

    def __init__(self, x, y):
        Building.__init__(self, x, y, T_HITS, 0)
        self.__color = Fore.GREEN

    def townhall_show(self, color_grid, grid):
        x = self.getx()
        y = self.gety()

        color_char = 'w'

        if self._hitpoints <= 10 and self._hitpoints > 6:
            self.__color = Fore.GREEN
            color_char = 'g'

        if self._hitpoints <= 6 and self._hitpoints > 3:
            self.__color = Fore.YELLOW
            color_char = 'y'

        if self._hitpoints <= 3 and self._hitpoints > 0:
            self.__color = Fore.RED
            color_char = 'r'

        if (self._hitpoints != 0):
            for i in range(y, y+4):
                for j in range(x, x+3):
                    grid[i][j] = town_hall[i-y][j-x]
                    color_grid[i][j] = color_char

        else:
            for i in range(y, y+4):
                for j in range(x, x+3):
                    grid[i][j] = "."
