class Item:
    def __init__(self, d, u, p):
        self.__description = d
        self.__units = u
        self.__price = p

    def get_desc(self):
        return self.__description

    def get_num(self):
        return self.__units

    def get_price(self):
        return self.__price
