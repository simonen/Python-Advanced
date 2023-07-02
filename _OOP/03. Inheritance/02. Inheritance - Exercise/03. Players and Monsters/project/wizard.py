from project.hero import Hero


class Wizard(Hero):

    def __init__(self, username: str, level: int):
        self.username = username
        self.level = level
