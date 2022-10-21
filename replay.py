from src.headers import *
from src.utility import *
from src.input import *
from src.barbarians import *

os.system('clear')

file = open('./replays/replay.txt', 'r')

while True:

    time.sleep(0.1)
    if(len(DICT3)==0):
        os.system('clear')
        yay()
        quit()

    k1=0

    os.system('clear')
    print_header()
    obj_board.print_board()
    bking.displayHealth()


    temp = file.read(1)         
    
    if temp == 'q':
        quit()

    elif temp == 'j' and COUNT < 6:
        obj_barb.append(Troop((int)(WIDTH/3), 2))
        obj_barb[COUNT].flag = 1
        obj_barb[COUNT].troop_show(obj_board.color_grid, obj_board.grid)
        COUNT += 1

    elif temp == 'k' and COUNT < 6:
        obj_barb.append(Troop(2, (int)(HT/2)))
        obj_barb[COUNT].flag = 1
        obj_barb[COUNT].troop_show(obj_board.color_grid, obj_board.grid)
        COUNT += 1

    elif temp == 'l' and COUNT < 6:
        obj_barb.append(Troop((int)(2*WIDTH/3), HT-3))
        obj_barb[COUNT].flag = 1
        obj_barb[COUNT].troop_show(obj_board.color_grid, obj_board.grid)
        COUNT += 1

    elif temp == 'r':
    
        bking._damage *= 2

        for i in range(len(obj_barb)):
            obj_barb[i]._damage *= 2 

    elif temp == 'h':

        if bking._health * 1.5 < 20 :
            bking._health = bking._health * 1.5
        else :
            bking._health = 20
        
        print(bking._health)

        for i in range(len(obj_barb)):

            if obj_barb[i]._health * 1.5 < 10 :
                obj_barb[i]._health = obj_barb[i]._health * 1.5
            else :
                obj_barb[i]._health = 10

    else:
        if (bking._health>0):
            bking.move(temp, obj_board.color_grid, obj_board.grid)

    for i in range(COUNT):
    
        if (obj_barb[i].flag == 1 and obj_barb[i]._health !=0):
            obj_barb[i].move(obj_board.color_grid,obj_board.grid)
            k1=1

    if (k1==0 and bking._health==0):
        game_over()
        quit()
