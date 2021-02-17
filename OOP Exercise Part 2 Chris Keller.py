import CarClass


def main():

    year_model = input("Enter the car's model year. ")
    make = input("Enter the car's make. ")

    car = CarClass.Car(year_model, make)

    acc_count = 1
    while acc_count <= 5:
        car.accelerate()
        print(car.get_speed())
        acc_count += 1

    brake_count = 1
    while brake_count <= 5:
        car.brake()
        print(car.get_speed())
        brake_count += 1


main()
