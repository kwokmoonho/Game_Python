"""
Name: Point
Author: Kwok Moon Ho
Description:
This is the class to handle the point location of the bullet, bird and the paddle.
"""
import random

class Point:
    def __init__(self):            ##constructor
        self.x = 0.0
        self.y = 0.0

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,new_x):
        self._x = new_x

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self,new_y):
        self._y = new_y
