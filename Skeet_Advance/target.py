"""
Name: target
Author: Kwok Moon Ho
Description:
This class is to handle the targets

Standard Target

Rendered as a circle with a 20px diameter.

Destroyed with one hit.

1 point is awarded for hitting it.

Use the arcade.draw_circle_filled to assist you.

Strong Target

Rendered as a circle with a number inside of it.

The strong target should move more slowly than the others as defined below.

It takes 3 hits to destroy this target.

1 point is awarded for each of the first two hits.

5 points are awarded for the third hit that destroys the target.

Safe Target

Rendered as a square.

Use the arcade.draw_rectangle_filled function to assist you.

This target should not be hit.

It is destroyed with a single hit.

A penalty of 10 points is incurred if this target is hit.
"""
from flyingObject import FlyingObject
from global_constants import *
import random
import arcade
from abc import ABC
from abc import abstractmethod

"""
constructor and the parent class of 3 different type of targets
inheritance from the flying obj class
"""
class Targets(FlyingObject,ABC):
    def __init__(self, radius, life):
        super().__init__()
        self.radius = radius
        ##overwritting
        self.center.x = 0
        self.center.y = random.randint(SCREEN_HEIGHT / 4, SCREEN_HEIGHT)
        self.life = life
        self.velocity.horizontal_v()
        self.velocity.vertical_v()

    def hit(self, score):
        self.life -= 1
        if self.life == 0:
            self.alive = False
        return score



"""
standard target, 1 point per hit
"""
class StandardTarget(Targets):
    def __init__(self):
        super().__init__(TARGET_RADIUS, 1)

    def hit(self):
        return super().hit(1)

    def draw(self):
        arcade.draw_circle_filled(self.center.x,self.center.y,self.radius, TARGET_COLOR)

"""
StrongTarget class, it will move slowly than other targets.
"""
class StrongTarget(Targets):
    def __init__(self):                      ##constructor, and it will move slowly than other targets
        super().__init__(TARGET_RADIUS,3)
        self.score = 0
        self.velocity.dx = random.randint(1,3)
        self.velocity.dy = random.randint(-2,3)

    def hit(self):    ##first two hit got 2 point and the last hit get 1 point
        if self.life > 1:
            return super().hit(1)
        else:
            return super().hit(3)

    def draw(self):
        arcade.draw_circle_outline(self.center.x, self.center.y, self.radius, TARGET_COLOR)
        text_x = self.center.x - (self.radius / 2)
        text_y = self.center.y - (self.radius / 2)
        arcade.draw_text(repr(self.life), text_x, text_y, TARGET_COLOR, font_size = 20)

"""
SafeTarget class, if hit, -10 point
"""
class SafeTarget(Targets):
    def __init__(self):
        super().__init__(TARGET_SAFE_RADIUS * 2, 1)

    def hit(self):
        return super().hit(-10)

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, self.radius, self.radius, TARGET_SAFE_COLOR)



