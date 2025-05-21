from symtable import Class

class Vehicle:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def get_vehicle_type(self, wheels):
        if wheels == 2:
            return f"Это мотоцикл марки {self.name}."
        elif wheels == 3:
            return f"Это трицикл марки {self.name}."
        elif wheels == 4:
            return f"Это автомобиль марки {self.name}."
        else:
            return f"Я не знаю такого транспортного средства."

    def get_vehicle_advice(self):
        if self.mileage <= 50000:
            return f"Неплохо, {self.name} можно брать."
        elif 50000 < self.mileage <= 100000:
            return f"{self.name} надо внимательно проверить."
        elif 100000 < self.mileage <= 150000:
            return f"{self.name} надо провести полную диагностику."
        else:
            return f"{self.name} лучше не покупать."


# Создаем экземпляры
car1 = Vehicle("Kawasaki", 45000)
car2 = Vehicle("Skoda", 80000)
car3 = Vehicle("Stels", 120000)
car4 = Vehicle("Covini", 160000)

# Проверка методов
vehicles = [car1, car2, car3, car4]
wheels_list = [2, 4, 3, 6]

for v, wheels in zip(vehicles, wheels_list):
    print("\n", v.get_vehicle_type(wheels))
    print(v.get_vehicle_advice())