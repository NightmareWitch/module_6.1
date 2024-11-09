class Animal:
    '''
    Родительсский класс Животные
    '''

    def __init__(self, name):
        self.alive = True  # Живой
        self.fed = False  # Накормленный
        self.name = name  # Название животного

    def eat(self, food):  # Кормим
        if isinstance(food, Plant):
            if food.edible:
                print(f'{self.name} съел {food.name}')
                self.fed = True
            else:
                print(f'{self.name} не стал есть {food.name}')
                self.alive = False
        else:
            print(f'{food} не относится к классу Plant')


class Plant:
    '''
    Родительский класс Растения
    '''

    def __init__(self, name):
        self.edible = False
        self.name = name


class Mammal(Animal):
    '''
    Дочерний класс Млекопитающие (От класса животные)
    '''
    pass


class Predator(Animal):
    '''
    Дочерний класс Хищиники (От класса животные)
    '''
    pass


class Flower(Plant):
    '''
    Дочерний класс Цветы (От класса Растения)
    '''
    pass


class Fruit(Plant):
    '''
    Дочерний класс Фрукты (От класса Растения)
    '''

    def __init__(self, name):  # Переопределяем
        super().__init__(name)
        self.edible = True


# Программа для проверки
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.