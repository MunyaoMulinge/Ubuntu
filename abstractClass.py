from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("Drive Car")

    def stop(self):
        print("I'm seeing a pattern here")


class Motorcycle(Vehicle):
    def go(self):
        print("Ride motor cycle")

    def stop(self):
        print("Finally wrapping my head around it!")


#  vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()

car.stop()
motorcycle.stop()

