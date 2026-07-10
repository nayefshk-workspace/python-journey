class Car:
    def start(self):
        print("The car is starting...")


class BMW(Car):
    def start(self):
        print("BMW engine roars! 🏎️")


class Toyota(Car):
    def start(self):
        print("Toyota starts smoothly. 🚗")


class Tesla(Car):
    def start(self):
        print("Tesla powers on silently. ⚡")



bmw = BMW()
toyota = Toyota()
tesla = Tesla()


cars = [bmw, toyota, tesla]

for car in cars:
    car.start()

