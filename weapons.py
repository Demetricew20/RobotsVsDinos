from copy import deepcopy

class Weapons:
    def __init__(self):
        self.weapon_list = ["Sword", "Cannon", "Fist", "Rock"]
        self.attack_list = ("Stomp", "Roar", "Bite")
        print(f'Available Weapons: {self.weapon_list}\nAvailable Attacks: {self.attack_list}\n')

    def choose_weapon(self, robo_obj):
        lst = self.weapon_list.copy()
        weapon_choice = input(f'Select weapon from list for {robo_obj.name} : ')
        while weapon_choice not in lst:
            weapon_choice = input("Try again: ")
        else:
            robo_obj.weapon = weapon_choice

    def choose_attack(self, dino_obj):
        lst = deepcopy(self.attack_list)
        attack_choice = input(f'Select weapon from list for {dino_obj.type} : ')
        while attack_choice not in lst:
            attack_choice = input("Try again: ")
        else:
            dino_obj.attack = attack_choice




