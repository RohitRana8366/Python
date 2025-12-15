# to map with real world scenarios,we started using objects in code this called object oriented programming
class students:
    
    name="karan"
s1=students()
print(s1.name )  


class car:
    color="blue"
    brand="mercedese"
car1=car()
print(car1.color)
print(car1.brand)




class person:
    name="rohit rana"
    occupation="software engineer"
    networth=1000
    def info(self):# self is  that obkect which on methods calling
     print("this is a info of a person")


a=person()
a.name='nitesh'
a.occupation="neta"
print(a.name,a.occupation)
a.info()