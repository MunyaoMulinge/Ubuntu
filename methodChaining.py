#  method chaining - call several methods sequentially
class Car:
    def start_car(self):
        print("Car started")
        return self

    def drive_car(self):
        print("Start driving the car")
        return self

    def brake_car(self):
        print("Make the car come to a halt")
        return self

    def stop_car(self):
        print("Stop the car & turn off the engine")
        return self


car = Car()
car.start_car().drive_car().brake_car().stop_car()
