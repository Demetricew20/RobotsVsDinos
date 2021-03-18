from robots import Robots
from dinosaurs import Dinosaurs
from weapons import Weapons




if __name__ == '__main__':
    robot_wally = Robots("Wally", "Love")
    robot_wally.power_level = 5
    robot_wally.attack_power = 30

    robot_megaman = Robots("Mega Man", "Cannon")
    robot_megaman.power_level = 40
    robot_megaman.attack_power = 120

    robot_marvin = Robots("Marvin", "Headbutt")
    robot_marvin.power_level = 32
    robot_marvin.attack_power = 90

    dino_one = Dinosaurs("Tyrannosaurus")
    dino_one.attack_power = 150

    dino_two = Dinosaurs("Stegosaurus")
    dino_two.attack_power = 60

    dino_three = Dinosaurs("Velociraptor")
    dino_three.attack_power = 85

    print(robot_wally)
    print(robot_megaman)
    print(robot_marvin)
    print(dino_one)
    print(dino_two)
    print(dino_three)


