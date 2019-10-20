# Defines all the enemies that can be encountered in the arena

import weapons
import class_methods


class WeakSwordsman:

    # Sets name, and basic stats
    def __init__(self, name):
        self.entity_class = "Weak Swordsman"
        self.name = name
        self.max_health = 30
        self.current_health = 30
        self.damage_done = 0
        self.alive = True
        self.weapon = weapons.RustyShortsword
        self.strength = 3
        self.dexterity = 1
        
        print(f"A Weak Swordsman named {self.name} appears! He is armed with a {self.weapon.weapon_type}")

    # Attack function is imported from the class_methods module
    attack = class_methods.attack

    # take_damage function is imported from the class_methods module
    take_damage = class_methods.take_damage

    # Checks to see if current health is 0 and prints death message
    check_death = class_methods.check_death
    
class Bear:
    
    def __init__(self, name):
        self.entity_class = "Bear"
        self.name = name
        self.max_health = 50
        self.current_health = 50
        self.damage_done = 0
        self.alive = True
        self.weapon = weapons.Claws
        self.strength = 10
        self.dexterity = 2
        
        print(f"A bear named {self.name} appears! It's claws look terribly sharp...")
        
    attack = class_methods.attack
    
    take_damage = class_methods.take_damage
    
    check_death = class_methods.check_death
    
class SeasonedGladiator:
    
    def __init__(self, name):
        self.entity_class = "Seasoned Gladiator"
        self.name = name
        self.max_health = 60
        self.current_health = 60
        self.damage_done = 0
        self.alive = True
        self.weapon = weapons.Morningstar
        self.strength = 12
        self.dexterity = 5
        
        print(f"A seasoned gladiator named {self.name} appears! He swings his morningstar menacingly...")
        
    attack = class_methods.attack
    
    take_damage = class_methods.take_damage
    
    check_death = class_methods.check_death
    
class Basilisk:
    
    def __init__(self, name):
        self.entity_class = "basilisk"
        self.name = name
        self.max_health = 60
        self.current_health = 60
        self.damage_done = 0
        self.alive = True
        self.weapon = weapons.Fangs
        self.strength = 8
        self.dexterity = 10
        
        print(f"A basilisk named {self.name} appears! His fangs drip with poison...")
        
    attack = class_methods.attack
    
    take_damage = class_methods.take_damage
    
    check_death = class_methods.check_death
    
class SmallDragon:
    
    def __init__(self, name):
        self.entity_class = "small dragon"
        self.name = name
        self.max_health = 70
        self.current_health = 70
        self.damage_done = 0
        self.alive = True
        self.weapon = weapons.Firebreath
        self.strength = 12
        self.dexterity = 4
        
        print(f"A small dragon named {self.name} appears! His eyes glow like embers...")
        
    attack = class_methods.attack
    
    take_damage = class_methods.take_damage
    
    check_death = class_methods.check_death

    

        