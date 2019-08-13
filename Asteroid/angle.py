"""
Author: Kwok Moon Ho
Class: Angle
It use to determine the obj angle of movement
"""

class Angle:
    def __init__(self):     ##construction
        self.angle = 0.0

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, new_angle):
        self._angle = new_angle