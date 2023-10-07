import math

class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self,other):
        d=math.sqrt((other.x-self.x)**2+(other.y-self.y)**2)
        return d
    def display(self):
        return f"({self.x},{self.y})"
    
p1=point(5,2)
p2=point(10,6)
print(f"distance between {p1.display()} and {p2.display()} ={p1.distance(p2):.2f}")