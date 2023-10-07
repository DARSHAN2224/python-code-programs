from math import sqrt
class quad:
    def __init__(self,a,b,c) -> None:
        self.a=a
        self.b=b
        self.c=c
        
    def roots(self):
        d=self.b**2-4*self.a*self.c
        if d>0:
            print("roots are real and distict")
            print("the roota are:")
            x1=(-self.b+sqrt(d))/(2*self.a)
            x2=(-self.b-sqrt(d))/(2*self.a)
            print(f"roots1 is {x1:.2f}\n root2 is {x2:.2f}")
        elif d<0:
            print("roots are imaginary")
            print("the roota are:")
            x1=-self.b/2*self.a
            x2=sqrt(abs(d))/2*self.a
            print(f"roots1 is {x1}+i{x2:.2f}\n root2 is {x1}-i{x2:.2f}")
        else:
            x1=-self.b/2*self.a
            print(f"root1 == root2 =={x1:.2f}")
q1=quad(1,-4,4)
q1.roots()