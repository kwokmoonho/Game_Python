"""
Class: Paddle
Description:
This class is the paddle and contain all the method and instructor for the paddle
Author: Kwok Moon Ho
"""
import arcade
from point import Point

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
MOVE_AMOUNT = 5
SCREEN_HEIGHT = 300

class Paddle:
    def __init__(self,x,y):                        ##constructor
        self.center = Point()
        self.center.x = x
        self.center.y = y

    def draw(self):                            ##draw the paddle
        arcade.draw_rectangle_filled(self.center.x, self.center.y, PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.BLUSH)

    def move_up(self):                         ##handle the input move up
        if self.center.y + (PADDLE_HEIGHT/2) < SCREEN_HEIGHT:
            self.center.y += MOVE_AMOUNT
            self.draw()


    def move_down(self):                       ##handle the input move down
        if self.center.y + (PADDLE_HEIGHT/2) > 50:
            self.center.y -= MOVE_AMOUNT
            self.draw()

