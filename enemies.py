# Defines all the enemies that can be encountered in the arena
# ALL ENEMY METHOD DOCUMENTATION IS IN THE WEAKSWORDSMAN CLASS 
# SINCE ALL THE METHODS ARE THE SAME

import time
import weapons
import class_methods
import inventory
from termcolor import colored, cprint


class WeakSwordsman:

    # Sets name, and basic stats
    def __init__(self, name):
        self.entity_class = colored("weak swordsman", "red")
        self.name = colored(name, "red")
        self.max_health = 30
        self.current_health = 30
        self.damage_done = 0
        self.alive = True
        self.weapon = weapons.RustyShortsword
        self.strength = 3
        self.dexterity = 1
        self.inventory = inventory.Inventory(f"{self.weapon.weapon_type}", 1, 0)
        
        print(f"\nA {self.entity_class} named {self.name} appears! He is armed with a {self.weapon.weapon_type}")

    # Attack function is imported from the class_methods module
    attack = class_methods.attack

    # take_damage function is imported from the class_methods module
    take_damage = class_methods.take_damage
    
    # Allows AI to consume a potion.  They do this automatically if their health is below 20.
    # (the below 20 rule is coded out in main.py in the enemy_turn() method)
    consume_potion = class_methods.enemy_consume_potion
    
class Bear:
    
    def __init__(self, name):
        time.sleep(2)
        self.entity_class = colored("bear", "red")
        self.name = colored(name, "red")
        self.max_health = 50
        self.current_health = 50
        self.damage_done = 0
        self.alive = True
        self.weapon = weapons.Claws
        self.strength = 10
        self.dexterity = 2
        self.inventory = inventory.Inventory(f"{self.weapon.weapon_type}", 1, 0)
        
        print(f"\nA {self.entity_class} named {self.name} appears! It's claws look terribly sharp...")
        
    attack = class_methods.attack
    
    take_damage = class_methods.take_damage
    
    consume_potion = class_methods.enemy_consume_potion
    
class SeasonedGladiator:
    
    def __init__(self, name):
        time.sleep(2)
        self.entity_class = colored("seasoned gladiator", "red")
        self.name = colored(name, "red")
        self.max_health = 60
        self.current_health = 60
        self.damage_done = 0
        self.alive = True
        self.weapon = weapons.Morningstar
        self.strength = 12
        self.dexterity = 5
        self.inventory = inventory.Inventory(f"{self.weapon.weapon_type}", 1, 0)
        
        print(f"\nA {self.entity_class} named {self.name} appears! He swings his morningstar menacingly...")
        
    attack = class_methods.attack
    
    take_damage = class_methods.take_damage
    
    consume_potion = class_methods.enemy_consume_potion
    
class Basilisk:
    
    def __init__(self, name):
        time.sleep(2)
        self.entity_class = colored("basilisk", "red")
        self.name = colored(name, "red")
        self.max_health = 60
        self.current_health = 60
        self.damage_done = 0
        self.alive = True
        self.weapon = weapons.Fangs
        self.strength = 8
        self.dexterity = 10
        self.inventory = inventory.Inventory(f"{self.weapon.weapon_type}", 1, 0)
        
        print(f"\nA {self.entity_class} named {self.name} appears! His fangs drip with poison...")
        
    attack = class_methods.attack
    
    take_damage = class_methods.take_damage
  
    consume_potion = class_methods.enemy_consume_potion
    
class SmallDragon:
    
    def __init__(self, name):
        time.sleep(2)
        self.entity_class = colored("small dragon", "red")
        self.name = colored(name, "red")
        self.max_health = 70
        self.current_health = 70
        self.damage_done = 0
        self.alive = True
        self.weapon = weapons.Firebreath
        self.strength = 12
        self.dexterity = 4
        self.inventory = inventory.Inventory(f"{self.weapon.weapon_type}", 2, 0)
        
        print(f"\nA {self.entity_class} named {self.name} appears! His eyes glow like embers...")
        
    attack = class_methods.attack
    
    take_damage = class_methods.take_damage
    
    consume_potion = class_methods.enemy_consume_potion

    

        