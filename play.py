from re import A
from src.headers import *
from src.utility import *
from src.input import *
from src.barbarians import *
from src.balloon import *
from src.archer import *

os.system('clear')

char = Get()

while True:
    
    time.sleep(0.2)
    if(arrow==1):
        tim=tim+1

    if(len(DICT3)==0):
        os.system('clear')
        yay()
        quit()    

    k1=0
    k2=0
    k3=0

    os.system('clear')
    print_header()
    print("Press 0 to select the king and 1 to select the queen.")
    obj_board[level-1].print_board()
    if (k4!=2):
        k_q[0].displayHealth()

    temp = input_to(Get())

    f = open("./replays/replay.txt", "a")
    if (temp==None):
        f.write(" ")
    else:
        f.write(temp)
    f.close()

    if temp == 'x':
        quit()

    elif temp == 'j' and COUNT_B < 6:
        a=Troop((int)(WIDTH/3), 2)
        obj_barb.append(a)
        troops.append(a)
        obj_barb[COUNT_B].flag = 1
        obj_barb[COUNT_B].troop_show(obj_board[level-1].color_grid, obj_board[level-1].grid)
        COUNT_B += 1

    elif temp == 'k' and COUNT_B < 6:
        a=Troop(2, (int)(HT/2))
        obj_barb.append(a)
        troops.append(a)
        obj_barb[COUNT_B].flag = 1
        obj_barb[COUNT_B].troop_show(obj_board[level-1].color_grid, obj_board[level-1].grid)
        COUNT_B += 1

    elif temp == 'l' and COUNT_B < 6:
        a=Troop((int)(2*WIDTH/3), HT-3)
        obj_barb.append(a)
        troops.append(a)
        obj_barb[COUNT_B].flag = 1
        obj_barb[COUNT_B].troop_show(obj_board[level-1].color_grid, obj_board[level-1].grid)
        COUNT_B += 1

    elif temp == 'u' and COUNT_O < 3:
        a=Balloon((int)(WIDTH/3), 2)
        obj_balloon.append(a)
        troops.append(a)
        obj_balloon[COUNT_O].flag = 1
        obj_balloon[COUNT_O].balloon_show(obj_board[level-1].color_grid, obj_board[level-1].grid)
        COUNT_O += 1

    elif temp == 'i' and COUNT_O < 3:
        a=Balloon(2, (int)(HT/2))
        obj_balloon.append(a)
        troops.append(a)
        obj_balloon[COUNT_O].flag = 1
        obj_balloon[COUNT_O].balloon_show(obj_board[level-1].color_grid, obj_board[level-1].grid)
        COUNT_O += 1

    elif temp == 'o' and COUNT_O < 3:
        a=Balloon((int)(2*WIDTH/3), HT-3)
        obj_balloon.append(a)
        troops.append(a)
        obj_balloon[COUNT_O].flag = 1
        obj_balloon[COUNT_O].balloon_show(obj_board[level-1].color_grid, obj_board[level-1].grid)
        COUNT_O += 1

    elif temp == 'b' and COUNT_A < 6:
        a=Archer((int)(WIDTH/3), 2)
        obj_arch.append(a)
        troops.append(a)
        obj_arch[COUNT_A].flag = 1
        obj_arch[COUNT_A].archer_show(obj_board[level-1].color_grid, obj_board[level-1].grid)
        COUNT_A += 1

    elif temp == 'n' and COUNT_A < 6:
        a=Archer(2, (int)(HT/2))
        obj_arch.append(a)
        troops.append(a)
        obj_arch[COUNT_A].flag = 1
        obj_arch[COUNT_A].archer_show(obj_board[level-1].color_grid, obj_board[level-1].grid)
        COUNT_A += 1

    elif temp == 'm' and COUNT_A < 6:
        a=Archer((int)(2*WIDTH/3), HT-3)
        obj_arch.append(a)
        troops.append(a)
        obj_arch[COUNT_A].flag = 1
        obj_arch[COUNT_A].archer_show(obj_board[level-1].color_grid, obj_board[level-1].grid)
        COUNT_A += 1

    elif temp == 'p':
    
        k_q[0]._damage *= 2

        for i in range(len(obj_barb)):
            obj_barb[i]._damage *= 2 

    elif temp == 'h':

        if k_q[0]._health * 1.5 < 20 :
            k_q[0]._health = k_q[0]._health * 1.5
        else :
            k_q[0]._health = 20
        
        print(k_q[0]._health)

        for i in range(len(obj_barb)):

            if obj_barb[i]._health * 1.5 < 10 :
                obj_barb[i]._health = obj_barb[i]._health * 1.5
            else :
                obj_barb[i]._health = 10

    elif temp == '1':
        k4 = 1
        k_q.append(Queen(2,2))
        k_q[0].queen_show(obj_board[level-1].grid)

    elif temp == '0':
        k4 = 0
        k_q.append(King(2,2))
        k_q[0].king_show(obj_board[level-1].grid)
    
    else:
        if (k4 == 1):
            if (k_q[0]._health>0):
                k_q[0].move(temp, obj_board[level-1].color_grid, obj_board[level-1].grid)
        elif (k4 == 0):
            if (k_q[0]._health>0):
                k_q[0].move(temp, obj_board[level-1].color_grid, obj_board[level-1].grid)

    for i in range(COUNT_B):
    
        if (obj_barb[i].flag == 1 and obj_barb[i]._health !=0):
            #print(obj_barb[i]._health)
            obj_barb[i].move(obj_board[level-1].color_grid,obj_board[level-1].grid)
            k1=1

    for i in range(COUNT_O):
        
        if (obj_balloon[i].flag == 1 and obj_balloon[i]._health !=0):
            obj_balloon[i].move(obj_board[level-1].color_grid,obj_board[level-1].grid)
            k2=1

    for i in range(COUNT_A):
        
        if (obj_arch[i].flag == 1 and obj_arch[i]._health !=0):
            obj_arch[i].move(obj_board[level-1].color_grid,obj_board[level-1].grid)
            k3=1

    if (k4!=2 and k1==0 and k_q[0]._health==0 and k2==0):
        game_over()
        quit()
