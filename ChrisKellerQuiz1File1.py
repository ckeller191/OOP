class Course:
    def __init__(self, t, cr, ca, co):
        self.__title = t
        self.__crn = cr
        self.__capacity = ca
        self.__code = co

    def get_title(self):
        return self.__title

    def get_crn(self):
        return self.__crn

    def get_capacity(self):
        return self.__capacity

    def get_code(self):
        return self.__code