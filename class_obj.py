# class student:
#     def __init__(self,name,regno) -> None:
#         self.name=name
#         self.regno=regno
#     def marks(self):
#         return "90"
# # creating a instance of a class         
# std1=student("varun",20)

# #accessing attributes and methods
# print(f"name:{std1.name}")
# print(f"regno:{std1.regno}")
# print(f"marks:{std1.marks()}")

# class rectangle:
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
# print("enter the length and breath of rect1")
# a,b=map(int,input().split())     
# rect1=(a,b)
# print("enter the length and breath of rect2")
# m,n=map(int,input().split())
# rect2=(m,n)
# if rect1>rect2:
#     print("rectangles 1 is greater than rectangle 2")
# else:
#     print("rectangles 2 is greater than rectangle 1")


# class point:
#     def __init__(self,x,y) -> None:
#         self.x=x
#         self.y=y
#     def quad(self):
#         if self.x>0 and self.y>0:
#             return "first quad"
#         elif self.x<0 and self.y>0:
#             return "second quad"
#         elif self.x<0 and self.y<0:
#             return "third quad"
#         elif self.x>0 and self.y<0:
#             return "fourth quad"
#         elif self.x==0 and self.y==0:
#             return "origin"
#         else:
#             return "axis"
# print("enter the x and y points")
# x,y=map(int,input().split())        
# p1=point(x,y)
# print(p1.quad())


class library:
    def __init__(self):
        self.acc_number=""
        self.publisher="" 
        self.title=""
        self.author=""
    def read(self):
        self.acc_number=input("enter acc_number:")
        self.publisher=input("enter publisher:")
        self.title=input("enter title:")
        self.author=input("enter author:")
    def compute(self):
        no_days=int(input("enter no_of_days_late:"))
        charge=no_days*1.50
        print(f"fine charge is {charge}")
    def dispaly(self):
        print(f"account number = {self.acc_number}")
        print(f"publisher = {self.publisher}")
        print(f"title = {self.title}")
        print(f"author = {self.author}")
    
std=library()
std.read()
std.dispaly()
std.compute()