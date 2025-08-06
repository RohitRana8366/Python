#when one class(child/derived) derives the properties & methods of another class(parent/base).
class car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("your car start")

    @staticmethod
    def off():
        print("your car is off")

class mercedese(car):
    def __init__(self, name):
        self.name=name 

#multilevel inheritance
class benz(mercedese):
    def __init__(self, fueltype):
        self.fueltype=fueltype
        print("your fueltype is=",self.fueltype)
        
car1=benz("petrol")
print(car1.fueltype)         
print(car1.start())

#/multiple level inheritance
class a:
    vara="welcome to class a"
class b:
    varb="welcome to class b "
class  c(a,b):
    varc= "welcome to class c"

object=c()
print(object.varc)
print(object.varb)
print(object.vara)

 