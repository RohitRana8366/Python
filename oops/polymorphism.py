#Polymorphism allows the same method or operator to perform different tasks based on the context.
class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real, "i +", self.img, "j")
    def add(self, num2):
        newreal=self.real+ num2.real
        newimg = self.img +  num2.img
        return complex(newreal,newimg)

num1=complex(1,2)
num1.shownumber() 
num2=complex(3,4)
num2.shownumber() 
num3=num1.add(num2)
num3.shownumber()  

 