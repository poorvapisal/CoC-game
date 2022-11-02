from src.headers import *
from src.building import *

class Cannon(Building):

    def __init__(self, x, y):
        Building.__init__(self, x, y, 1, 5)

    def show(self, grid):
        x = self.getx()
        y = self.gety()

        grid[y][x] = Fore.YELLOW + "$" + Fore.RESET 
        
           
