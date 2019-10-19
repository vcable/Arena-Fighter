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
    


    

        