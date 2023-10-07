# class rect:
#     def __init__(self,l,b) -> None:
#         self.l=l
#         self.b=b
#     def area(self):
#         return self.l*self.b 
#     def __gt__(self,other):
#         if self.area()>other.area():
#             return True
#         else:
            
#             return False
    
# rect1=rect(20,30)
# rect2=rect(40,20)
# if rect1>rect2:
#     print("rectangles 1 is greater than rectangle 2")
# else:
#     print("rectangles 2 is greater than rectangle 1")
class rect:
    def __init__(self,l,b) -> None:
        self.l=l
        self.b=b
    # def area(self):
    #     return self.l*self.b 
    def __eq__(self,other):
        if self.l==other.l:
            return True
        else:
            
            return False
    
rect1=rect(20,30)
rect2=rect(20,20)
if rect1==rect2:
    print("equal")
else:
    print("not equal")