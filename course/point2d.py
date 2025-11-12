from math import sqrt

class Point2D:
    def __init__(self,x:float,y:float) :
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return sqrt(self.x**2+self.y**2)
    
    def distance_2_points(self,other) :
        return sqrt((other.x-self.x)**2+(other.y-self.y)**2)

point_a = Point2D(3,3)
point_b = Point2D(4,3)
print(point_a.x)
print(point_a.distance_2_points(point_b))