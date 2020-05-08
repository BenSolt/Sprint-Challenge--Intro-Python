# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle: # base Class of everything, - ground, flight, starship
    pass

#GROUND

class GroundVehicle(Vehicle): #base class of car, motorcycle
    pass

class Car(GroundVehicle): # Base class - if there are models or makes of cars.
    pass
class motorcycle(GroundVehicle): # Base class - if there are models or makes of cars.
    pass

#AIR

class FlightVehicle(Vehicle0):

class Airplane(FlightVehicle): #Base class of 