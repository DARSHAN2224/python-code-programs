class rect:
    def __init__(self,l,b) -> None:
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b 
    def compare(self,other):
        if self.area()==other.area():
            return 1
        else:
            return 0
    
rect1=rect(20,30)
rect2=rect(30,20)
if rect1.compare(rect2)==1:
    print("rectangles are equal")
else:
    print("area is not equal")