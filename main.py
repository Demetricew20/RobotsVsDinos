from robots import Robot
from dinosaurs import Dinosaur
from fleet import Fleet
from herd import Herd
from battlefield import Battlefield
from weapons import Weapons
from pygame_test import *
import ctypes

if __name__ == '__main__':

    #Battlefield
    battlefield = Battlefield()

    #Weapons
<<<<<<< HEAD
    # weapons = Weapons()
    def initialize_battle():
        #Select Battlefield
        #Weapons List
        weapons = Weapons()
        #Fighters
        marvin = Robot('Marvin')
        megaman = Robot('Megaman')
        wall_E = Robot('Wall-e')
        stegosaurus = Dinosaur('Stegosaurus')
        velociraptor = Dinosaur('Velociraptor')
        tyrannosaurus = Dinosaur('Tyrannosaurus')
        #Select Weapon/Attack
        weapons.choose_weapon(marvin)
        weapons.choose_weapon(megaman)
        weapons.choose_weapon(wall_E)

        weapons.choose_attack(stegosaurus)
        weapons.choose_attack(velociraptor)
        weapons.choose_attack(tyrannosaurus)

        #Robots
        marvin.power_level = 120
        marvin.attack_power = 70

        megaman.power_level = 110
        megaman.attack_power = 100

        wall_E.power_level = 100
        wall_E.attack_power = 60
        

        #Dinos
        stegosaurus.attack_power = 60

        velociraptor.attack_power = 80

        tyrannosaurus.attack_power = 100
        

        #Fleet
        robot_fleet = Fleet()
        robot_fleet.add_to_fleet([marvin, megaman, wall_E])
        # print(robot_fleet.fleet)

        #Herd
        dino_herd = Herd()
        dino_herd.add_to_herd([stegosaurus, velociraptor, tyrannosaurus])
        # print(dino_herd.herd)

        #Display fighters and battlefield
        display(battlefield)

# --- Fighters will attack each other randomly, last fighter standing wins!---
        def battle(fleet, herd):
            counter = 0
            for element in fleet:
                fleet_health = 0
                for i in range(0, len(element)):
                    fleet_health += element[i].health
                for obj in herd:
                    herd_health = 0
                    for a in range(0, len(obj)):
                        herd_health += obj[a].health
                    while counter <= 100 or fleet_health <= 0 or herd_health <= 0:
                        n = random.randint(0, 2)
                        i = random.randint(0, 2)
                        obj[n].attack_robo(element[n])
                        element[n].attack_dino(obj[i])
                        counter += 1

        battle(robot_fleet.fleet, dino_herd.herd)

        #Stats
        print(wall_E)
        print(megaman)
        print(marvin)
        print(stegosaurus)
        print(velociraptor)
        print(tyrannosaurus)

        def conclude_battle(robot_fleet, dino_herd):
            for element in robot_fleet.fleet:
                count = 0
                while count <= len(element):
                    for robot in element:
                        if robot.status == 'Defeated' or robot.status == 'Resting':
                            element.remove(robot)
                    count += 1

                if len(element) == 0:
                    return ctypes.windll.user32.MessageBoxW(0, 'Battle concluded: Dinos have won!',
                                                            'Robots vs Dinosaurs', 64)

            for element in dino_herd.herd:
                count = 0
                while count <= len(element):
                    for dino in element:
                        if dino.health <= 0 or dino.status == 'Resting':
                            element.remove(dino)
                    count += 1

                if len(element) == 0:
                    return ctypes.windll.user32.MessageBoxW(0, 'Battle concluded: Robos have won!',
                                                            'Robots vs Dinosaurs', 64)

            return ctypes.windll.user32.MessageBoxW(0, 'Battle is Ongoing!', 'Robots vs Dinosaurs', 64)

        conclude_battle(robot_fleet, dino_herd)
    
    initialize_battle()
=======
    weapons = Weapons()

    # Robots
    robot_wally = Robot("Wally")
    robot_wally.power_level = 50
    robot_wally.attack_power = 30
    weapons.choose_weapon(robot_wally)

    robot_megaman = Robot("Mega Man")
    robot_megaman.power_level = 110
    robot_megaman.attack_power = 120
    weapons.choose_weapon(robot_megaman)

    robot_marvin = Robot("Marvin")
    robot_marvin.power_level = 90
    robot_marvin.attack_power = 90
    weapons.choose_weapon(robot_marvin)

    #Dinos
    dino_one = Dinosaur("Tyrannosaurus")
    dino_one.attack_power = 150
    weapons.choose_attack(dino_one)

    dino_two = Dinosaur("Stegosaurus")
    dino_two.attack_power = 60
    weapons.choose_attack(dino_two)

    dino_three = Dinosaur("Velociraptor")
    dino_three.attack_power = 85
    weapons.choose_attack(dino_three)

    #Actions
    robot_megaman.attack_dino(dino_two)
    robot_megaman.attack_dino(dino_two)
    robot_megaman.attack_dino(dino_three)
    robot_megaman.attack_dino(dino_three)
    robot_megaman.attack_dino(dino_three)
    robot_marvin.attack_dino(dino_one)
    robot_marvin.attack_dino(dino_one)
    robot_marvin.attack_dino(dino_one)
    robot_marvin.attack_dino(dino_one)
    robot_marvin.attack_dino(dino_one)
    robot_marvin.attack_dino(dino_one)
    robot_marvin.attack_dino(dino_two)
    robot_marvin.attack_dino(dino_two)
    robot_marvin.attack_dino(dino_two)
    robot_marvin.attack_dino(dino_three)
    robot_marvin.attack_dino(dino_three)
    robot_marvin.attack_dino(dino_three)
    robot_marvin.attack_dino(dino_three)
    robot_marvin.attack_dino(dino_three)
    dino_two.attack_robo(robot_megaman)
    dino_two.attack_robo(robot_megaman)
    dino_two.attack_robo(robot_megaman)
    dino_one.attack_robo(robot_marvin)
    dino_one.attack_robo(robot_marvin)
    robot_marvin.attack_dino(dino_one)

    print(battlefield)
    print(robot_wally)
    print(robot_megaman)
    print(robot_marvin)
    print(dino_one)
    print(dino_two)
    print(dino_three)

    #Fleet
    robot_fleet = Fleet()
    robot_fleet.add_to_fleet([robot_megaman, robot_marvin, robot_wally])
    # print(robot_fleet.fleet)

    #Herd
    dino_herd = Herd()
    dino_herd.add_to_herd([dino_one, dino_two, dino_three])
    # print(dino_herd.herd)

    def conclude_battle(robot_fleet, dino_herd):
        for element in robot_fleet.fleet:
            count = 0
            while count <= len(element):
                for robot in element:
                    if robot.health <= 0:
                        element.remove(robot)
                count += 1

            if len(element) == 0:
                return ctypes.windll.user32.MessageBoxW(0, 'Battle concluded: Dinos have won!',
                                                        'Robots vs Dinosaurs', 64)

        for element in dino_herd.herd:
            count = 0
            while count <= len(element):
                for dino in element:
                    if dino.health <= 0:
                        element.remove(dino)
                count += 1

            if len(element) == 0:
                return ctypes.windll.user32.MessageBoxW(0, 'Battle concluded: Robos have won!',
                                                        'Robots vs Dinosaurs', 64)

        return ctypes.windll.user32.MessageBoxW(0, 'Battle is Ongoing!', 'Robots vs Dinosaurs', 64)

    conclude_battle(robot_fleet, dino_herd)
>>>>>>> parent of de96dee... Removed all attack actions. Created battle function that will randomize attacks based off number of turns.
