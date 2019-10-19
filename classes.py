# This file will define the available classes in Arena Fighter
# At the moment, there are three classes: Fighter, Mage, and Hunter

# The fighter uses swords, spears, and clubs, and fights in close quarters
# The mage uses spells, and engages from afar
# The hunter uses ranged weapons such as longbows, crossbows, and slingshots

# Each class has default weapons/spells, and starts with 3 health potions

import weapons
import class_methods
import spells

class Fighter:

    # Init function to set a user-defined name and default stats
    def __init__(self, name):
        self.name = name 
        self.weapon = weapons.Shortsword
        self.max_health = 100
        self.current_health = 100
        self.alive = True
        self.strength = 10
        self.dexterity = 5
        self.damage_done = 0
        print(f"Your fighter's name is {self.name} and he is armed with a {self.weapon.weapon_type}.")

    # Attacks a target and does damage based on weapon
    attack = class_methods.attack

    # Subtracts taken damage from current health
    take_damage = class_methods.take_damage

    # Checks for death
    check_death = class_methods.check_death


class Mage:
    
    # Sets user-defined name and default stats
    def __init__(self, name):
        self.name = name
        self.weapon = weapons.WoodenStaff
        self.max_health = 80
        self.damage_done = 0
        self.current_health = 80
        self.alive = True
        self.strength = 5
        self.dexterity = 6
        self.max_mana = 20
        self.current_mana = 20
        self.fireball = spells.Fireball
        self.frozen_arrow = spells.FrozenArrow
        self.meteor_shower = spells.MeteorShower
        
        print(f"Your mage's name is {self.name} and he is armed with a {self.weapon.weapon_type}.")
    
    # Checks if current_health <= 0
    check_death = class_methods.check_death
        
    # Keeps track of mage's spells and lists them
    def list_spells(self):
        print(f"Available spells: \n {self.fireball.spell_name}, {self.frozen_arrow.spell_name}, {self.meteor_shower.spell_name}.")
    
    # Allows mages to pick from available spells
    def pick_spell(self):
        self.list_spells()
        print("Enter a spell to select it.")
        spell_selection = input()
        
        if spell_selection.lower().strip("\n") == "fireball":
            self.equiped_spell = spells.Fireball
        
        elif spell_selection.lower().strip("\n") == "frozen arrow":
            self.equiped_spell = spells.FrozenArrow
            
        elif spell_selection.lower().strip("\n") == "meteor shower":
            self.equiped_spell = spells.MeteorShower
            
        else:
            print("That is not a valid spell, please try again.")
            self.pick_spell()
        
    # Allows mages to cast fireball.  Works very similar to attack()
    def cast_fireball(self, target):
        
        if self.current_mana < spells.Fireball.mana_required:
                print("Not enough mana.")
        else:
                print(f"{self.name} casts fireball on {target}.")
                self.damage_done = spells.Fireball.damage
                self.current_mana -= spells.Fireball.mana_required
                print(f"{self.name} does {self.damage_done} damage with fireball.")
                

class Hunter:
    
    # Init function to set a user-defined name and default stats
    def __init__(self, name):
        self.name = name 
        self.weapon = weapons.Longbow
        self.damage_done = 0
        self.max_health = 75
        self.current_health = 75
        self.alive = True
        self.strength = 5
        self.dexterity = 10
        print(f"Your hunter's name is {self.name} and he is armed with a {self.weapon.weapon_type}.")
        
    # Attack method works the same way as the fighter
    attack = class_methods.attack
    
    # Take damage method works the same way as the fighter
    take_damage = class_methods.take_damage
    
    # Check if current_health <= 0
    check_death = class_methods.check_death

