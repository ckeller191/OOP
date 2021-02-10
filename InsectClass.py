import random


class Insect:
    def __init__(self, w, l, f):
        self.__wings = w
        self.__legs = l
        self.__flight = f

    def flight(self):
        self.__flight = random.randint(1, 10)

    # can also return flight in the first flight function

    def get_flight(self):
        return self.__flight

    def get_wings(self):
        return self.__wings

    def get_legs(self):
        return self.__legs

    def __str__(self):
        return (
            "wings: "
            + str(self.__wings)
            + "\n"
            + "legs: "
            + str(self.__legs)
            + "\n"
            + "flight: "
            + str(self.__flight)
        )


# all this at the end is for the string method; not really what I did in the flight code, but learn it