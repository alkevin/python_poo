# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import models

v1 = models.Vehicle('Fiat', 'red')
v2 = models.Vehicle('Mercedes', 'black')
h1 = models.Human("Foe", 18)
g1 = models.Garage(12)
m1 = models.Moto('Ducati', 'red')
h2 = models.Human("John", 45)
c1 = models.Car('Volvo', 'vert')
h3 = models.Human("John", 70)
h4 = models.Human("Doe", 30)
h5 = models.Human("Marie", 10)
h6 = models.Human("Curie", 52)


def wtprint(type, wtp):  # wtp = what to print
    if type == "vehicle":
        print('# Print Vehicle #')
        print(wtp)
    elif type == "human":
        print('# Print Human #')
        print(wtp)
    elif type == "moto":
        print('# Print Moto #')
        print(wtp)
    elif type == "car":
        print('# Print Car #')
        print(wtp)
    elif type == "garage":
        print('# Print Garage #')
        print(wtp)


def start_engine():
    print('# Start Engine #')
    v1.start_engine()


def stop_engine():
    print('# Stop Engine #')
    v1.stop_engine()


def roll():
    print('# Roll #')
    v1.roll(5)


def add_vehicle_to_human(vehicle):
    print('# add Vehicle to Human #')
    h1.set_vehicle(vehicle)


def human_start_car():
    print('# Human start car #')
    h1.start_vehicle()


def human_stop_car():
    print('# Human stop car #')
    h1.stop_vehicle()


def print_garage():
    print('# Print garage #')
    print(g1)


def human_own_garage():
    print('# Human own garage #')
    h1.set_garage(g1)


def deposit_garage():
    print('# Deposer garage #')
    h1.deposit_garage()


def add_vehicle_garage():
    print('# Add vehicle to garage #')
    g1.__add__(v1)


def get_vehicle_garage():
    print('# Get vehicle from garage #')
    print(g1.__getitem__(0))


def set_vehicle_garage():
    print('# Set vehicle in garage #')
    g1.__setitem__(0, v2)


def attach_moto(condition):
    print('# Attach moto #')
    m1.set_attach(condition)


def goat():
    print('# Goat moto #')
    m1.goat(5)


def start_moto():
    print('# Start moto engine #')
    m1.start_engine()


def add_passenger(type, passenger):
    if type == "moto":
        print('# Add passenger to moto #')
        m1.add_passenger(passenger)
    elif type == "car":
        print('# Add passenger to car #')
        c1.add_passenger(passenger)


def remove_passenger(type, passenger):
    if type == "moto":
        print('# Remove passenger to moto #')
        m1.remove_passenger(passenger)
    elif type == "car":
        print('# Remove passenger to car #')


def add_meter_credit(car, credit):
    print('# Add meter credit to car #')
    car.add_meter_credit(credit)


def use_meter_credit(car, credit):
    print('# Use credit meter car #')
    car.use_meter_credit(credit)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    wtprint("vehicle", v1)
    start_engine()
    roll()
    stop_engine()
    wtprint("human", h1)
    human_start_car()
    human_stop_car()
    add_vehicle_to_human(v1)
    wtprint("human", h1)
    human_start_car()
    human_stop_car()
    wtprint("garage", g1)
    human_own_garage()
    wtprint("human", h1)
    wtprint("garage", g1)
    add_vehicle_garage()
    deposit_garage()
    wtprint("garage", g1)
    get_vehicle_garage()
    set_vehicle_garage()
    get_vehicle_garage()
    wtprint("garage", g1)
    wtprint("moto", m1)
    attach_moto(True)
    start_moto()
    wtprint("moto", m1)
    goat()
    attach_moto(False)
    goat()
    add_passenger("moto", h1)
    start_moto()
    goat()
    add_passenger("moto", h2)
    add_passenger("moto", h3)
    wtprint("moto", m1)
    wtprint("car", c1)
    add_passenger("car", h1)
    add_passenger("car", h2)
    add_passenger("car", h3)
    add_passenger("car", h4)
    add_passenger("car", h5)
    add_passenger("car", h6)
    add_meter_credit(c1, 50)
    use_meter_credit(c1, 25)
    use_meter_credit(c1, 25)
    use_meter_credit(c1, 50)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

