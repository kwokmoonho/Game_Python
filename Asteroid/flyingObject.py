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
from angle import Angle

class FlyingObject(ABC):
    def __init__(self, radius):
        self.center = Point()
        self.velocity = Velocity()
        self.direction = Angle()
        self.radius = radius
        self.alive = True

    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        self.wrap()

    def wrap(self):
        if self.center.x > SCREEN_WIDTH:
            self.center.x = 0
        elif self.center.x < 0:
            self.center.x = SCREEN_WIDTH
        if self.center.y > SCREEN_HEIGHT:
            self.center.y = 0
        elif self.center.y < 0:
            self.center.y = SCREEN_HEIGHT

    @abstractmethod
    def draw(self):
        pass