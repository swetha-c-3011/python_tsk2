from abc import abstractmethod
class ElectronicDevice:


    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        self.power_consumption_rate=0

    def describe(self,type):

            if(type.lower()=="laptop"):
                 print("the type you selected is laptop \n the brand is",self.brand,"\n the model is ",self.model)
            else:
                print("the type you selected is smartphone \n the brand is",self.brand,"\n the model is ",self.model)





    @classmethod
    def from_type(cls,brand,model,type,fourthParameter):
        if(type=="laptop"):




           return Laptop(brand,model,type,fourthParameter)

        elif(type=="smartphone"):

            return Smartphone(brand,model,type,fourthParameter)

    @abstractmethod
    def power_uasge(self):
        pass



class Laptop(ElectronicDevice):
    def __init__(self,  brand, model,type,batteryLife):
        super().__init__(brand, model)
        self.batteryLife=batteryLife
        self.type=type



    def power_uasge(self):
        self.power_consumption_rate = 50
        print("The consumption of power is",self.power_consumption_rate,"wats per hour")


class Smartphone(ElectronicDevice):
    def __init__(self, brand, model, type,screenSize):
        super().__init__(brand, model)
        self.screenSize=screenSize
        self.type=type

    def power_uasge(self):
        self.power_consumption_rate = 10
        print("The consumption of power is", self.power_consumption_rate, "wats per hour")