import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
p1 = Point (20,10)
p2 = Point (50,30)

a = 30
b = 20

d = math.sqrt((a*a)+(b*b))
print('거리={}'.format(d))