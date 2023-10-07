class father :
    def __init__(self,propertyvalue) -> None:
        self.propertyvalue=propertyvalue
        
    def display_property(self):
        print(f"property value ={self.propertyvalue}")
    
    
class mother:
    def __init__(self,gold) -> None:
        self.gold=gold
    def display_gold(self):
        print(f"gold={self.gold}")
    
class child(father,mother):
    def __init__(self,vechicle, propertyvalue,gold):
        self.vechicle=vechicle
        self.propertyvalue=propertyvalue
        self.gold=gold
    
        
    def display(self):
        print(f"vehicle = {self.vechicle}")

c1=child("bike","10 acer","2kg")
c1.display()
c1.display_gold()
c1.display_property()