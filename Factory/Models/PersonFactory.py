from .Student import Student
from .Teacher import Teacher


class PersonFactory():

    @staticmethod
    def create_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid type!")
        return -1
