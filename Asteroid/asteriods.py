"""
Author: Kwok Moon Ho
Class: Asteriods

Asteriods is the base class of three different kind of asteriods
Big Asteriods contain all the method of the big asteriods
Medium asteriods contain all the method of the medium asteriods
Small asteriods contain all the method of the small asteriods

Asteroids

There are 3 types of asteroids in the game:

Large Asteroids

Moves at 1.5 pixels per frame, at a random initial direction.

Rotates at 1 degree per frame.

For collision detection, can be treated as a circle with radius 15.

If a large asteroid gets hit, it breaks apart and becomes two medium asteroids and one small one.

The first medium asteroid has the same velocity as the original large one plus 2 pixel/frame in the up direction.

The second medium asteroid has the same velocity as the original large one plus 2 pixel/frame in the down direction.

The small asteroid has the original velocity plus 5 pixels/frame to the right.

Medium Asteroid

Rotates at -2 degrees per frame.

For collision detection, can be treated as a circle with radius 5.

If hit, it breaks apart and becomes two small asteroids.

The small asteroid has the same velocity as the original medium one plus 1.5 pixels/frame up and 1.5 pixels/frame to the right.

The second, 1.5 pixels/frame down and 1.5 to the left.

Small Asteroid

Rotates at 5 degrees per frame.

For collision detection, can be treated as a circle with radius 2.

If a small asteroid is hit, it is destroyed and removed from the game.

"""
from global_constants import *
from flyingObject import FlyingObject
from abc import abstractmethod
from abc import ABC
import arcade

class Asteriods(FlyingObject,ABC):
    def __init__(self, radius, x, y, dx, dy):       ##constructor
        super().__init__(radius)
        self.spin = 0.0
        self.velocity.dx = dx
        self.velocity.dy = dy
        self.center.x = x
        self.center.y = y

    @abstractmethod
    def hit(self):
        pass


"""
Big Asteriods
"""
class BigAsteriods(Asteriods):
    def __init__(self, x, y, dx, dy):
        super().__init__(BIG_ROCK_RADIUS, x, y, dx, dy)

    def hit(self, list):
        self.alive = False
        list.append(MediumAsteriods(self.center.x, self.center.y, self.velocity.dx, self.velocity.dy + 2))
        list.append(MediumAsteriods(self.center.x, self.center.y, self.velocity.dx, self.velocity.dy - 2))
        list.append(SmallAsteriods(self.center.x, self.center.y, self.velocity.dx+5, self.velocity.dy))

    def draw(self):
        img = "images/big.png"
        texture = arcade.load_texture(img)
        width = texture.width
        height = texture.height
        alpha = 1
        self.spin += BIG_ROCK_SPIN
        arcade.draw_texture_rectangle(self.center.x, self.center.y, width, height, texture, self.spin, alpha)

"""
Medium Asteriods
"""
class MediumAsteriods(Asteriods):

    def __init__(self, x, y, dx, dy):
        super().__init__(MEDIUM_ROCK_RADIUS, x, y, dx, dy)

    def hit(self, list):
        self.alive = False
        list.append(SmallAsteriods(self.center.x, self.center.y, self.velocity.dx + 1.5, self.velocity.dy + 1.5))
        list.append(SmallAsteriods(self.center.x, self.center.y, self.velocity.dx - 1.5, self.velocity.dy - 1.5))


    def draw(self):
        img = "images/medium.png"
        texture = arcade.load_texture(img)
        width = texture.width
        height = texture.height
        alpha = 1
        self.spin += MEDIUM_ROCK_SPIN
        arcade.draw_texture_rectangle(self.center.x, self.center.y, width, height, texture, self.spin, alpha)

"""
Small Asteriods
"""
class SmallAsteriods(Asteriods):

    def __init__(self, x, y, dx, dy):
        super().__init__(SMALL_ROCK_RADIUS, x, y, dx, dy)

    def hit(self, list):
        self.alive = False

    def draw(self):
        img = "images/small.png"
        texture = arcade.load_texture(img)
        width = texture.width
        height = texture.height
        alpha = 1
        self.spin += SMALL_ROCK_SPIN
        arcade.draw_texture_rectangle(self.center.x, self.center.y, width, height, texture, self.spin, alpha)







