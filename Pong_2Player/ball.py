"""
Name: Ball
Author: Kwok Moon Ho
Description:
This is the calss to handle the ball object and contain all the method
"""
import arcade
import random
from point import Point
from velocity import Velocity
BALL_RADIUS = 10
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

class Ball:
    def __init__(self):                            ##constructor
        self.center = Point()
        self.velocity = Velocity()
        self.center.reset_ball()
        self.center.x = 200
        self.center.y = 150

    def draw(self):                                 ##to draw the ball object
        arcade.draw_circle_filled(self.center.x, self.center.y, BALL_RADIUS, (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)))

    def advance(self):                               ##to handle the ball object movement
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def bounce_horizontal(self):                     ## to handle the bounce of the ball in horizontal direction
        self.velocity.dx *= -1

    def bounce_vertical(self):                       ##to handle the bounce of the ball in vertical direction
        self.velocity.dy *= -1

    def restart(self):                               ##to restrat the ball in the game
        self.center.reset_ball()
        self.velocity.reset_velocity()
