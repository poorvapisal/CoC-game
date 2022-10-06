from src.headers import *
from src.board import Board
from src.walls import wall

obj_board = Board(HT, WIDTH)
obj_board.create_board()

def print_header():
    print(Fore.WHITE + Back.RED + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.RED + Style.BRIGHT + "CLASH OF CLANS".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.RED + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)

t_wall=wall((int)(WIDTH/2)-4, (int)(HT/2)-3)
t_wall.wall_show(obj_board.grid)

