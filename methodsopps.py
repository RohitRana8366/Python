class student:
    def __init__(self, name, marks):
        self.name=name 
        self.marks=marks 
    def hello(self):
        print("welcome student,",self.name)
    def get_marks(self ):
        return self.marks
s1=student('karan',99)
s1.hello()
print(s1.get_marks())