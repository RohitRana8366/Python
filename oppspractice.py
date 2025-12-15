#define a circle class to create a circle with radius r using the constructor. define an area() method of the circle define
#perimeter () method of the class which allows you to calculate the perimeter of the circle
class circle:
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def perimeter(self):
        return 2*3.14*self.radius
c1=circle(int(input("enter your radius")))
print("radius=",c1.radius)
print("area=",c1.area())
print("perimeter",c1.perimeter())

"""define an employee class with attribute role. department and salary.this method called show details() method"""

class employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showdetails(self):
        print("Role:", self.role)
        print("Department:", self.department)
        print("Salary:", self.salary)

# Input for employee object
role = input("Enter your role: ")
department = input("Enter your department: ")
salary = input("Enter your salary: ")

E1 = employee(role, department, salary)
print("\nEmployee Details:")
E1.showdetails()

# Define Engineer subclass
class engineer(employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75000")

    def showdetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().showdetails()

engg1 = engineer("Rohit Rana", "40")
print("\nEngineer Details:")
engg1.showdetails()
