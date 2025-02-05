import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__X=x
        self.__Y=y

    def getx(self):
        return self.__X

    def gety(self):
        return self.__Y

    def distance_from_xy(self, x, y):
        return math.sqrt(math.pow(self.__X- x)+math.pow(self.__Y-y))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(),point.gety())


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))