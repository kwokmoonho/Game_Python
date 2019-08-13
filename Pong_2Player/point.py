"""
Name: Point
Author: Kwok Moon Ho
Description:
This is the class to handle the point location of the ball, pong and the paddle.
"""
import random

class Point:
    def __init__(self):            ##constructor
        self.x = 0.0
        self.y = 0.0

    def reset_ball(self):          ##reset the position of the ball
        self.x = 200
        self.y = 150