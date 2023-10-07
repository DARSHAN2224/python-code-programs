class vehicle:
    def __init__(self,regno):
        self.regno=regno
    def display(self):
        print(f"vehicle registration no: {self.regno}")
class car(vehicle):
    def __init__(self, regno,model,color):
        # super().__init__(regno)
        self.regno=regno
        self.model=model
        self.color=color
    def display(self):
        # super().display()
        print(f"vechicle registration no:{self.regno}")
        print(f"model name:{self.model}")
        print(f"vechicle color:{self.color}")
martuti = car("KA04MN2447","maruti alto","silver")
tata=car("KA40N3449","tata nano","blue")
martuti.display()
tata.display()
