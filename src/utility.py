from src.headers import *
from src.board import Board
from src.townhall import townhall
from src.hut import hut
from src.cannon import Cannon
from src.king import King
from src.walls import wall
from src.wizard import wizard
from src.queen import Queen

obj_board.append(Board(HT, WIDTH))
obj_board[0].create_board()

def print_header():
    print(Fore.WHITE + Back.RED + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.RED + Style.BRIGHT + "CLASH OF CLANS".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.RED + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)

t_wall=wall((int)(WIDTH/2)-4, (int)(HT/2)-3)
t_wall.wall_show(obj_board[0].grid)

obj_townhall.append(townhall((int)(WIDTH/2)-2, (int)(HT/2)-1))
obj_townhall[0].townhall_show(obj_board[0].color_grid,obj_board[0].grid)

obj_hut.append(hut((int)(3*WIDTH/4), (int)(4*HT/5)))
obj_hut[0].hut_show(obj_board[0].color_grid, obj_board[0].grid)
obj_hut.append(hut((int)(WIDTH/8), (int)(HT/7)))
obj_hut[1].hut_show(obj_board[0].color_grid, obj_board[0].grid)
obj_hut.append(hut((int)(7*WIDTH/8), (int)(HT/11)))
obj_hut[2].hut_show(obj_board[0].color_grid, obj_board[0].grid)
obj_hut.append(hut((int)(2*WIDTH/9), (int)(3*HT/5)))
obj_hut[3].hut_show(obj_board[0].color_grid, obj_board[0].grid)
obj_hut.append(hut((int)(3*WIDTH/5), (int)(2*HT/7)))
obj_hut[4].hut_show(obj_board[0].color_grid, obj_board[0].grid)
obj_hut.append(hut((int)(3*WIDTH/5)+3, (int)(2*HT/7)+2))
obj_hut[5].hut_show(obj_board[0].color_grid, obj_board[0].grid)
obj_hut.append(hut((int)(WIDTH/8)-3, (int)(HT/7)+2))
obj_hut[6].hut_show(obj_board[0].color_grid, obj_board[0].grid)

obj_can1 = Cannon((int)(WIDTH/5), (int)(HT/2))
dest_build.append(obj_can1)
obj_can1.show(obj_board[0].grid)
obj_can2 = Cannon((int)(3*WIDTH/5), (int)(5*HT/6))
dest_build.append(obj_can2)
obj_can2.show(obj_board[0].grid)
#dest_build.append(obj_can1,obj_can2,obj_can3)

obj_wiz1 = wizard((int)(3*WIDTH/8), (int)(HT/7))
dest_build.append(obj_wiz1)
obj_wiz1.show(obj_board[0].grid)
obj_wiz2 = wizard((int)(7*WIDTH/8), (int)(2*HT/3))
dest_build.append(obj_wiz2)
obj_wiz2.show(obj_board[0].grid)
#dest_build.append(obj_wiz1,obj_wiz2)