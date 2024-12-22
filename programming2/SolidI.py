class Animal:
    def fly(self):
        pass

    def swim(self):
        pass


class Swimmable:
    def swim(self):
        pass

class Flyable:
    def fly(self):
        pass

class Bird(Flyable, Swimmable):
    def fly(self):
        print("Flying")

    def swim(self):
        print("Swimming")
