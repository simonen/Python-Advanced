from project.dark_wizard import DarkWizard


class SoulMaster(DarkWizard):

    def __init__(self, username: str, level: int):
        self.username = username
        self.level = level
