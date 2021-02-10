class Phone:
    def __init__(self):
        self.__manufact = ""
        self.__model = ""
        self.__retail_price = 0

    def set_manufact(self):
        self.__manufact = input("Who is the manufacturer of the phone? ")

    def set_model(self):
        self.__model = input("What model is the phone? ")

    def set_retail_price(self):
        self.__retail_price = float(input("What is the phone's retail price? "))

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price
