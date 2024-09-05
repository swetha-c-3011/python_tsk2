from Vehicle import Vehicle
class Main:

        try:
            type1=input("Enter the type of vechile:\n Car Truck : ").lower().replace(" ","")

            obj=Vehicle.from_name(type1)
            obj.get_fuel_efficiency()
            obj.describe()


        except AttributeError:
            print("exception is handeled")






