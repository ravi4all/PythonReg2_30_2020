class BMW:

    def __init__(self):
        self.gates = 4
        self.avg = 15
        self.topSpeed = 300
        self.color = "Red"
        self.airbag = 2

class BMWV2(BMW):

    def __init__(self):
        super().__init__()
        self.avg = 10
        self.topSpeed = 400
        self.gates = 2

    def baseDetails(self):
        print("Color : ",self.color)
        print("Airbags : ",self.airbag)
            
    def showDetails(self):
        print("Car Details : ")
        print("Average : ",self.avg)
        print("Top Speed : ",self.topSpeed)
        print("Number of gates : ",self.gates)

obj = BMWV2()
obj.showDetails()
obj.baseDetails()