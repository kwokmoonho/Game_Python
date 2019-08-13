"""
Name: velocity
Author: Kwok Moon Ho
Description:
This class is to handle the velocity of the objects.
"""
import random

class Velocity:
    def __init__(self):            ##constructor
        self.dx = 0
        self.dy = 0

    def horizontal_v(self):
        self.dx = random.randint(1,5)

    def vertical_v(self):
        self.dy = random.randint(-2,5)
