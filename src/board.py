from src.headers import *


class Board:

    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.grid = []
        self.color_grid = []

    # function to create the playing board
    def create_board(self):
        for i in range(self.__rows):
            self.temp = []
            for j in range(self.__cols):
                if ((i != 0 and j != 0 and i != self.__rows-1 and j != self.__cols-1) and (i == 1 or j == 1 or j == self.__cols-2 or i == self.__rows-2)):
                    self.temp.append("#")
                # if (i==1 and j==(int)(WIDTH/3)) or (j==1 and i==(int)(HT/2)) or (j==(int)(2*WIDTH/3) and i==HT-2):
                #     self.temp.append("o")
                else:
                    self.temp.append(".")
            self.grid.append(self.temp)

        for i in range(self.__rows):
            self.temp1=[]
            for j in range(self.__cols):
                self.temp1.append("w")
            self.color_grid.append(self.temp1)

    # function to print the playing board
    def print_board(self):
        color = Fore.WHITE

        for i in range(self.__rows):
            for j in range (self.__cols):
                     
                    # print(Back.GREEN + self.grid[i][j],end='')
                if self.color_grid[i][j] == 'w':
                    color = Fore.BLACK
                if self.grid[i][j]==".":
                    color = Fore.LIGHTGREEN_EX
                if self.color_grid[i][j] == 'g':
                    color = Fore.BLUE
                if self.color_grid[i][j] == 'y':
                    color = Fore.YELLOW
                if self.color_grid[i][j] == 'r':
                    color = Fore.RED

                print(color + Back.GREEN + self.grid[i][j] + Fore.RESET + Back.RESET, end='')
                # print(Fore.RESET)

            print()
