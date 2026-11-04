class Bell:
    def __init__(self):
        self.color = 'white'
        self.sound = 'ding', 'dong'
        self.size = 'Standart'
        self.status = False

    def play(self):
        if not self.status:
            self.status = True
            return self.sound[0]
        self.status = False
        return self.sound[1]


class Big_bell(Bell):
    def __init__(self):
        super().__init__()
        self.size = 'Big'
        self.sound = 'DING', "DONG"


class Car:
    def __init__(self, model, hp, year, fuel, max_fuel, fuel_usage):
        self.model = model
        self.hp = hp
        self.year = year
        self.fuel = fuel
        self.max_fuel = max_fuel
        self.fuel_usage = fuel_usage

        self.engine_status = False

    def fuel_status(self):
        return self.fuel > 0

    def ignite(self):
        if self.fuel_status():
            self.engine_status = True

    def drive(self):
        if self.engine_status:
            return True

    def __str__(self):
        return f'Model - {self.model}, {self.year} year of release'

    def distance_left(self):
        if self.engine_status:
            return round((100 / self.fuel_usage) * self.fuel)

    def refill(self):
        self.fuel = self.max_fuel


car = Car(model='Ford Mustang', hp=500, year=1965, fuel=25, max_fuel=60, fuel_usage=12.7)
car.ignite()
print(car.distance_left())
