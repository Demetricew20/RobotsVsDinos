import math
from dinosaurs import Dinosaurs

class Robots(Dinosaurs):
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
        self.health = 100
        self.power_level = 0
        self.attack_power = 0

    def attack_dino(self, dino_obj):
        if dino_obj.health <= 0:
            dino_obj.health = "Defeated!"
            dino_obj.energy = "Defeated!"
            dino_obj.attack_power = "Defeated!"
        else:
            dino_obj.health -= math.ceil(self.attack_power / 4)



    def __repr__(self):
        return f'{self.name} : Weapon: {self.weapon}, Health: {self.health}, Power: {self.power_level}, Attack: {self.attack_power}'
