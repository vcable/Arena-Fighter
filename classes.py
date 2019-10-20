# This file will define the available classes in Arena Fighter
# At the moment, there are three classes: Fighter, Mage, and Hunter

# The fighter uses swords, spears, and clubs, and fights in close quarters
# The mage uses spells, and engages from afar
# The hunter uses ranged weapons such as longbows, crossbows, and slingshots

# Each class has default weapons/spells, and starts with 3 health potions

import weapons
import class_methods
import spells
import inventory
from termcolor import colored, cprint

class Fighter:

    # Init function to set a user-defined name and default stats
    def __init__(self, name):
        self.name = colored(name, "blue")
        self.weapon = weapons.Shortsword
        self.max_health = 100
        self.current_health = 100
        self.alive = True
        self.strength = 10
        self.dexterity = 5
        self.damage_done = 0
        self.inventory = inventory.Inventory(f"{self.weapon.weapon_type}", 1, 0)
        
        print(f"\nYour fighter's name is {self.name} and he is armed with a {self.weapon.weapon_type}.")

    # Attacks a target and does damage based on weapon
    attack = class_methods.attack

    # Subtracts taken damage from current health
    take_damage = class_methods.take_damage

    # Checks for death
    check_death = class_methods.check_death
    
    # Resets health
    reset_stats = class_methods.reset_stats

    # Uses health potion
    consume_potion = class_methods.player_consume_potion

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
        self.inventory = inventory.Inventory(f"{self.weapon}", 1, 2)
        
        print(f"Your mage's name is {self.name} and he is armed with a {self.weapon.weapon_type}.")
    
    # Subtract taken damage from current_health
    take_damage = class_methods.take_damage
    
    # Checks if current_health <= 0
    check_death = class_methods.check_death
    
    # Resets health and mana
    reset_stats = class_methods.reset_stats
    
    # Uses health/mana potion
    consume_potion = class_methods.player_consume_potion
        
    # Keeps track of mage's spells and lists them
    def list_spells(self):
        print(f"Available spells: \n {self.fireball.spell_name}, {self.frozen_arrow.spell_name}, {self.meteor_shower.spell_name}.")
    
    # Allows mages to pick from available spells
    def pick_spell(self):
        self.list_spells()
        print("Enter a spell to equip it.")
        spell_selection = input("> ")
        
        if spell_selection.lower().strip("\n") == "fireball":
            print("You have selected the Fireball spell.  Are you sure? (yes/no)")
            p_input = input("> ")
            if p_input.lower().strip("\n") == "yes":
                self.equiped_spell = spells.Fireball
            elif p_input.lower().strip("\n") == "no":
                print("Pick another spell!")
                self.pick_spell()
                
        elif spell_selection.lower().strip("\n") == "frozen arrow":
            print("You have selected the Frozen Arrow spell.  Are you sure? (yes/no)")
            p_input = input("> ")
            if p_input.lower().strip("\n") == "yes":
                self.equiped_spell = spells.FrozenArrow
            elif p_input.lower().strip("\n") == "no":
                print("Pick another spell!")
                self.pick_spell()
            
        elif spell_selection.lower().strip("\n") == "meteor shower":
            print("You have selected the Meteor Shower spell.  Are you sure? (yes/no)")
            p_input = input("> ")
            if p_input.lower().strip("\n") == "yes":
                self.equiped_spell = spells.MeteorShower
            elif p_input.lower().strip("\n") == "no":
                print("Pick another spell!")
                self.pick_spell()
            
        else:
            print("That is not a valid spell, please try again.  If you would like to choose a different action, enter 'action'.  Otherwise, press the enter key.")
            self.pick_spell()
    
        
    # Casts the currently equipped spell            
    def cast_equipped_spell(self, target):
        if self.current_mana < self.equiped_spell.mana_required:
            print("Not enough mana.  Select a different spell or drink a mana potion.")
            self.pick_spell()
        else:
            print(f"{self.name} casts {self.equiped_spell.spell_name} on {target}.")
            self.damage_done = self.equiped_spell.damage
            self.current_mana -= self.equiped_spell.mana_required
            print(f"{self.name} does {self.damage_done} damage with {self.equiped_spell.spell_name}.")
                
    # Allows mages to attack
    def attack(self, target):
        self.pick_spell()
        print("Cast currently equipped spell? (yes/no)")
        p_input = input("> ")
        if p_input.lower().strip("\n") == "yes":
            target = target
            self.cast_equipped_spell(target)
        elif p_input.lower().strip("\n") == "no":
            print("Pick a different spell.")
            self.pick_spell()
            
                

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
        self.inventory = inventory.Inventory(f"{self.weapon}", 1, 0)
        
        print(f"Your hunter's name is {self.name} and he is armed with a {self.weapon.weapon_type}.")
        
    # Attack method works the same way as the fighter
    attack = class_methods.attack
    
    # Take damage method works the same way as the fighter
    take_damage = class_methods.take_damage
    
    # Check if current_health <= 0
    check_death = class_methods.check_death
    
    # Resets health 
    reset_stats = class_methods.reset_stats
    
    # Uses health potion
    consume_potion = class_methods.player_consume_potion

