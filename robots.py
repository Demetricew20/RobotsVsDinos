import math

class Robot:
    def __init__(self, name):
        self.name = name
        self.weapon = "Fist"
        self.health = 100
        self.power_level = 0
        self.attack_power = 0



    def attack_dino(self, dino_obj):
        if self.health == 0 or self.power_level == 0:
            print("Energy/Health depleted")
        elif dino_obj.health <= 0:
            dino_obj.health = 0
            dino_obj.energy = 0
            dino_obj.attack_power = 0
        else:
            dino_obj.health -= math.ceil(self.attack_power / 4)
            self.power_level = self.power_level - 10

            def stat_check(dino_obj):
                if dino_obj.health <= 0:
                    dino_obj.health = 0
                elif dino_obj.energy <= 0:
                    dino_obj.energy = 0
                elif dino_obj.attack_power <= 0:
                    dino_obj.attack_power = 0

            stat_check(dino_obj)


    def choose_weapon(self, available_weapons):
        weapon_choice =  input("Select weapon from available list: ")
        if weapon_choice not in available_weapons:
            input("Must select from list, try again: ")
        else:
            self.weapon = weapon_choice

    def __repr__(self):
        return f'Robo * {self.name} - Weapon: {self.weapon}, Health: {self.health}, Power: {self.power_level}, Attack: {self.attack_power}'
