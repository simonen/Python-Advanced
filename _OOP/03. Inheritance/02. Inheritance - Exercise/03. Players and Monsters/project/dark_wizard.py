from project.wizard import Wizard


class DarkWizard(Wizard):

    def __init__(self, username: str, level: int):
        self.username = username
        self.level = level
