class Customer:

    id = 0

    def __init__(self, name: str, address: str, email: str) -> None:
        self.name = name
        self.address = address
        self.email = email
        self.customer_id = Customer.get_next_id()

    @staticmethod
    def get_next_id() -> int:
        Customer.id += 1
        return Customer.id

    def __repr__(self):
        return f"Customer <{self.customer_id}> {self.name}; Address: {self.address}; Email: {self.email}"


