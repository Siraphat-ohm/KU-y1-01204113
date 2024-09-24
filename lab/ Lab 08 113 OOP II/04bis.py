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


x1 = float(input("Enter x1 : "))
y1 = float(input("Enter y1 : "))
x2 = float(input("Enter x2 : "))
y2 = float(input("Enter y2 : "))

l = Line(x1, y1, x2, y2)

print(f"value of x1 on this line is {l.get_x1():.3f}")
print(f"value of x2 on this line is {l.get_x2():.3f}")
print(f"value of y1 on this line is {l.get_y1():.3f}")
print(f"value of y2 on this line is {l.get_y2():.3f}")

print("==========")

print("Check x and y are on this line ?")
x = float(input("Enter x : "))
y = float(input("Enter y : "))

if l.contains(x, y):
    print(f"x = {x:.3f} and y = {y:.3f} are on this line")
else:
    print(f"x = {x:.3f} and y = {y:.3f} are not on this line")

print(f"Distance between startPoint and endPoint is {l.get_distance():.3f}")

print("==========")

print("Find value of y that gives( x , y ) on this line")
x = float(input("Enter x : "))
y = l.get_y(x)
print(f"value of y is {y:.3f}")

if l.contains(x, y):
    print(f"( x , y ) = ( {x:.3f} , {y:.3f} ) on this line")
else:
    print(f"( x , y ) = ( {x:.3f} , {y:.3f} ) is not on this line")
