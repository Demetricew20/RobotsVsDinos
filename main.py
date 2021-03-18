from robots import Robots
from dinosaurs import Dinosaurs
from fleet import Fleet
from herd import Herd
from battlefield import Battlefield




if __name__ == '__main__':
    #Battlefield
    valley = Battlefield("Valley")



    # Robots
    robot_wally = Robots("Wally", "Love")
    robot_wally.power_level = 50
    robot_wally.attack_power = 30

    robot_megaman = Robots("Mega Man", "Cannon")
    robot_megaman.power_level = 110
    robot_megaman.attack_power = 120


    robot_marvin = Robots("Marvin", "Headbutt")
    robot_marvin.power_level = 90
    robot_marvin.attack_power = 90

    #Dinos
    dino_one = Dinosaurs("Tyrannosaurus")
    dino_one.attack_power = 150

    dino_two = Dinosaurs("Stegosaurus")
    dino_two.attack_power = 60

    dino_three = Dinosaurs("Velociraptor")
    dino_three.attack_power = 85

    #Weapon Selection *Power Adjustments*


    #Actions
    #----- Fix health to only display positive int, currently, will display negative before final attack call ----#
    robot_megaman.attack_dino(dino_two)
    robot_megaman.attack_dino(dino_two)
    robot_megaman.attack_dino(dino_two)

    dino_three.attack_robo(robot_marvin)
    dino_three.attack_robo(robot_marvin)
    dino_three.attack_robo(robot_marvin)
    dino_three.attack_robo(robot_marvin)
    dino_three.attack_robo(robot_marvin)
    dino_one.attack_robo(robot_megaman)
    dino_one.attack_robo(robot_megaman)

    print(valley)
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
        robot_health_sum = 0
        for element in robot_fleet.fleet:
            for robots in element:
                robot_health_sum += robots.health
                if (robot_health_sum <= 0):
                    print("Battle has concluded. The Dinos have won!")

        dino_health_sum = 0
        for element in dino_herd.herd:
            for dinos in element:
                dino_health_sum += dinos.health
                if (dinos.health <= 0):
                    print("Battle has concluded. The Robots have won!")


    conclude_battle(robot_fleet, dino_herd)