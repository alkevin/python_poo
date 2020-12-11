from datetime import datetime
import random

# Vehicle class ##########


class Vehicle:
    """Classe définissant un vehicle caractérisée par :
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
               + ', nb km : ' + str(self.get_km()) + ', démarré : ' + str(self.get_condition()) + '}'

    def __str__(self):
        return 'Vehicle {\n\tmarque : ' + self.get_brand() \
               + '\n\tcouleur : ' + self.get_color() \
               + '\n\tannée : ' + str(self.get_year()) \
               + '\n\tnb km : ' + str(self.get_km()) \
               + '\n\tdémarré : ' + str(self.get_condition()) + '\n\t}'

# Moto class ##########


class Moto(Vehicle):
    """Classe définissant une Moto héritant de la class Vehicle caractérisée par :
        - type : type du véhicule
        - nb_wheel : nombre de roue du véhicule
        - nb_passenger : nombre de passagers disponible du véhicule
        - passengers : les passagers du véhicule
        - attach : condition du véhicule True = attaché False = détaché
        """

    def __init__(self, brand, color):
        Vehicle.__init__(self, brand, color)
        self._type = "Moto"
        self._nb_wheel = 2
        self._nb_passenger = 2
        self.passengers = []
        self._attach = False

    def get_type(self):
        return self._type

    def get_nb_wheel(self):
        return self._nb_wheel

    def get_nb_passenger(self):
        return self._nb_passenger

    def get_passengers(self):
        return self.passengers

    def available_space(self):
        if self.get_nb_passenger() > len(self.get_passengers()):
            return True
        else:
            return False

    def add_passenger(self, passenger):
        if self.available_space():
            self.passengers.append(passenger)
            print("=> Passenger added to moto vehicle successfully !")
        else:
            print("=> Couldn't add passenger to moto vehicle, No more available space !")

    def remove_passenger(self, passenger):
        if not self.available_space():
            self.passengers.remove(passenger)
            print("=> Remove passenger from moto vehicle successfully !")
        else:
            print("=> Couldn't remove passenger from moto vehicle, Available space empty !")

    def get_attach(self):
        return self._attach

    def set_attach(self, condition):
        if condition:
            print("=> Moto attached !")
        else:
            print("=> Moto detached !")
        self._attach = condition

    def goat(self, km):
        if self.get_passengers():
            if not self.get_attach():
                if random.randint(0, 100) <= 10:
                    print("=> Your have crashed dummy !")
                else:
                    self.roll(km)
            else:
                print("=> You can't goat, moto is attached !")
        else:
            print("=> You can't goat, moto have no passenger !")

    def start_engine(self):
        if not self.get_attach():
            if not self.get_condition():
                self.set_condition(True)
                print("=> Engine started !")
            else:
                print("=> Engine already started !")
        else:
            print("=> Detach moto before starting engine !")

    def __repr__(self):
        return '{type : ' + self.get_type() \
               + ', nb roues : ' + str(self.get_nb_wheel())\
               + ', nb passagers : ' + str(self.get_nb_passenger()) \
               + ', marque : ' + self.get_brand() \
               + ', couleur : ' + self.get_color() \
               + ', année : ' + str(self.get_year()) \
               + ', nb km : ' + str(self.get_km()) \
               + ', démarré : ' + str(self.get_condition()) \
               + ', attaché : ' + str(self.get_attach()) + '}'

    def __str__(self):
        return 'Moto {\n\ttype : ' + self.get_type() \
               + '\n\tnb roues : ' + str(self.get_nb_wheel()) \
               + '\n\tnb passagers : ' + str(self.get_nb_passenger()) \
               + '\n\tpassagers : ' + str(self.get_passengers()) \
               + '\n\tmarque : ' + self.get_brand() \
               + '\n\tcouleur : ' + self.get_color() \
               + '\n\tannée : ' + str(self.get_year()) \
               + '\n\tnb km : ' + str(self.get_km()) \
               + '\n\tdémarré : ' + str(self.get_condition()) \
               + '\n\tattaché : ' + str(self.get_attach()) + '\n\t}'

    def __len__(self):
        # return len(self.vehicules)
        return self.get_passengers().__len__()

# Car class ##########


class Car(Vehicle):
    """Classe définissant une voiture héritant de la class Vehicle caractérisée par :
        - type : type du véhicule
        - nb_wheel : nombre de roue du véhicule
        - nb_passenger : nombre de passagers du véhicule
        - passengers : les passagers du véhicule
        - meter_credit : le credit dans le parcmètre
        - use_credit : le credit utilisé
        - counter : compte le nombre d'instance
        """
    counter = 0

    def __init__(self, brand, color):
        Vehicle.__init__(self, brand, color)
        self._type = "Voiture"
        self._nb_wheel = 4
        self._nb_passenger = 5
        self.passengers = []
        self._meter_credit = 0
        self._use_credit = 0
        type(self).counter += 1

    def get_type(self):
        return self._type

    def get_nb_wheel(self):
        return self._nb_wheel

    def get_nb_passenger(self):
        return self._nb_passenger

    def get_passengers(self):
        return self.passengers

    def available_space(self):
        if self.get_nb_passenger() > len(self.get_passengers()):
            return True
        else:
            return False

    def add_passenger(self, passenger):
        if self.available_space():
            self.passengers.append(passenger)
            print("=> Passenger added to car vehicle successfully !")
        else:
            print("=> Couldn't add passenger to car vehicle, No more available space !")

    def remove_passenger(self, passenger):
        if not self.available_space():
            self.passengers.remove(passenger)
            print("=> Remove passenger from car vehicle successfully !")
        else:
            print("=> Couldn't remove passenger from car vehicle, Available space empty !")

    def get_meter_credit(self):
        return self._meter_credit

    def set_meter_credit(self, credit):
        self._meter_credit = credit

    def add_meter_credit(self, credit):
        print("=> you add " + str(credit) + " credit successfully !")
        self._meter_credit += credit

    def get_use_credit(self):
        return self._use_credit

    def use_meter_credit(self, credit):
        if self.get_meter_credit() >= credit:
            if not (self.get_meter_credit()) - credit <= 0:
                print("=> You have enought credit !")
                self._meter_credit -= credit
                print("=> Meter credit decremente by " + str(credit) + " credit !")
                self._use_credit += credit
                print("=> Used credit increment by " + str(credit) + " credit !")
            else:
                print("=> Can't reach 0, add credit ! ")
        else:
            print("=> You haven't enought credit !")

    def __repr__(self):
        return '{type : ' + self.get_type() \
               + ', nb roues : ' + str(self.get_nb_wheel())\
               + ', nb passagers : ' + str(self.get_nb_passenger()) \
               + ', marque : ' + self.get_brand() \
               + ', couleur : ' + self.get_color() \
               + ', année : ' + str(self.get_year()) \
               + ', nb km : ' + str(self.get_km()) \
               + ', démarré : ' + str(self.get_condition()) \
               + ', compteur d''instance : ' + str(type(self).counter) + '}'

    def __str__(self):
        return 'Car {\n\ttype : ' + self.get_type() \
               + '\n\tnb roues : ' + str(self.get_nb_wheel()) \
               + '\n\tnb passagers : ' + str(self.get_nb_passenger()) \
               + '\n\tpassagers : ' + str(self.get_passengers()) \
               + '\n\tmarque : ' + self.get_brand() \
               + '\n\tcouleur : ' + self.get_color() \
               + '\n\tannée : ' + str(self.get_year()) \
               + '\n\tnb km : ' + str(self.get_km()) \
               + '\n\tdémarré : ' + str(self.get_condition()) \
               + '\n\tcompteur d''instance : ' + str(type(self).counter) + '\n\t}'

    def __len__(self):
        # return len(self.vehicules)
        return self.get_passengers().__len__()

    def __del__(self):
        type(self).counter -= 1


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