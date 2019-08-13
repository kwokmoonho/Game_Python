"""
Name: Point
Author: Kwok Moon Ho
Description:
This is the class to handle the rifle.
"""
from point import Point
from global_constants import *

class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.
    """
    def __init__(self):                          #constructor
        self.center = Point()
        self.center.x = 0.0
        self.center.y = 0.0
        self.angle = 45

    def draw(self):                             #draw out the rifle
        arcade.draw_rectangle_filled(self.center.x, self.center.y, RIFLE_WIDTH, RIFLE_HEIGHT, RIFLE_COLOR, self.angle)
