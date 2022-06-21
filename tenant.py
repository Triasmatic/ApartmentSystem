class Tenant:
    
    def __init__(self, name, num) -> None:
        self.name = name
        self.num = num
        self.payments = []
        return
    
    
    def __repr__(self):
        return f'Name: {self.num},Room: {self.name}'