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
        self.class_name = "Fighter"
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
    player_death = class_methods.player_death
    
    # Resets health
    reset_stats = class_methods.reset_stats

    # Uses health potion
    consume_potion = class_methods.player_consume_potion
    
    # Runs loot generator
    loot = class_methods.loot
    
    # Equips different weapon
    #equip = class_methods.equip

class Mage:
    
    # Sets user-defined name and default stats
    def __init__(self, name):
        self.name = name
        self.weapon = weapons.WoodenStaff
        self.max_health = 80
        self.damage_done = 0
        self.current_health = 80
        self.alive = True
        self.class_name = "Mage"
        self.strength = 5
        self.dexterity = 6
        self.max_mana = 30
        self.current_mana = 30
        self.fireball = spells.Fireball
        self.frozen_arrow = spells.FrozenArrow
        self.meteor_shower = spells.MeteorShower
        self.inventory = inventory.Inventory(f"{self.weapon.weapon_type}", 1, 2)
        
        self.spell_list = [colored("\nMeteor Shower", "yellow"), 
                      colored("Fireball", "yellow"), 
                      colored("Frozen Arrow", "yellow")]
        self.mana_costs = ["(15 mana)",
                      "(10 mana)",
                      "(10 mana)",]
        
        print(f"Your mage's name is {self.name} and he is armed with a {self.weapon.weapon_type}.")
    
    # Subtract taken damage from current_health
    take_damage = class_methods.take_damage
    
    # Checks if current_health <= 0
    player_death = class_methods.player_death
    
    # Resets health and mana
    reset_stats = class_methods.reset_stats
    
    # Uses health/mana potion
    consume_potion = class_methods.player_consume_potion
        
    loot = class_methods.loot
    
    #equip = class_methods.equip
    
    # Keeps track of mage's spells and lists them
    def list_spells(self):
        
        cprint("\nSPELLS", "yellow")
        
        # I realize this method for concatenating elements from two
        # different arrays is dumb but I'm still new to Python
        j = 0
        for i in self.spell_list:
            print(i + " " + self.mana_costs[j])  
            j += 1
                
    
    # Allows mages to pick from available spells
    def pick_spell(self):
        self.list_spells()
        print("\nEnter a spell to equip it.  Enter 'back' to go back to turn menu.")
        spell_selection = input("> ")
        
        if spell_selection.lower().strip("\n") == "fireball":
            print("\nYou have selected the Fireball spell.  Are you sure? (yes/no)")
            p_input = input("> ")
            if p_input.lower().strip("\n") == "yes":
                self.equiped_spell = spells.Fireball
            elif p_input.lower().strip("\n") == "no":
                print("\nPick another spell!")
                self.pick_spell()
                
        elif spell_selection.lower().strip("\n") == "frozen arrow":
            print("\nYou have selected the Frozen Arrow spell.  Are you sure? (yes/no)")
            p_input = input("> ")
            if p_input.lower().strip("\n") == "yes":
                self.equiped_spell = spells.FrozenArrow
            elif p_input.lower().strip("\n") == "no":
                print("\nPick another spell!")
                self.pick_spell()
            
        elif spell_selection.lower().strip("\n") == "meteor shower":
            print("\nYou have selected the Meteor Shower spell.  Are you sure? (yes/no)")
            p_input = input("> ")
            if p_input.lower().strip("\n") == "yes":
                self.equiped_spell = spells.MeteorShower
            elif p_input.lower().strip("\n") == "no":
                print("\nPick another spell!")
                self.pick_spell()
            
        else:
            print("\nThat is not a valid spell, please try again.  If you would like to choose a different action, enter 'action'.  Otherwise, press the enter key.")
            self.pick_spell()
    
        
    # Casts the currently equipped spell            
    def cast_equipped_spell(self, target):
        if self.current_mana < self.equiped_spell.mana_required:
            print("\nNot enough mana.  Select a different spell or drink a mana potion.")
            self.pick_spell()
        else:
            print(f"\n{self.name} casts {self.equiped_spell.spell_name} on {target}.")
            self.damage_done = self.equiped_spell.damage
            self.current_mana -= self.equiped_spell.mana_required
            print(f"\n{self.name} does {self.damage_done} damage with {self.equiped_spell.spell_name}.")
                
    # Allows mages to attack
    def attack(self, target):
        self.pick_spell()
        print("\nCast currently equipped spell? (yes/no)")
        p_input = input("> ")
        if p_input.lower().strip("\n") == "yes":
            target = target
            self.cast_equipped_spell(target)
        elif p_input.lower().strip("\n") == "no":
            print("\nPick a different spell.")
            self.pick_spell()
            
                

class Hunter:
    
    # Init function to set a user-defined name and default stats
    def __init__(self, name):
        self.name = name 
        self.weapon = weapons.Longbow
        self.damage_done = 0
        self.class_name = "Hunter"
        self.max_health = 75
        self.current_health = 75
        self.alive = True
        self.strength = 5
        self.dexterity = 10
        self.inventory = inventory.Inventory(f"{self.weapon.weapon_type}", 1, 0)
        
        self.weapons = []
        
        print(f"Your hunter's name is {self.name} and he is armed with a {self.weapon.weapon_type}.")
        
    # Attack method works the same way as the fighter
    attack = class_methods.attack
    
    # Take damage method works the same way as the fighter
    take_damage = class_methods.take_damage
    
    # Check if current_health <= 0
    player_death = class_methods.player_death
    
    # Resets health 
    reset_stats = class_methods.reset_stats
    
    # Uses health potion
    consume_potion = class_methods.player_consume_potion
    
    loot = class_methods.loot
    
    #equip = class_methods.equip

