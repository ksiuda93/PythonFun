def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}"


def parent():
    print(f"Parent function")

    def child_one():
        print(f"Child function1")

    def child_twice():
        print(f"Child function2")

    child_one()
    child_twice()


def greet_bob(f):
    return f("Bob")


if __name__ == "__main__":
    parent()
