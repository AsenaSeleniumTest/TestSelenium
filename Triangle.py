import math
from selenium import webdriver

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())
    

class Triangle:
    def __init__(self,v1,v2,v3):
        self.__v1 = v1
        self.__v2 = v2
        self.__v3 = v3
        
    def perimeter(self):
        dis1 = Point.distance_from_point(self.__v1,self.__v2)
        dis2 =Point.distance_from_point(self.__v1,self.__v3)
        dis3 =Point.distance_from_point(self.__v2,self.__v3)
        return dis1+dis2+dis3
    
    
            
            
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())        
            

                 