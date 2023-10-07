class shape:
    def __init__(self,fillcolor):
        self.fillcolor=fillcolor

class rectangle(shape):
    def __init__(self,l,b,fillcolor):
        super().__init__(fillcolor)
        self.l=l
        self.b=b
        # self.fillcolor=fillcolor
    def area(self):
        return self.l*self.b
    
class square (rectangle):
    def __init__(self, sides, fillcolor):
        super().__init__(sides,sides,fillcolor)
    
    def area(self):
        return super().area()

s1=square(5,"blue")
print(f"area of square is {s1.area()}")
print(f"fillcolor is {s1.fillcolor}")
       