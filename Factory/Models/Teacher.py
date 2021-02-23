from .IPerson import IPerson

class Teacher(IPerson):

    def __init__(self):
        self.name = "Teacher class"

    def run_job(self):
        print(f"Hello {self.name}")
