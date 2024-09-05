from abc import abstractmethod


class Vehicle:
    def __init__(self,type):
        self.type=type;
    @abstractmethod
    def get_fuel_efficiency(self):
        pass

    def describe(self):
        if(self.type=="car"):
            print( "description of the vechivcle is car")
        else:
            print( "description of the vechivcle is truck")

    @classmethod
    def from_name(cls,type):
         if(type=="car"):
             return Car(type)
         elif(type=="truck"):
             return Truck(type)





class Car(Vehicle):
    def get_fuel_efficiency(self):
        print( "fuel efficiency of 25 miles per gallon.")


class Truck(Vehicle):
    def get_fuel_efficiency(self):
        print( "fuel efficiency of 15 miles per gallon.")



