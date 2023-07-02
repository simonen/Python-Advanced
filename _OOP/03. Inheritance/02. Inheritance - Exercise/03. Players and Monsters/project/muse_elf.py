from project.elf import Elf


class MuseElf(Elf):

    def __init__(self, username: str, level: int):
        self.username = username
        self.level = level
