class vehicle:
    def used_for(self):
        print("transportation")
        
class bike(vehicle):
    def no_of_wheels(self):
        print("2")
        
my_bike = bike()
my_bike.no_of_wheels()
my_bike.used_for()

class car(vehicle):
    def no_of_wheels(self):
        print("4")
        
my_car = car()
my_car.no_of_wheels()
my_car.used_for()