from copy import deepcopy


class Weapons:
    def __init__(self):
        self.weapon_list = ["Sword", "Cannon", "Fist", "Rock"]
        self.attack_list = ("Stomp", "Roar", "Bite")
        print(f'Available Weapons: {self.weapon_list}\nAvailable Attacks: {self.attack_list}\n')

    def choose_weapon(self, robo_obj):
        option_list = self.weapon_list.copy()
        weapon_choice = input(f'Select weapon from list for {robo_obj.name} : ')
        lower = []
        upper = []
        for item in option_list:
            lower.append(item.lower())
            lower.append(item.upper())
        while weapon_choice not in option_list and weapon_choice not in lower and weapon_choice not in upper:
            weapon_choice = input("Try again: ")
        else:
            robo_obj.weapon = weapon_choice.capitalize()

    def choose_attack(self, dino_obj):
        option_list = deepcopy(self.attack_list)
        attack_choice = input(f'Select weapon from list for {dino_obj.type} : ')
        lower = []
        upper = []
        for item in option_list:
            lower.append(item.lower())
            lower.append(item.upper())
        while attack_choice not in option_list and attack_choice not in lower and attack_choice not in upper:
            attack_choice = input("Try again: ")
        else:
            dino_obj.attack = attack_choice.capitalize()
