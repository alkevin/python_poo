from datetime import datetime

# Vehicle class ##########


class Vehicle:
    """Classe définissant une voiture caractérisée par :
    - brand : marque du véhicule
    - color : couleur du véhicule
    - year : année de la date réel de la création du véhicule
    - km: nombre de kilomètres du véhicule
    - condition : état du véhicule True = démarré False = éteint
    """

    def __init__(self, brand, color):
        self._brand = brand
        self._color = color
        self._year = datetime.now().year
        self._km = 0
        self._condition = False

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = brand

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_year(self):
        return self._year

    def set_year(self, year):
        self._year = year

    def get_km(self):
        return self._km

    def set_km(self, km):
        self._km += km

    def get_condition(self):
        return self._condition

    def set_condition(self, condition):
        self._condition = condition

    def start_engine(self):
        if not self.get_condition():
            self.set_condition(True)
            print("=> Engine started !")
        else:
            print("=> Engine already started !")

    def stop_engine(self):
        if not self.get_condition():
            print("=> Engine already stopped !")
        else:
            self.set_condition(False)
            print("=> Engine stopped !")

    def roll(self, km):
        if self.get_condition():
            self.set_km(km)
            print("=> Your roll " + str(km) + " km !")
        else:
            print("=> Engine stopped, can't add km to counter !")

    def __repr__(self):
        return '{marque : ' + self.get_brand() + ', couleur : ' + self.get_color() \
               + ', année : ' + str(self.get_year()) \
               + ', nb km : ' + str(self.get_km()) + ', état : ' + str(self.get_condition()) + '}'

    def __str__(self):
        return 'Vehicle {\n\tmarque : ' + self.get_brand() \
               + '\n\tcouleur : ' + self.get_color() \
               + '\n\tannée : ' + str(self.get_year()) \
               + '\n\tnb km : ' + str(self.get_km()) \
               + '\n\tétat : ' + str(self.get_condition()) + '\n\t}'


# Human class ##########

class Human:
    """Classe définissant une voiture caractérisée par :
    - name : nom de la personne
    - age : age de la personne
    - vehicle : vehicule de la personne
    - garage : garage de la personne
    """

    def __init__(self, name, age, vehicle=None, garage=None):
        self._name = name
        self._age = age
        self.vehicle = vehicle
        self.garage = garage

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_vehicle(self):
        return self.vehicle

    def set_vehicle(self, vehicle):
        self.vehicle = vehicle
        print("=> Vehicle added to human successfully !")

    def start_vehicle(self):
        if self.vehicle:
            self.vehicle.start_engine()
        else:
            print("=> You need to have a car to start it !")

    def stop_vehicle(self):
        if self.vehicle:
            self.vehicle.stop_engine()
        else:
            print("=> You need to have a car to stop it !")

    def get_garage(self):
        return self.garage

    def set_garage(self, garage):
        self.garage = garage
        print("=> Garage added to human successfully !")
        self.garage.set_handler(self.get_name())

    def deposit_garage(self):
        if self.vehicle and self.garage:
            if self.garage.available_space():
                print("=> Deposit garage OK ! All conditions filled !")
                return True
        else:
            print("=> Deposit garage NOK :( !")
            return False

    def __repr__(self):
        return '{name : ' + self.get_name() + ', age : ' + str(self.get_age()) \
               + repr(self.get_vehicle()) \
               + repr(self.get_garage()) + '}'

    def __str__(self):
        return 'Human {\n\tname : ' + self.get_name() \
               + '\n\tage : ' + str(self.get_age()) \
               + '\n\t' + str(self.get_vehicle()) \
               + '\n\t' + str(self.get_garage()) + '\n}'


# Garage class ##########

class Garage:
    """Classe définissant une voiture caractérisée par :
    - handler : propriétaire du garage
    - capacity : capacité du garage
    - vehicles : liste des vehicules dans le garage
    """

    def __init__(self, capacity, handler=None):
        self.handler = handler
        self._capacity = capacity
        self.vehicles = []

    def get_handler(self):
        return self.handler

    def set_handler(self, handler):
        self.handler = handler
        print("=> Handler added to garage successfully !")

    def get_capacity(self):
        return self._capacity

    def set_capacity(self, capacity):
        self._capacity = capacity

    def get_vehicles(self):
        return self.vehicles

    def set_vehicles(self, vehicles):
        self.vehicles = vehicles
        print("=> Vehicles added to human successfully !")

    def available_space(self):
        if self.get_capacity() >= len(self.get_vehicles()):
            return True
        else:
            return False

    def __repr__(self):
        return '{handler : ' + repr(self.get_handler()) + ', capacity : ' + str(self.get_capacity()) \
               + ', vehicles : ' + repr(self.get_vehicles()) + '}'

    def __str__(self):
        return 'Garage {\n\thandler : ' + str(self.get_handler()) \
               + '\n\tcapacity : ' + str(self.get_capacity()) \
               + '\n\tvehicles : ' + str(self.get_vehicles()) + '\n\t}'

    def __add__(self, vehicle):
        if self.available_space():
            self.get_vehicles().append(vehicle)
            print("=> Vehicle added to garage successfully ! ")
        else:
            print("=> Can't add vehicle to garage - No more space !")

    def __len__(self):
        # return len(self.vehicules)
        return self.get_vehicles().__len__()

    def __getitem__(self, index):
        if not self.get_vehicles():
            print("=> No vehicles !")
        elif index > self.__len__():
            print("=> No vehicles !")
        else:
            return self.get_vehicles()[index]

    def __setitem__(self, index, vehicle):
        try:
            self.get_vehicles()[index] = vehicle
        except IndexError:
            print("=> Wrong index !")