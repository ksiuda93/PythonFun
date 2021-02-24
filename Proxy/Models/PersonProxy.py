from .Person import Person


class PersonProxy(Person):

    def __init__(self) -> None:
        self.person = Person()

    def run_job(self) -> None:
        print("Add invoke function to logger")
        self.person.run_job()
