from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    def __init__(self, name, speed):
        super().__init__(name, speed)  # Calls the Horse's __init__ method to validate speed

    def _get_max_speed(self):
        return 120

    def train(self):
        max_speed = self._get_max_speed()
        self._speed += 2
        if self.speed > max_speed:
            self._speed = max_speed
