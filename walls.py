from src.building import *
from src.headers import *

walls = [list("#######"),
         list("#.....#"),
         list("#.....#"),
         list("#.....#"),
         list("#.....#"),
         list("#.....#"),
         list("#.....#"),
         list("#######")]


class wall(Building):

    def __init__(self, x, y):
        Building.__init__(self, x, y, T_HITS, 0)

    def wall_show(self, grid):
        x = self.getx()
        y = self.gety()

        if (self._hitpoints != 0):
            for i in range(y, y+8):
                for j in range(x, x+7):
                    grid[i][j] = walls[i-y][j-x]
