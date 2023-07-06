class Trainer:

    id = 0

    def __init__(self, name: str) -> None:
        self.name = name
        self.trainer_id = Trainer.get_next_id()

    @staticmethod
    def get_next_id():
        Trainer.id += 1
        return Trainer.id

    def __repr__(self):
        return f"Trainer <{self.trainer_id}> {self.name}"
