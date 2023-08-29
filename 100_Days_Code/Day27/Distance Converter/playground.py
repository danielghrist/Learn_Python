# CHALLENGE:  MODIFY THE ADD FUNCTION TO TAKE AN UNLIMITED NUMBER OF ARGUMENTS
def add(*args):
    # sum = 0
    # for n in args:
    #     sum += n
    return sum(args)

# print(add(3, 5, 6, 10, 52))


def calculate(n=0, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # OR
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# print(calculate(2, add=3, multiply=5))

# CAN CREATE A CLASS WHICH TAKES *args and **kwargs
# CAN USE PASS THE KEYWORD ARGUMENT TO .get() FUNCTION TO GET
class Car():

    def __init__(self, **kwargs):
        # self.make = kw["make"]
        # OR
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", model="GT-R", dumb="stupid")
print(my_car.make)
print(my_car.model)
print(my_car.dumb)
