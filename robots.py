from weapons import Weapons

class Robots(Weapons):
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
        self.health = 100
        self.power_level = 0
        self.attack_power = 0

    def __repr__(self):
        return f'{self.name} : Weapon: {self.weapon}, Health: {self.health}, Power: {self.power_level}, Attack: {self.attack_power}'

