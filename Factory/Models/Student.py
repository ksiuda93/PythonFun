from .IPerson import IPerson

class Student(IPerson):

    def __init__(self):
        self.name = "Student class"

    def run_job(self):
        print(f"Hello {self.name}")
