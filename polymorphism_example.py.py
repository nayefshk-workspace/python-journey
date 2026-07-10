"""
Car Polymorphism Example

This program demonstrates the following Object-Oriented Programming (OOP)
concepts in Python:

- Inheritance
- Method Overriding
- Polymorphism
- Encapsulation

Each car brand provides its own implementation of the engine_sound()
method while sharing common behavior from the Car base class.
"""


class Car:
    """Base class representing a generic car."""

    def __init__(self, brand):
        """
        Initialize a Car object.

        Args:
            brand (str): Name of the car brand.
        """
        self.brand = brand
        self.start_count = 0

    def start(self):
        """
        Start the car and play the engine sound.
        """
        self.start_count += 1
        self.engine_sound()

    def engine_sound(self):
        """
        Display the default engine sound.

        This method is intended to be overridden by child classes.
        """
        print(f"{self.brand} is starting...")

    def show_start_count(self):
        """
        Display how many times the car has been started.
        """
        print(f"{self.brand} has been started {self.start_count} time(s).")


class BMW(Car):
    """Represent a BMW car."""

    def engine_sound(self):
        """Display BMW's engine sound."""
        print("BMW engine roars! 🏎️")


class Toyota(Car):
    """Represent a Toyota car."""

    def engine_sound(self):
        """Display Toyota's engine sound."""
        print("Toyota starts smoothly. 🚗")


class Tesla(Car):
    """Represent a Tesla car."""

    def engine_sound(self):
        """Display Tesla's engine sound."""
        print("Tesla powers on silently. ⚡")


def main():
    """Run the polymorphism demonstration."""

    cars = [
        BMW("BMW"),
        Toyota("Toyota"),
        Tesla("Tesla"),
    ]

    for car in cars:
        car.start()
        car.show_start_count()
        print("-" * 30)


if __name__ == "__main__":
    main()