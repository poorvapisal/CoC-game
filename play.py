from src.headers import *
from src.utility import *
from src.input import *

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
    
    if temp == 'q':
        quit()
        
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
        
    else:
        if (bking._health>0):
            bking.move(temp, obj_board.color_grid, obj_board.grid)
            
    if (k1==0 and bking._health==0):
        game_over()
        quit()
