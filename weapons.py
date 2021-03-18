

class Weapons:
    def __init__(self):
        self.weapons = input("Select a weapon from the following [Sword, Laser Rifle, Fist, Rock]: ")
        self.attack = 0

    def weapon_types(self, attack):
        weapon_list = ["Sword", "Laser Rifle", "Fist", "Rock"]
        for element in weapon_list:
            if element == "Sword":
                self.attack = 50
            elif element == "Fist":
                self.attack = 15

