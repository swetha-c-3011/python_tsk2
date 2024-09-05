from abc import abstractmethod


class Employee:

    def __init__(self,name):
        self.name=name

    @abstractmethod
    def calculate_salary():
        pass


    def describe(self,type):
        self.type=type
        print("name of the employee ",self.name,"type of the employee is ",self.type)



class FullTimeEmployee(Employee):

    def __init__(self,name):
        super().__init__(name)


    def calculate_salary(self):
        print("Montly salry is : 3000")



class PartTimeEmployee(Employee):

    def __init__(self,name,hours_worked,hourly_rate):
        super().__init__(name)

        self.hours_worked=hours_worked
        self.hourly_rate=hourly_rate


    def calculate_salary(self):
        print("Salary is ",self.hours_worked*self.hourly_rate)

if __name__ == "__main__":
    try:
        choice=input("enter the type of Employee \n 1. FullTime \n 2. PartTime").lower().replace(" ","")

        if choice not in ["fulltime","parttime"]:
            raise ValueError
        name=input("enter your name").replace(" ","")
        if(name==""):
            raise ValueError
        if(choice=="fulltime"):


            objFullTime=FullTimeEmployee(name)
            objFullTime.describe(choice)
            objFullTime.calculate_salary()

        elif(choice=="parttime"):
            hours_worked = int(input("enter the hours you have worked"))
            hourly_rate = int(input("enter your hourly rate "))
            if(hours_worked <=0 and hourly_rate<=0  and (type(hours_worked) and type(hourly_rate)!=int ) ):
                raise ValueError
            else:
                objPartTime=PartTimeEmployee(name,hours_worked,hourly_rate)
                objPartTime.describe(choice)
                objPartTime.calculate_salary()
    except ValueError:
        print(" check the correctness of value")