"""
Author: Kwok Moon Ho
Class : Ship

The ship obeys the laws of motion. When in motion, the ship will tend to stay in motion.

Note that the angle or orientation of the ship can be different than the direction it is traveling.

The right and left arrows rotate the ship 3 degrees to either direction.

The up arrow will increase the velocity in the direction the ship is pointed by 0.25 pixels/frame.

For collision detection, you can assume the ship is a circle of radius 30.
"""
from flyingObject import FlyingObject
from global_constants import *
import arcade
import math

class Ship(FlyingObject):
    def __init__(self):                 ##constructor
        super().__init__(SHIP_RADIUS)
        self.center.x = SCREEN_WIDTH / 2
        self.center.y = SCREEN_HEIGHT / 2
        self.direction.angle = 0

    def draw(self):
        img = "images/ship.png"
        texture = arcade.load_texture(img)
        width = texture.width - 20
        height = texture.height - 20
        alpha = 1
        arcade.draw_texture_rectangle(self.center.x, self.center.y, width, height, texture, self.direction.angle, alpha)

    def move(self):         ##get the angle and the move
        self.velocity.dy += SHIP_THRUST_AMOUNT * math.cos(math.radians(self.direction.angle))
        self.velocity.dx -= SHIP_THRUST_AMOUNT * math.sin(math.radians(self.direction.angle))

    def turn_right(self):
        self.direction.angle -= SHIP_TURN_AMOUNT

    def turn_left(self):
        self.direction.angle += SHIP_TURN_AMOUNT

    def stop(self):         #stop !
        self.velocity.dx = 0
        self.velocity.dy = 0