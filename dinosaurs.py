import math


class Dinosaur:
    def __init__(self, type_dino):
        self.type = type_dino
        self.attack = 'Stomp'
        self.health = 100
        self.energy = math.ceil(100)
        self.attack_power = 80

    def attack_robo(self, robo_obj):
        if self.health == 0 or self.energy == 0:
            return "Health/Energy depleted"
        elif robo_obj.health <= 0:
            robo_obj.health = 0
            robo_obj.attack_power = 0
            robo_obj.power_level = 0
        else:
            robo_obj.health -= math.ceil(self.attack_power / 4)
            self.energy -= 10

        def stat_check(robo_obj):
            if robo_obj.health <= 0:
                robo_obj.health = 0
            elif robo_obj.power_level <= 0:
                robo_obj.power_level = 0
            elif robo_obj.attack_power <= 0:
                robo_obj.attack_power = 0

        stat_check(robo_obj)

    def __repr__(self):
        return f'Dino * {self.type} - Attack: {self.attack}, Health: {self.health}, ' \
               f'Energy: {self.energy}, Attack Power: {self.attack_power}'
