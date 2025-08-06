"""Implement of abstraction"""
class car:
    def __init__(self):
        self.acc=False
        self.clutch=False
        self.brk=False

    def start(self):
        self.acc=True
        self.clutch=True
        self.brk=True
        print("car started")
car1=car()
car1.start()

        