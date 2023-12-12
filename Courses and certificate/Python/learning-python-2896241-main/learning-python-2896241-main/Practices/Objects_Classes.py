class vehicule:
    color = "white"
    def __init__ (self, maxspeed, mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage
        self.seating_capacity = None
    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity
    def displayAll(self):
        print("Properties of the vehicule")
        print("----------------------------")
        print("Max speed: ",self.maxspeed)
        print("Mileage: ", self.mileage)
        print("Color: ", self.color)
        print("Seating Capacity: ", self.seating_capacity)
#Test case
vehicule1 = vehicule(120, 10500)
vehicule1.assign_seating_capacity(2)
vehicule1.displayAll()

vehicule2 = vehicule(120, 500)
vehicule1.assign_seating_capacity(8)
vehicule2.displayAll()
