from .IPerson import IPerson


class Person(IPerson):

    def run_job(self) -> None:
        print("Person job")
