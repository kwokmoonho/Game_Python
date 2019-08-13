"""
Author: Kwok Moon Ho
Class: Bullet

This is the class of the bullet and contain all the mehtod of the bullet

Pressing space bar will shoot a bullet.

Bullets are should start with the same velocity of the ship (speed and direction) plus 10 pixels per frame in the direction the ship is pointed. This means if the ship is traveling straight up, but pointed directly to the right, the bullet will have a velocity that is at an angle up and to the right (starting with an upward velocity from the ship, and adding to it a velocity to the right because of the direction the ship is pointed).

There is no limit to the number of bullets that can be fired.

Bullets only live for 60 frames, after which they should "die" and be removed from the game.

For collision detection, you can assume that bullets have a radius of 30
"""
from global_constants import *
from flyingObject import FlyingObject
import arcade
import math

class Bullet(FlyingObject):
    def __init__(self, ship_x, ship_y, ship_angle):
        super().__init__(BULLET_RADIUS)
        self.life = 0
        self.center.x = ship_x
        self.center.y = ship_y
        self.direction.angle = ship_angle


    def advance(self):      ##set the life to be 0 and count to bullet_life
        if self.life > BULLET_LIFE:
            self.alive = False
        self.life += 1
        super().advance()


    def draw(self):
        img = "images/laser.png"
        texture = arcade.load_texture(img)
        width = texture.width
        height = texture.height
        alpha = 1
        arcade.draw_texture_rectangle(self.center.x, self.center.y, width, height, texture, self.direction.angle, alpha)

    def fire(self, ship_angle):     ##according to the ship angle which pass from the game.
        self.velocity.dx += BULLET_SPEED * math.sin(math.radians(ship_angle)) * -1
        self.velocity.dy += BULLET_SPEED * math.cos(math.radians(ship_angle))
