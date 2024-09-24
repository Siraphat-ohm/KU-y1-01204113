import math


class Cylinder:
    def __init__(self, radius, height):
        self.r = radius
        self.h = height

    def get_radius(self):
        return self.r

    def get_height(self):
        return self.h

    def set_radius(self, r):
        self.r = r

    def set_height(self, h):
        self.h = h

    def get_base_area(self):
        return math.pi * self.r**2

    def get_volume(self):
        return math.pi * self.r**2 * self.h

    def __str__(self):
        return f"Radius: {self.r:.3f}, Height: {self.h:.3f}"
