"""
Author: Kwok Moon Ho
Class: Bullet

This is the class of the bullet and contain all the mehtod of the bullet
"""
from global_constants import *
from flyingObject import FlyingObject
import arcade
import math

class Bullet(FlyingObject):     ##constructor
    def __init__(self):
        super().__init__()

    def fire(self, angle):      ##tune the angle of the bullet
        self.velocity.dx += BULLET_SPEED * math.cos(math.radians(angle))
        self.velocity.dy += BULLET_SPEED * math.sin(math.radians(angle))

    def advance(self):          ##handle the movement of the bullet
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def draw(self):             ##draw the bullet
        arcade.draw_circle_filled(self.center.x, self.center.y, BULLET_RADIUS, BULLET_COLOR)

    def is_off_screen(self):    ##check if the bullet if off screen and kill it
        return super().is_off_screen()