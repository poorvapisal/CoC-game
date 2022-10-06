from src.headers import *

class Building():

    def __init__(self, x_cood, y_cood, hitpoints, ranges):

        self._x_cood = x_cood
        self._y_cood = y_cood
        self._hitpoints = hitpoints
        self._ranges = ranges

    def getx(self):
        return self._x_cood

    def setx(self, x):
        self._x_cood = x

    def gety(self):
        return self._y_cood

    def sety(self, y):
        self._y_cood = y

    def hitpts(self, hits, n):
        self._hitpoints = self._hitpoints-hits
