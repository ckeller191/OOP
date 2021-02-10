import PhoneClass as c


def main():

    my_phone = c.Phone()

    my_phone.set_manufact()

    my_phone.set_model()

    my_phone.set_retail_price()

    print("The phone's manufacturer is ", my_phone.get_manufact())

    print("The model of the phone is ", my_phone.get_model())

    print("The retail price of the phone is $", my_phone.get_retail_price())


main()