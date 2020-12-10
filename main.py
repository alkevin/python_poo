# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import models

v1 = models.Vehicle('Fiat', 'red')
v2 = models.Vehicle('Mercedes', 'black')
h1 = models.Human("Foe", 18)
g1 = models.Garage(12)


def print_vehicle():
    # Use a breakpoint in the code line below to debug your script.
    print(v1)


def start_engine():
    print('# Start Engine #')
    v1.start_engine()


def stop_engine():
    print('# Stop Engine #')
    v1.stop_engine()


def roll():
    print('# Roll #')
    v1.roll(5)


def print_human():
    print('# Print Human #')
    print(h1)


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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_vehicle()
    start_engine()
    roll()
    stop_engine()
    print_human()
    human_start_car()
    human_stop_car()
    add_vehicle_to_human(v1)
    print_human()
    human_start_car()
    human_stop_car()
    print_garage()
    human_own_garage()
    print_human()
    print_garage()
    add_vehicle_garage()
    deposit_garage()
    print_garage()
    get_vehicle_garage()
    set_vehicle_garage()
    get_vehicle_garage()
    print_garage()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

