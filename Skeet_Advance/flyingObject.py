"""
Author: Kwok Moon Ho
class: flyingObject

This is the Base Class of the bullet and the bird
"""
from abc import ABC
from abc import abstractmethod
from point import Point
from velocity import Velocity
from global_constants import *

class FlyingObject(ABC):
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 0.0
        self.alive = True

    def advance(self):              ##handle the movement of the flying obj
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    @abstractmethod
    def draw(self):
        pass

    def is_off_screen(self):        ##check the function is off screen
        if self.center.x > SCREEN_WIDTH or self.center.y > SCREEN_HEIGHT or self.center.y < 0:
            return True
        return False
