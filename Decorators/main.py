def my_decorator(func):
    def wrapper():
        print("Inside the wrapper")
        func()
        print("After function")
    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)
