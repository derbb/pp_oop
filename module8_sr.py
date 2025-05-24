# 8.1
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def length(self):
        return round(2 * math.pi * self.radius, 1)

    def area(self):
        return round(math.pi * self.radius ** 2, 1)

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return round(self.side ** 2, 1)

class circle_in_square(Circle, Square):
    def __init__(self, side):
        Square.__init__(self, side)
        super().__init__(radius = round(side /2 , 1))

side_length = 10
figure = circle_in_square(side_length)

print(f"\nСторона квадрата: {figure.side}")
print(f"Радиус вписанной окружности: {figure.radius}")
print(f"Длина окружности: {figure.length()}")
print(f"Площадь окружности: {figure.area()}")
print(f"Площадь квадрата: {figure.area()}\n")

# 8.2

class Wheels:
    def __init__(self, count, diameter):
        self._count = count
        self._diameter = diameter

    def get_count_wheels(self):
        return self._count

    def get_diameter(self):
        return self._diameter

    def set_count(self, count):
        if count > 0:
            self._count = count
        else:
            print("Количество колёс должно быть положительным числом.")

class Doors:
    def __init__(self, count, material):
        self._count = count
        self._material = material

    def get_count_doors(self):
        return self._count

    def get_material(self):
        return self._material

class Engine:
    def __init__(self, power, type):
        self._power = power
        self._type = type

    def get_power(self):
        return self._power

    def get_type(self):
        return self._type

class Car(Wheels, Doors, Engine):
    def __init__(self, wheels_count, wheels_diameter, doors_count, doors_material, engine_power, engine_type):
        Wheels.__init__(self, wheels_count, wheels_diameter)
        Doors.__init__(self, doors_count, doors_material)
        Engine.__init__(self, engine_power, engine_type)

car = Car(4, 18.5, 4, "металл", 150, "бензиновый")

print("Количество колес:", car.get_count_wheels())
print("Диаметр колес:", car.get_diameter())
print("Количество дверей:", car.get_count_doors())
print("Материал дверей:", car.get_material())
print("Мощность двигателя:", car.get_power())
print("Тип двигателя:", car.get_type(), "\n")

# 8.3

class Pet:
    def __init__(self, name, breed):
        self._name = name
        self._breed = breed

    def get_name(self):
        return self._name

    def get_breed(self):
        return self._breed

    def get_sound(self):
        raise NotImplementedError("Этот метод должен быть реализован в подклассах.")

    def get_type(self):
        raise NotImplementedError("Этот метод должен быть реализован в подклассах.")

class Dog(Pet):
    def __init__(self, name, breed):
        super().__init__(name, breed)

    def get_sound(self):
        print("Гав!")

    def get_type(self):
        return "Собака"

class Cat(Pet):
    def __init__(self, name, breed):
        super().__init__(name, breed)

    def get_sound(self):
        print("Мяу!")

    def get_type(self):
        return "Кошка"

class Parrot(Pet):
    def __init__(self, name, breed):
        super().__init__(name, breed)

    def get_sound(self):
        print("Пик!")

    def get_type(self):
        return "Попугай"

class Hamster(Pet):
    def __init__(self, name, breed):
        super().__init__(name, breed)

    def get_sound(self):
        print("Писк!")

    def get_type(self):
        return "Хомяк"

dog = Dog("Бобик", "Лабрадор")
cat = Cat("Мурка", "Сиамская")
parrot = Parrot("Кеша", "Ара")
hamster = Hamster("Шустрик", "Русский карликовый")

dog.get_sound()
print(f"Имя: {dog.get_name()}, Тип: {dog.get_type()}, Порода: {dog.get_breed()}")

cat.get_sound()
print(f"Имя: {cat.get_name()}, Тип: {cat.get_type()}, Порода: {cat.get_breed()}")

parrot.get_sound()
print(f"Имя: {parrot.get_name()}, Тип: {parrot.get_type()}, Порода: {parrot.get_breed()}")

hamster.get_sound()
print(f"Имя: {hamster.get_name()}, Тип: {hamster.get_type()}, Порода: {hamster.get_breed()}")

# 8.4-5

class Employer:
    def __init__(self, first_name="", last_name="", age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print(self):
        print("\nThis is Employer class.")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}\n")

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, Age: {self.age}."

    def __int__(self):
        return self.age

class President(Employer):
    def __init__(self, first_name="", last_name="", age=0, country=""):
        super().__init__(first_name, last_name, age)
        self.country = country

    def print(self):
        print("\nPresident")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}\n")

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Age: {self.age}, Country: {self.country}"

    def __int__(self):
        return self.age

class Manager(Employer):
    def __init__(self, first_name="", last_name="", age=0, department=""):
        super().__init__(first_name, last_name, age)
        self.department = department

    def print(self):
        print("\nManager")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}\n")

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Age: {self.age}, Department: {self.department}."

    def __int__(self):
        return self.age

class Worker(Employer):
    def __init__(self, first_name="", last_name="", age=0, skill_level=""):
        super().__init__(first_name, last_name, age)
        self.skill_level = skill_level

    def print(self):
        print("\nWorker")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Skill Level: {self.skill_level}\n")

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Age: {self.age}, Skill Level: {self.skill_level}."

    def __int__(self):
        return self.age

president = President("Ivan", "Ivanov", 50, "Russia")
manager = Manager("Anna", "Petrova", 35, "Sales")
worker = Worker("Sergey", "Sidorov", 28, "Junior")

president.print()
print(president)
print(int(president))
manager.print()
print(manager)
print(int(manager))
worker.print()
print(worker)
print(int(worker))