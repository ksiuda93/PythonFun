from Models.PersonFactory import PersonFactory

if __name__ == "__main__":
    choice = input("What type do you want to create ?! ")
    person = PersonFactory.create_person(choice)
    person.run_job()
