# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

# Базовый класс Animal
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def make_sound(self):
        pass
    
    def eat(self):
        pass

# Классы животных   
class Bird(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
    def make_sound(self):
        return "Чирик-чирик"
    
    def eat(self):
        return f"{self.name} ест зерно."
    
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color
        
    def make_sound(self):
        return "Ррр-ррр"
    
    def eat(self):
        return f"{self.name} ест мясо."
    
class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type
        
    def make_sound(self):
        return "Ш-ш-ш"
    
    def eat(self):
        return f"{self.name} ест насекомых."

# Классы сотрудников зоопарка        
class ZooKeeper():
    def __init__(self, name):
        self.name = name
        
    def feed_animal(self, animal):
        return f"{self.name} кормит {animal.name}."
    
class Veterinarian():
    def __init__(self, name):
        self.name = name
        
    def heal_animal(self, animal):
        return f"{self.name} лечит {animal.name}."

# Класс Zoo с композицией   
class Zoo():
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []
        
    def add_animal(self, animal):
        self.animals.append(animal)
        
    def add_employee(self, employee):
        self.employees.append(employee)

# Функция для демонстрации полиморфизма        
def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} издает звук: {animal.make_sound()}")       

# Демонстрация работы всех классов

# Создаем животных разных типов    
eagle = Bird("Орел", 5, "Коричневый")
lion = Mammal("Лев", 8, "Золотистый")
snake = Reptile("Змея", 2, "Гладкая")

# Создаем сотрудников зоопарка
keeper = ZooKeeper("Иван")
veterinarian = Veterinarian("Петр")

# Создаем зоопарк и добавляем животных и сотрудников
zoo = Zoo("Зоопарк")
zoo.add_animal(eagle)
zoo.add_animal(lion)
zoo.add_animal(snake)
zoo.add_employee(keeper)
zoo.add_employee(veterinarian)

# Выводим информацию о животных и сотрудниках
print("Животные в зоопарке:")
for animal in zoo.animals:
    print(f"- {animal.name}, возраст: {animal.age}, {getattr(animal, 'color', getattr(animal, 'fur_color', getattr(animal, 'scale_type', 'N/A')))}")

print("\nСотрудники зоопарка:")
for employee in zoo.employees:
    print(f"- {employee.name}")

# Выводим звуки животных
print("\nЗвуки животных:")
animal_sound(zoo.animals)
        