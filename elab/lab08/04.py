class Line:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        if x2 != x1:
            self.slope = (y2 - y1) / (x2 - x1)
        else:
            return

        self.y_intercept = self.slope * (self.x2 - self.x1) + self.y1

    def contains(self, x, y):
        return min(self.x1, self.x2) <= x <= max(self.x1, self.x2) and min(
            self.y1, self.y2
        ) <= y <= max(self.y1, self.y2)

    def get_distance(self):
        return ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5

    def get_x1(self):
        return self.x1

    def get_x2(self):
        return self.x2

    def get_y1(self):
        return self.y1

    def get_y2(self):
        return self.y2

    def get_y(self, x):
        if min(self.x1, self.x2) <= x <= max(self.x1, self.x2):
            return x * self.slope
        return -999.999


n = Line(1, 1, 4, 4)

print(f"{n.get_x1()} {n.get_y1()} {n.get_x2()} {n.get_y2()}")
print(n.contains(0.0, 0.0))
print(n.contains(1.0, 1.0))
print(n.contains(1.0, 0.0))
print(n.contains(0.0, 1.0))
print(n.contains(2.0, 0.0))
print(n.contains(0.0, 3.0))
print(n.get_distance())
print(n.get_y(3))
print(n.get_y(0))
