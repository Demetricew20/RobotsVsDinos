from robots import Robot
from dinosaurs import Dinosaur
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
                return "\nBattle concluded: Dinos have won!"

        for element in dino_herd.herd:
            count = 0
            while count <= len(element):
                for dino in element:
                    if dino.health <= 0:
                        element.remove(dino)
                count += 1

            if len(element) == 0:
                return "\nBattle concluded: Robos have won!"

        return "\nBattle Ongoing!"

    print(conclude_battle(robot_fleet, dino_herd))
