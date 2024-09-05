from ElectronicDevice import ElectronicDevice
from ElectronicDevice import Laptop
from ElectronicDevice import Smartphone
class ElectronicDeviceMain:

    try:
        type = input("enter the type of device \n 1.Laptop \n 2.SmartPhone").replace(" ","").lower()
        if type not in["laptop","smartphone"]:
            raise ValueError
        if(type=="laptop"):
            brand=input("enter the brand ").lower().replace(" ","")
            model=input("enter the model ").lower().replace(" ","")
            batterylife = int(input("enter the batterylife "))
            if( brand=="" or batterylife==""):
                raise ValueError
            obj = ElectronicDevice.from_type(brand,model,type,batterylife)
            obj.describe(type)
            obj.power_uasge()

        elif(type=="smartphone"):
            brand = input("enter the brand ").lower().replace(" ", "")
            model = input("enter the model ").lower().replace(" ", "")
            screensize = float(input("enter the screensize "))
            if (   brand=="" or screensize==""):
                raise ValueError
            obj=ElectronicDevice.from_type(brand,model,type,screensize)
            obj.describe(type)
            obj.power_uasge()


    except ValueError:
        print("check corrcetness of your input")

