import pygame 
import math
from battlefield import Battlefield


def display(battlefield_name):

    pygame.init()

    clock = pygame.time.Clock
    fps = 60
    #game window
    screen_width = 800
    screen_height = 400

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('RobosVsDinos')

    #Classes
    class Dinosaur:
        def __init__(self, type_dino, x, y):
            self.type = type_dino
            self.attack = 'Stomp'
            self.health = 100
            self.energy = math.ceil(100)
            self.attack_power = 80
            self.status = 'Active'
            self.image = f'RobotsVsDinos\images\{self.type}.png'
            self.dino_img = pygame.image.load(f'RobotsVsDinos\images\{self.type}.png')
            self.image = pygame.transform.scale(self.dino_img, (math.ceil(self.dino_img.get_width() / 1.25), math.ceil(self.dino_img.get_height() / 1.25)))
            self.rect = self.image.get_rect()
            self.rect.center = (x,y)
        
        def draw(self):
            screen.blit(self.image, self.rect)

        def attack_robo(self, robo_obj):
            if self.health != 0 and self.energy <= 0:
                self.status = 'Resting'
                return 'Resting, cannot attack'
            if self.health <= 0:
                self.status = 'Defeated'
                return 'Defeated, cannot attack'
            elif robo_obj.health <= 0:
                robo_obj.health = 0
                robo_obj.attack_power = 0
                robo_obj.power_level = 0
                robo_obj.status = 'Defeated'
                return 'Defeated, cannot attack'
            else:
                robo_obj.health -= math.ceil(self.attack_power / 4)
                self.energy -= 10

        def __repr__(self):
            return f'Dino * {self.type} - Attack: {self.attack}, Health: {self.health}, Energy: {self.energy}, Attack Power: {self.attack_power}, Status: {self.status}'

    class Robot:
        def __init__(self, name, x, y):
            self.name = name
            self.weapon = "Fist"
            self.health = 100
            self.power_level = 0
            self.attack_power = 0
            self.status = 'Active'
            self.player_img = pygame.image.load(f'RobotsVsDinos\images\{self.name}.png')
            self.image = pygame.transform.scale(self.player_img, (math.ceil(self.player_img.get_width() / 3), math.ceil(self.player_img.get_height() / 3)))
            self.rect = self.image.get_rect()
            self.rect.center = (x,y)
        
        def draw(self):
            screen.blit(self.image, self.rect)

        def attack_dino(self, dino_obj):
            if self.health != 0 and self.power_level <= 0:
                self.status = 'Resting'
                return 'Resting, cannot attack'
            elif self.health <= 0:
                self.status = 'Defeated'
                return 'Defeated, cannot attack'
            elif dino_obj.health <= 0:
                dino_obj.health = 0
                dino_obj.energy = 0
                dino_obj.attack_power = 0
                dino_obj.status = 'Defeated'
                return 'Defeated, cannot be attacked'
            else:
                dino_obj.health -= math.ceil(self.attack_power / 4)
                self.power_level = self.power_level - 10

        def choose_weapon(self, available_weapons):
            weapon_choice = input("Select weapon from available list: ")
            if weapon_choice not in available_weapons:
                input("Must select from list, try again: ")
            else:
                self.weapon = weapon_choice

        def __repr__(self):
            return f'Robo * {self.name} - Weapon: {self.weapon}, Health: {self.health}, Power: {self.power_level}, Attack: {self.attack_power}, Status: {self.status}'

    #Fighters
    marvin = Robot('Marvin', 625, 250)
    megaman = Robot('Megaman', 700, 275)
    wall_E = Robot('Wall-e', 710, 350)
    stegosaurus = Dinosaur('Stegosaurus', 130, 320)
    velociraptor = Dinosaur('Velociraptor', 160, 270)
    tyrannosaurus = Dinosaur('Tyrannosaurus', 180, 240)

    #Selections
    # weapons = Weapons()
    # weapons.choose_weapon(marvin)
    # weapons.choose_weapon(megaman)
    # weapons.choose_weapon(wall_E)
    # weapons.choose_attack(stegosaurus)
    # weapons.choose_attack(velociraptor)
    # weapons.choose_attack(tyrannosaurus)

    #Stats
    # print(marvin)
    # print(megaman)
    # print(wall_E)
    # print(stegosaurus)
    # print(velociraptor)
    # print(tyrannosaurus)

    #background image
    background_img = pygame.image.load(battlefield_name.image).convert_alpha()

    #function drawing background
    def draw_bg():
        screen.blit(background_img, (0,0))

    run = True
    while run:
        #background
        draw_bg()
        #fighters
        marvin.draw()
        megaman.draw()
        wall_E.draw()
        tyrannosaurus.draw()
        velociraptor.draw()
        stegosaurus.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

        

    pygame.quit()

# display(battlefield)