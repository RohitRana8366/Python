"""reate student class that takes name & marks of 3 subjects asargument in constructor. then create a method to print the average with use 
 """

class student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def hello():
        print("hello")
    
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hie",self.name,"your avg score is ",sum/3)
s1=student("tony stark",[99,98,97])
s1.get_avg()
s1.hello()

