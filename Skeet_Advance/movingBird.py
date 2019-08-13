"""
Class: MovingBird
Author: Kwok Moon Ho

The class contain all the method of the moving bird

The moving bird is the player 2 which can move by the keyboard up,down,right,left arrow

if the bullet hit the moving bird, player 1 can score 10 point.

if the player 2 avoid the bullet and it's off the screen, player score 10 point
"""
import arcade
import random
from global_constants import *
from point import Point
from velocity import Velocity

class MovingBird:           ##constructor of the moving bird
    def __init__(self):
        self.center = Point
        self.velocity = Velocity
        self.center.x = SCREEN_HEIGHT / 2
        self.center.y = SCREEN_WIDTH / 2
        self.velocity.dx = 4
        self.velocity.dy = 4

    def draw_moving_bird(self):        ##draw the moving bird and it's raindow color
        self.color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        arcade.draw_circle_filled(self.center.x, self.center.y, TARGET_RADIUS, self.color)

    def move_up(self):                         ##handle the input move up
        if self.center.y + TARGET_RADIUS < SCREEN_HEIGHT:
            self.center.y += self.velocity.dy
            ##self.draw_moving_bird()

    def move_down(self):                       ##handle the input move down
        if self.center.y + TARGET_RADIUS > TARGET_RADIUS * 2:
            self.center.y -= self.velocity.dy
           ## self.draw_moving_bird()

    def move_left(self):                         ##handle the input move left
        if self.center.x + TARGET_RADIUS > TARGET_RADIUS * 2:
            self.center.x -= self.velocity.dx
           ## self.draw_moving_bird()

    def move_right(self):                       ##handle the input move right
        if self.center.x + TARGET_RADIUS < SCREEN_WIDTH:
            self.center.x += self.velocity.dx
          ##  self.draw_moving_bird()
