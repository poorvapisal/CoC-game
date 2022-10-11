import time
import numpy as np
import signal
import os
import sys
from colorama import init, Fore, Back, Style
init()
import random
from src.input import *

HT=40
SCREEN=200
WIDTH=200
obj_hut=[]
obj_townhall=[]
arrow=0
tim=0
T_HITS=10
H_HITS=5
T_COL=3
H_COL=3
W=Fore.BLACK+"#"+Fore.RESET
TROOP=6
COUNT_B=0
COUNT_A=0
COUNT_O=0
k4=2
x1=0
y1=0
x2=0
y2=0
POS=0
obj_board=[]
troops=[]
troop_area=[]
obj_barb=[]
obj_balloon=[]
obj_arch=[]
dest_build=[]
can_check1=0
can_check2=0
can_chec3=0
k_q=[]
level=0


DICT1={1:[(int)(3*WIDTH/4),(int)(3*WIDTH/4)+1],2:[(int)(WIDTH/8),(int)(WIDTH/8)+1],3:[(int)(7*WIDTH/8),(int)(7*WIDTH/8)+1],4:[(int)(2*WIDTH/9),(int)(2*WIDTH/9)+1],5:[(int)(3*WIDTH/5),(int)(3*WIDTH/5)+1], 6:[(int)(3*WIDTH/5)+3,(int)(3*WIDTH/5)+4], 7:[(int)(WIDTH/8)-3, (int)(WIDTH/8)-2]} 
DICT2=[(int)(WIDTH/2)-2,(int)(WIDTH/2)-1,(int)(WIDTH/2)]
DICT3={1:[(int)(3*WIDTH/4), (int)(4*HT/5)], 2:[(int)(WIDTH/8), (int)(HT/7)], 3:[(int)(7*WIDTH/8), (int)(HT/11)], 4:[(int)(2*WIDTH/9), (int)(3*HT/5)], 5:[(int)(3*WIDTH/5), (int)(2*HT/7)], 8:[(int)(WIDTH/2)-2, (int)(HT/2)-1], 6:[(int)(3*WIDTH/5)+3, (int)(2*HT/7)+2], 7:[(int)(WIDTH/8)-3, (int)(HT/7)+2]}
DICT4={1:[(int)(WIDTH/5), (int)(HT/2)], 2:[(int)(3*WIDTH/5), (int)(5*HT/6)], 3:[(int)(3*WIDTH/8), (int)(HT/7)], 4:[(int)(7*WIDTH/8), (int)(2*HT/3)]}

def game_over():
    os.system('aplay -q ./src/sounds/sounds_game_over.wav&')
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                     ".center(SCREEN))                 
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "  _____                         ____                 ".center(SCREEN))                 
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ " / ____|                       / __ \                ".center(SCREEN))              
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ ".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +"| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +"| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   ".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +" \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   ".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                     ".center(SCREEN)+Style.RESET_ALL)                 
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                     ".center(SCREEN)+Style.RESET_ALL)                 
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                     ".center(SCREEN)+Style.RESET_ALL)      

def yay():
    os.system('aplay -q ./src/sounds/sounds_win.wav&')
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ " __     __                             _ ".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ " \ \   / /                            | |".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "  \ \_/ /_ _  __ _  __ _  __ _ _   _  | |".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "   \   / _` |/ _` |/ _` |/ _` | | | | | |".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "    | | (_| | (_| | (_| | (_| | |_| | |_|".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "    |_|\__,_|\__,_|\__,_|\__,_|\__, | (_)".center(SCREEN)+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                __/ |    ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                               |___/     ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                         ".center(SCREEN)+Style.RESET_ALL)