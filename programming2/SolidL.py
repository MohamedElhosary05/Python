class Bird:
    def fly(self):
        print("Flying")

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")



class Bird:
    def move(self):
        print("Moving")

class FlyingBird(Bird):
    def fly(self):
        print("Flying")

class Penguin(Bird):
    def swim(self):
        print("Swimming")
