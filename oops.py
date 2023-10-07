class vechile:
    def __init__(self,model,year,regno) -> None:
        self.model=model
        self.year=year
        self.regno=regno
    def display(self):
        print("model=",self.model)
        print("year of manufacturing=",self.year)
        print("registration no=",self.regno)
v1=vechile("maruti",2014,"kA-43 MN 4559")
v2=vechile("honda",2022,"kA-53 NX 6759")
v1.model="harsha"
v1.display()
v2.display()