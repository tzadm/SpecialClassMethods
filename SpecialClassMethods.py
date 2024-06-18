class House:
    def __init__(self, NumberOfFloors=0):
        self.NumberOfFloors = NumberOfFloors

    def setNewNumberOfFloors(self, floors):
        self.NumberOfFloors = int(floors)
        print(self.NumberOfFloors)


h1 = House()

h1.setNewNumberOfFloors(4)
