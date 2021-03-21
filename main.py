from robots import Robot
from dinosaurs import Dinosaur
from fleet import Fleet
from herd import Herd
from battlefield import Battlefield
from weapons import Weapons
import ctypes
import random

if __name__ == '__main__':

    #Battlefield
    battlefield = Battlefield()

    #Weapons
    weapons = Weapons()

    # Robots
    robot_wally = Robot("Wally")
    robot_wally.power_level = 100
    robot_wally.attack_power = 60
    weapons.choose_weapon(robot_wally)

    robot_megaman = Robot("Mega Man")
    robot_megaman.power_level = 110
    robot_megaman.attack_power = 100
    weapons.choose_weapon(robot_megaman)

    robot_marvin = Robot("Marvin")
    robot_marvin.power_level = 120
    robot_marvin.attack_power = 70
    weapons.choose_weapon(robot_marvin)

    #Dinos
    dino_one = Dinosaur("Tyrannosaurus")
    dino_one.attack_power = 100
    weapons.choose_attack(dino_one)

    dino_two = Dinosaur("Stegosaurus")
    dino_two.attack_power = 60
    weapons.choose_attack(dino_two)

    dino_three = Dinosaur("Velociraptor")
    dino_three.attack_power = 85
    weapons.choose_attack(dino_three)

    #Fleet
    robot_fleet = Fleet()
    robot_fleet.add_to_fleet([robot_megaman, robot_marvin, robot_wally])
    # print(robot_fleet.fleet)

    #Herd
    dino_herd = Herd()
    dino_herd.add_to_herd([dino_one, dino_two, dino_three])
    # print(dino_herd.herd)

        #Actions
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
    print(battlefield)
    print(robot_wally)
    print(robot_megaman)
    print(robot_marvin)
    print(dino_one)
    print(dino_two)
    print(dino_three)


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


