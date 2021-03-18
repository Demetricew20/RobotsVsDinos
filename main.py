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
    robot_wally.power_level = 5
    robot_wally.attack_power = 30

    robot_megaman = Robots("Mega Man", "Cannon")
    robot_megaman.power_level = 40
    robot_megaman.attack_power = 120


    robot_marvin = Robots("Marvin", "Headbutt")
    robot_marvin.power_level = 32
    robot_marvin.attack_power = 90

    #Dinos
    dino_one = Dinosaurs("Tyrannosaurus")
    dino_one.attack_power = 150

    dino_two = Dinosaurs("Stegosaurus")
    dino_two.attack_power = 60

    dino_three = Dinosaurs("Velociraptor")
    dino_three.attack_power = 85

    #Actions
    #----- Fix health to only display positive int, currently, will display negative before final attack call ----#
    robot_megaman.attack_dino(dino_two)
    robot_megaman.attack_dino(dino_two)
    robot_megaman.attack_dino(dino_two)

    dino_three.attack_robo(robot_marvin)
    dino_three.attack_robo(robot_marvin)

    print(valley)
    print(robot_wally)
    print(robot_megaman)
    print(robot_marvin)
    print(dino_one)
    print(dino_two)
    print(dino_three)

    #Fleet
    robot_fleet = Fleet()
    robot_fleet.add_to_fleet([robot_megaman.name, robot_marvin.name, robot_wally.name])
    print(robot_fleet.fleet)

    #Herd
    dino_herd = Herd()
    dino_herd.add_to_herd([dino_one.type, dino_two.type, dino_three.type])
    print(dino_herd.herd)



