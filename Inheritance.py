import math

class shape(object):
    def __eq__(self,other):
        return self.area()==other.area()
    def __lt__(self,other):
        return self.area()<other.area()


class rectangle(shape):
    def __init__(self,side1,side2):
        self.side1=side1
        self.side2=side2
    def area(self):
        return self.side1*self.side2
    def perimeter(self):
        return 2*(self.side1+self.side2)

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius*self.radius
    def perimeter(self):
        return 2*math.pi*self.radius


class square(rectangle):
    def __init__(self,side):
        rectangle.__init__(self,side,side)
        
c=circle(2)
print(c.area())

r1=rectangle(4,1)
r=square(2)
print(r.area())

print(r==c)
print(r==r1)
