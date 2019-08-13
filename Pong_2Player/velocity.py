"""
Name: velocity
Author: Kwok Moon Ho
Description:
This class is to handle the velocity of the object.
"""
import random

class Velocity:
    def __init__(self):            ##constructor
        self.dx = 3
        self.dy = 3

    def reset_velocity(self):      ##reset the velocity of the ball
        self.dx = random.randint(-3, 3)
        self.dy = random.randint(-3, 3)