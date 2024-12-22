# Single Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, dob):
        super().__init__(name, age)
        self.dob = dob

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, DOB: {self.dob}")

student = Student("Mohamed", 23, "16-03-2000")
student.display()
student.display_info()


# Multiple Inheritance
class Base1:
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1 Constructor")


class Base2:
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2 Constructor")


class Derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived Constructor")

    def print_strings(self):
        print(f"String1: {self.str1}, String2: {self.str2}")

derived = Derived()
derived.print_strings()


# Multilevel Inheritance
class Base:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Child(Base):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def get_age(self):
        return self.age


class GrandChild(Child):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address

    def get_address(self):
        return self.address

grandchild = GrandChild("Geek1", 23, "Noida")
print(f"Name: {grandchild.get_name()}, Age: {grandchild.get_age()}, Address: {grandchild.get_address()}")
