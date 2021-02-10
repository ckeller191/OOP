import InsectClass as c


def main():

    my_insect = c.Insect(2, 4, 0)
    # numbers as parameter b/c add w,l,f to init function in class code
    my_insect.flight()

    # can also just call flight fuction in print statement

    print("The miles this insect can fly is:", my_insect.get_flight())

    print("The insect has ", my_insect.get_wings(), " wings.")

    print("The insect has ", my_insect.get_legs(), " legs.")


main()
