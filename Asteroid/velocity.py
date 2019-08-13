"""
Name: velocity
Author: Kwok Moon Ho
Description:
This class is to handle the velocity of the objects.
"""
import random

class Velocity:
    def __init__(self):            ##constructor
        self.dx = 0
        self.dy = 0

    @property
    def dx(self):
        return self._dx

    @dx.setter
    def dx(self, new_dx):
        self._dx = new_dx

    @property
    def dy(self):
        return self._dy

    @dy.setter
    def dy(self,new_dy):
        self._dy = new_dy
