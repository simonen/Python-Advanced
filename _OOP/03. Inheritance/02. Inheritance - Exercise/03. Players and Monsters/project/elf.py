from project.hero import Hero


class Elf(Hero):

    def __init__(self, username: str, level: int):
        self.username = username
        self.level = level