import math
import pygame

class Robot:
    def __init__(self, name):
        self.name = name
        self.weapon = "Fist"
        self.health = 100
        self.power_level = 0
        self.attack_power = 0
        self.status = 'Active'

    def attack_dino(self, dino_obj):
        if self.health != 0 and self.power_level <= 0:
            self.status = 'Resting'
            return 'Resting, cannot attack'
        elif self.health <= 0:
            self.status = 'Defeated'
            return 'Defeated, cannot attack'
        elif dino_obj.health <= 0:
            dino_obj.health = 0
            dino_obj.energy = 0
            dino_obj.attack_power = 0
            dino_obj.status = 'Defeated'
            return 'Defeated, cannot be attacked'
        else:
            dino_obj.health -= math.ceil(self.attack_power / 4)
            self.power_level = self.power_level - 10

    def choose_weapon(self, available_weapons):
        weapon_choice = input("Select weapon from available list: ")
        if weapon_choice not in available_weapons:
            input("Must select from list, try again: ")
        else:
            self.weapon = weapon_choice

    def __repr__(self):
        return f'Robo * {self.name} - Weapon: {self.weapon}, Health: {self.health}, ' \
               f'Power: {self.power_level}, Attack: {self.attack_power}, Status: {self.status}'
