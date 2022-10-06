from src.headers import *

class Person():

    def __init__(self, x_cood, y_cood, damage, health, speed):

        self._x_cood = x_cood
        self._y_cood = y_cood
        self._damage = damage
        self._health = health
        self._speed = speed

    def getx(self):
        return self._x_cood

    def setx(self, x):
        self._x_cood = x

    def gety(self):
        return self._y_cood

    def sety(self, y):
        self._y_cood = y

    def healths(self, hits):
        self._health = self._health-hits
