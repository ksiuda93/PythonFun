from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """Person method"""

class Student(IPerson):

    def __init__(self):
        self.name = "Default student"
    
    def person_method(self):
        print(f"I am {self.name}")

class Teacher(IPerson):

    def __init__(self):
        self.name = "Default Teacher"

    def person_method(self):
        print(f"I am teacher")

class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid type")
        return -1


if __name__ == "__main__":
    choice = input("What type do you want to create ?! ")
    person = PersonFactory.build_person(choice)
    person.person_method()

