import math
class Dinosaurs:
    def __init__(self, type):
        self.type = type
        self.health = math.ceil(100)
        self.energy = math.ceil(100)
        self.attack_power = 80

    def __repr__(self):
        return f'{self.type} : Health: {self.health}, Energy: {self.energy}, Attack: {self.attack_power}'