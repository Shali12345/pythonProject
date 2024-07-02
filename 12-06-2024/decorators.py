def my_decorator(func):
    def wrapper():
        print("Starting****")
        print("hey****")
        func()
        print("gehjj")
        print("jskjs")

        return wrapper()


@my_decorator

def say_hello():
    print("hello")

say_hello()