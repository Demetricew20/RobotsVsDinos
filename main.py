import math
from robots import Robots
from dinosaurs import Dinosaurs
from fleet import Fleet
from herd import Herd
from battlefield import Battlefield
from weapons import Weapons




if __name__ == '__main__':
    #Battlefield
    battlefield = Battlefield()

    #Weapons
    weapons = Weapons()



    # Robots
    robot_wally = Robots("Wally")
    robot_wally.power_level = 50
    robot_wally.attack_power = 30
    # weapons.choose_weapon(robot_wally)


    robot_megaman = Robots("Mega Man")
    robot_megaman.power_level = 110
    robot_megaman.attack_power = 120


    robot_marvin = Robots("Marvin")
    robot_marvin.power_level = 90
    robot_marvin.attack_power = 90

    #Dinos
    dino_one = Dinosaurs("Tyrannosaurus")
    dino_one.attack_power = 150
    # weapons.choose_attack(dino_one)

    dino_two = Dinosaurs("Stegosaurus")
    dino_two.attack_power = 60

    dino_three = Dinosaurs("Velociraptor")
    dino_three.attack_power = 85

    #Weapon Selection *Power Adjustments*


    #Actions
    robot_megaman.attack_dino(dino_two)
    robot_megaman.attack_dino(dino_two)
    robot_megaman.attack_dino(dino_two)
    robot_megaman.attack_dino(dino_two)
    robot_megaman.attack_dino(dino_two)

    robot_marvin.attack_dino(dino_one)
    robot_marvin.attack_dino(dino_one)
    robot_marvin.attack_dino(dino_one)
    robot_marvin.attack_dino(dino_one)
    robot_marvin.attack_dino(dino_one)

    robot_megaman.attack_dino(dino_three)
    robot_megaman.attack_dino(dino_three)


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
                return "Battle concluded: Dinos have won!"

        for element in dino_herd.herd:
            count = 0
            while count <= len(element):
                for dino in element:
                    if dino.health <= 0:
                        element.remove(dino)
                count += 1

            if len(element) == 0:
                return "Battle concluded: Robos have won!"

        return "Battle Ongoing!"

    print(conclude_battle(robot_fleet, dino_herd))