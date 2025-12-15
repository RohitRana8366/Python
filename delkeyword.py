#used to delete object properties or object itself
class student:
    def __init__(self, name):
        self.name=name
        
s1=student("rohit")
del s1





class person:
    name="anonymous"

    def __say(self):
        print("hello")
    def welcome(self):
        self.__say()
        print("hello")
p1=person()
print(p1.name)
print(p1.welcome())