from src.building import *
from src.headers import *
huts = [list("HH"), list("HH")]

class hut(Building):

    def __init__(self, x, y):
        Building.__init__(self, x, y, H_HITS, 0)
        self.__color = Fore.GREEN

    def hut_show(self, color_grid, grid):
        x = self.getx()
        y = self.gety()
        
        color_char = 'w'

        if self._hitpoints <= 5 and self._hitpoints > 3:
            self.__color = Fore.GREEN
            color_char = 'g'

        if self._hitpoints <= 3 and self._hitpoints > 1:
            self.__color = Fore.YELLOW
            color_char = 'y'

        if self._hitpoints <= 1 and self._hitpoints > 0:
            self.__color = Fore.RED
            color_char = 'r'

        if (self._hitpoints != 0):
            for i in range(y, y+2):
                for j in range(x, x+2):
                    grid[i][j] = huts[i-y][j-x]
                    color_grid[i][j] = color_char

        else:
            for i in range(y, y+2):
                for j in range(x, x+2):
                    grid[i][j] = "."

        
