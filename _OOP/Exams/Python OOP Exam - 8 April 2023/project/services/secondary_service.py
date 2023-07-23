from project.services.base_service import BaseService


class SecondaryService(BaseService):

    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def details(self) -> str:
        res = [f"{self.name} Secondary Service:",
               f"Robots: {' '.join(map(lambda x: x.name, self.robots)) if self.robots else 'none'}"]

        return '\n'.join(res)
