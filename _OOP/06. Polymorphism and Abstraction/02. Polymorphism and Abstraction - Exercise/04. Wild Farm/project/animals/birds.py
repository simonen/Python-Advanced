from abc import ABC, abstractmethod
from project.animals.animal import Bird


class Owl(Bird):

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        food_given = food.__class__.__name__
        if food_given != 'Meat':
            return f"{self.__class__.__name__} does not eat {food_given}!"

        self.weight += food.quantity * 0.25
        self.food_eaten += food.quantity


class Hen(Bird):

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.weight += food.quantity * 0.35
        self.food_eaten += food.quantity