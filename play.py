from src.headers import *
from src.utility import *
from src.input import *
from src.troops import *

os.system('clear')

char = Get()

while True:

    if(len(DICT3)==0):
        os.system('clear')
        yay()
        quit()

    k1=0

    os.system('clear')
    print_header()
    obj_board.print_board()
    bking.displayHealth()

    temp = input_to(Get())

    f = open("./replays/replay.txt", "a")
    if (temp==None):
        f.write(" ")
    else:
        f.write(temp)
    f.close()

    if temp == 'q':
        quit()

    elif temp == 'j' and COUNT < 6:
        obj_troop.append(Troop((int)(WIDTH/3), 2))
        obj_troop[COUNT].flag = 1
        obj_troop[COUNT].troop_show(obj_board.color_grid, obj_board.grid)
        COUNT += 1

    elif temp == 'k' and COUNT < 6:
        obj_troop.append(Troop(2, (int)(HT/2)))
        obj_troop[COUNT].flag = 1
        obj_troop[COUNT].troop_show(obj_board.color_grid, obj_board.grid)
        COUNT += 1

    elif temp == 'l' and COUNT < 6:
        obj_troop.append(Troop((int)(2*WIDTH/3), HT-3))
        obj_troop[COUNT].flag = 1
        obj_troop[COUNT].troop_show(obj_board.color_grid, obj_board.grid)
        COUNT += 1

    elif temp == 'r':
    
        bking._damage *= 2

        for i in range(len(obj_troop)):
            obj_troop[i]._damage *= 2 

    elif temp == 'h':

        if bking._health * 1.5 < 20 :
            bking._health = bking._health * 1.5
        else :
            bking._health = 20
        
        print(bking._health)

        for i in range(len(obj_troop)):

            if obj_troop[i]._health * 1.5 < 10 :
                obj_troop[i]._health = obj_troop[i]._health * 1.5
            else :
                obj_troop[i]._health = 10

    elif temp == '':

        bking.axe(obj_board.grid)

    else:
        if (bking._health>0):
            bking.move(temp, obj_board.color_grid, obj_board.grid)

    for i in range(COUNT):
    
        if (obj_troop[i].flag == 1 and obj_troop[i]._health !=0):
            obj_troop[i].move(obj_board.color_grid,obj_board.grid)
            k1=1

    if (k1==0 and bking._health==0):
        game_over()
        quit()
