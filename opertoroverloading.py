import math
class circle:
    def __init__(self,x,y,radius) -> None:
        self.x=x
        self.y=y
        self.radius=radius
        
    def area(self):
        area=math.pi*self.radius**2
        return area
    def __eq__(self, object):
        if self.area()==object.area():
            return True
        else:
            return False
    """
    __gt__ -> for greater than
    __lt__ -> for lesser than
    __ge__ -> for greater than or equal to 
    __le__ -> for lesser than or equal to
    __add__-> for adding two circle
    """
        
c1=circle(0,0,5)
c2=circle(1,1,5)
if c1==c2:
    print("cirlce are equal")
else:
    print("cirlce are not equal")