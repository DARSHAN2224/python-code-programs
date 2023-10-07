class point:
    def __init__(self,x,y):
          self.x=x
          self.y=y
p1=point(3,6)
p2=point(5,6)

class circle:
    def __init__(self,point,radius):
         self.point=point
         self.radius=radius
    def __eq__(self,other) -> bool:
         if self.point.x==other.point.x and self.point.y==other.point.y:
              return True
         else:
              return False
         
c1=circle(p1,5)
c2=circle(p2,5)
print(c1==c2)