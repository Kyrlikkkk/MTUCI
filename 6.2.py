class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return self.make, self.model

class Car(Vehicle):
    def __init__(self, make, model, fuel_type ):
        self.fuel_type = fuel_type
        super().__init__(make, model)

    def fuel(self):
        return super().get_info(), self.fuel_type

a=Vehicle('aa', 'bb')
b = Car('a', 'b',  'gas')
print(b.fuel())


