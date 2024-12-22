# Public Access Modifier Example
class Person:
    def __init__(self, name ):
        self.name = name  

    def display(self):
        print(f"Name: {self.name}")


person = Person("Khalid")
print(f"Name: {person.name}")
person.display()


# Protected Access Modifier Example
class Student:

    def __init__(self, name):
        self._name = name

    def _display_name(self):
        print(f"name: {self._name}")


class Geek(Student):
    def __init__(self, name):
        super().__init__(name)

    def display_details(self):
        self._display_name()


geek = Geek("Ali")
print("Protected Access Example:")
geek.display_details()

# Private Access Modifier Example
class GeekPrivate:
    __name = None  

    def __init__(self, name):
        self.__name = name

    def __display_details(self):
        print(f"Name: {self.__name}")

    def access_private_function(self):
        self.__display_details()

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

geek_private = GeekPrivate("Osama")
geek_private.access_private_function()
