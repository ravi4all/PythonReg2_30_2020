class BMW:

    def __init__(self):
        self.gates = 4
        self.avg = 15
        self.topSpeed = 300
        self.color = "Red"
        self.airbag = 2

    def baseDetails(self):
        print("Color : ", self.color)
        print("Airbags : ", self.airbag)

class BMWV2(BMW):

    def __init__(self):
        super().__init__()
        self.avg = 10
        self.topSpeed = 400
        self.gates = 2

    def showDetails(self):
        print("Car Details : ")
        print("Average : ", self.avg)
        print("Top Speed : ", self.topSpeed)
        print("Number of gates : ", self.gates)


class BMWV3(BMWV2):

    def __init__(self):
        super().__init__()
        self.automatic = "Yes"
        self.topSpeed = 500
        self.avg = 4
        self.self_driven = "Yes"

    # @override
    def showDetails(self):
        print("New Updates : ")
        print("Average : ", self.avg)
        print("Top Speed : ", self.topSpeed)
        print("Number of gates : ", self.gates)
        print("Automatic : ",self.automatic)
        print("Self Driven : ",self.self_driven)

obj = BMWV3()
obj.baseDetails()
obj.showDetails()