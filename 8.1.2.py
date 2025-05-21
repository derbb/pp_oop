from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def max_speed(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

class Car(Transport):
    def __init__(self, name, speed, fuel):
        super().__init__(name)
        self.speed = speed
        self.fuel = fuel

    def max_speed(self):
        return f"Максимальная скорость {self.name} — {self.speed} км/ч."

    def fuel_type(self):
        return f"{self.name} использует {self.fuel}."

class Motorcycle(Transport):
    def __init__(self, name, speed, fuel):
        super().__init__(name)
        self.speed = speed
        self.fuel = fuel

    def max_speed(self):
        return f"Максимальная скорость {self.name} — {self.speed} км/ч."

    def fuel_type(self):
        return f"{self.name} использует {self.fuel}."

car1 = Car("Skoda", 200, "бензин")
car2 = Car("Tesla", 250, "электричество")
motorcycle1 = Motorcycle("Kawasaki", 180, "бензин")
motorcycle2 = Motorcycle("Yamaha", 220, "бензин")

cars = [car1, car2]
motorcycles = [motorcycle1, motorcycle2]

for c, m in zip(cars, motorcycles):
    print("\n", c.max_speed())
    print(c.fuel_type())

    print("\n", m.max_speed())
    print(m.fuel_type())