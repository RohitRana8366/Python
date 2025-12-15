class student:
    def __init__(self,physics,chemistry,maths):
        self.physics=physics
        self.chemistry=chemistry
        self.maths=maths
    @property
    def percentage(self):
        return str((self.physics+self.chemistry+self.maths)/3)+"%"

student1=student(93,97,98)
print(student1.percentage)
student1.physics=86
print(student1.physics)
print(student1.percentage)