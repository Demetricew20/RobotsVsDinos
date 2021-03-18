

class Weapons:
    def __init__(self):
        self.weapon_list = ["Sword", "Laser Rifle", "Fist", "Rock"]
        print(f'Available Weapons: {self.weapon_list}\n')

    def choose_weapon(self, robo_obj):
        lst = self.weapon_list.copy()
        weapon_choice = input("Select weapon from list: ")
        while weapon_choice not in lst:
            weapon_choice = input("Try again: ")
        else:
            robo_obj.weapon = weapon_choice




