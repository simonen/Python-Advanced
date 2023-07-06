class Equipment:

    id = 0

    def __init__(self, name: str) -> None:
        self.name = name
        self.equipment_id = Equipment.get_next_id()

    @staticmethod
    def get_next_id():
        Equipment.id += 1
        return Equipment.id

    def __repr__(self):
        return f"Equipment <{self.equipment_id}> {self.name}"
