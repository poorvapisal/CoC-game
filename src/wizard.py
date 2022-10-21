from src.building import *
from src.headers import *


class wizard(Building):

    def __init__(self, x, y):
        Building.__init__(self, x, y, 5, 0)

    def show(self, grid):
        x = self.getx()
        y = self.gety()

        grid[y][x] = Fore.MAGENTA + "W" + Fore.RESET

    def shoot(self):

        troop_found = 0
        troop_num = 0

        if len(troop_area) == 0:
            for troop in troops:
                if troop.gety > (self.gety - 7) and troop.gety < (self.gety + 7):
                    if troop.getx > (self.getx - 7) and troop.getx < (self.getx + 7):
                        troop_area.append(troop)
                        troop_found = 1
                        break
                
                if troop_found == 1:
                    break
                else:
                    return

        if len(troop_area) != 0:

            if troop_area[0].gety > (self.gety - 7) and troop_area[0].gety < (self.gety + 7) and troop_area[0].getx > (self.getx - 7) and troop_area[0].getx < (self.getx + 7):
                    
                troop_area[0].healths(1)

                if troop_area[0].health <= 0:
                    troops.remove(troop_area[0])
                    troop_area.pop(0)

                else:
                    for i in range(troop_area[0].gety-1, troop_area[0].gety+1):
                        for j in range(troop_area[0].getx-1, troop_area[0].getx+1):
                            
                            inc = 0

                            for t in troops:
                                
                                #if i == troop_area[0].gety and j == troop_area[0].getx:
                                if t == troop_area[0]:
                                    continue

                                elif t.gety == i and t.getx == j:
                                    t.healths(1)

                                    if troops[inc].health <= 0:
                                        troops.pop(inc)
                                
                                inc = inc + 1

            else:
                if len(troop_area) != 0 and troop_area[0].health < 0:                               
                    troop_area.pop()          # if the target troop is no longer in range

   



