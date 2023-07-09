from abc import ABC, abstractmethod
from project.animals.animal import Animal, Mammal
from project.food import Food, Vegetable, Fruit, Meat, Seed


mice_food = ['Vegetable', 'Fruit']
cat_food = ['Vegetable', 'Meat']


class Mouse(Mammal):
    def make_sound(self) -> str:
        return "Squeak"

    def feed(self, food: Food):
        food_given = food.__class__.__name__
        if food_given not in mice_food:
            return f"{self.__class__.__name__} does not eat {food_given}!"

        self.weight += food.quantity * 0.1
        self.food_eaten += food.quantity


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        food_given = food.__class__.__name__
        if food_given != 'Meat':
            return f"{self.__class__.__name__} does not eat {food_given}!"

        self.weight += food.quantity * 0.4
        self.food_eaten += food.quantity


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def feed(self, food):
        food_given = food.__class__.__name__
        if food_given not in cat_food:
            return f"{self.__class__.__name__} does not eat {food_given}!"

        self.weight += food.quantity * 0.3
        self.food_eaten += food.quantity


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        food_given = food.__class__.__name__
        if food_given != 'Meat':
            return f"{self.__class__.__name__} does not eat {food_given}!"

        self.weight += food.quantity
        self.food_eaten += food.quantity
