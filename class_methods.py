import potions_and_items
import time
import inventory
from termcolor import colored, cprint
import weapons
import random
import spells

# This module defines common class methods, such as attack and deal damage

# Attacks a given target.  Damage is dependent on weapon used
def attack(self, target):
        if self.alive == False:
                pass
        else:
                print(f"\n{self.name} attacks {target}!")
                time.sleep(2)
                self.damage_done = self.weapon.damage
                print(f"\n{self.name} does {self.damage_done} damage with his {self.weapon.weapon_type}")

# Takes damage (subtracts taken damage from max_health) and check for death
def take_damage(self, damage):
        self.current_health -= damage 
        print(f"\n{self.name} took {damage} damage! Total health is now {self.current_health}/{self.max_health}")
        if self.current_health <= 0:
                print(f"\n{self.name} is dead.")
                self.alive = False
    
        
# Player death message and program exit
def player_death(self):
        if self.alive == False:
                print("You have fought valiantly in the arena, but unfortunately you have suffered defeat.")
                exit()
        
# Allows user to consume a potion
def player_consume_potion(self):
        print(f"\nWhich potion would you like to use? Look at your inventory, and select one! (enter 'health potion'/'mana potion')")
        self.inventory.print_inventory()
        p_input = input("\n> ")
        
        if p_input == "health potion" and self.inventory.health_potion > 0 and self.current_health < self.max_health:
                self.current_health += 10
                self.inventory.health_potion -= 1
                print(f"\n{self.name} uses a health potion.")
                time.sleep(2)
                print(f"\n{self.name}'s current health is now {self.current_health}/{self.max_health}")
                
        elif p_input == "mana potion" and self.inventory.mana_potion > 0 and self.current_mana < self.max_mana:
                print(f"\n{self.name} uses a mana potion.")
                self.current_mana += 10
                self.inventory.mana_potion -= 1
                time.sleep(2)
                print(f"\n{self.name}'s current mana is now {self.current_mana}/{self.max_mana}")
                
        else:
                time.sleep(2)
                print("\nEither you can't use that particular potion, your health/mana points are full, or you entered some invalid input.  Try again!")
                self.consume_potion()
                
# Consume potion method for AI.  I made 2 different methods because the AI has to decide independently when to use a potion
# and what potion to use, whereas the player decides differently
# Note: Enemies currently do not have mana, so they will only be able to consume health potions
def enemy_consume_potion(self):
        if self.current_health < self.max_health / 2 and self.inventory.health_potion > 0:
                time.sleep(2)
                self.current_health += 10
                self.inventory.health_potion -= 1
                print(f"\n{self.name} uses a health potion and recovers 10 health points.  Current health is {self.current_health}/{self.max_health}")
        else:
                pass
        
# Resets players stats (health/mana) before every encounter and grants potions
def reset_stats(self):
    hp = colored("2", "yellow")
    mp = colored("1", "yellow")
    try:
        self.current_mana = self.max_mana
        time.sleep(2)
        print(f"\n{self.name}'s mana points have been reset.  They are now at {self.current_mana}/{self.max_mana}")
    except:
        pass
    
    self.current_health = self.max_health
    time.sleep(2)
    print(f"\n{self.name}'s health points have been reset.  They are now at {self.current_health}/{self.max_health}")
    
    if self.class_name == "Fighter" or self.class_name == "Hunter":
            self.inventory.health_potion += 2
            time.sleep(2)
            print("\nYou have been granted " + hp + " health potions.")
    elif self.class_name == "Mage":
            self.inventory.mana_potion += 1
            self.inventory.health_potion += 2
            time.sleep(2)
            print("\nYou have been granted " + mp + " mana potion and " + hp + " health potions.")    
            
# This function handles the loot system
def loot(self):
        
        if self.class_name == "Fighter":
                # Items that can drop
                items = [potions_and_items.HealthPotion.name, 
                         weapons.Longsword.weapon_type, 
                         weapons.RustyShortsword.weapon_type, 
                         weapons.Morningstar.weapon_type]

                loot = random.choice(items)
                
                if loot == potions_and_items.HealthPotion.name:
                        self.inventory.health_potion += 1
                        time.sleep(2)
                        print("\nYou loot a health potion.")
                else:
                        self.inventory.weapons.append(loot)
                        time.sleep(2)
                        print("\nYou loot a " + loot)
        
        elif self.class_name == "Mage":
                
                items = [potions_and_items.HealthPotion.name,
                         potions_and_items.ManaPotion.name,
                         spells.LightningBolt.spell_name,
                         spells.Stun.spell_name]
                
                loot = random.choice(items)
                
                if loot == potions_and_items.HealthPotion.name:
                        self.inventory.health_potion += 1
                        time.sleep(2)
                        print("\nYou loot a health potion.")
                elif loot == potions_and_items.ManaPotion.name:
                        self.inventory.mana_potion += 1
                        time.sleep(2)
                        print("\nYou loot a mana potion.")
                else:
                        self.spell_list.append(colored(loot, "yellow"))
                        self.mana_costs.append("(10 mana)")
                        time.sleep(2)
                        print("\nYou loot a " + loot + " scroll.")
                        
        elif self.class_name == "Hunter":
                
                items = [potions_and_items.HealthPotion.name,
                         weapons.Crossbow.weapon_type,
                         potions_and_items.HealthPotion.name,
                         weapons.Slingshot.weapon_type]
                
                loot = random.choice(items)
                
                if loot == potions_and_items.HealthPotion.name:
                        self.inventory.health_potion += 1
                        time.sleep(2)
                        print("\nYou loot a health potion.")
                else:
                        self.inventory.weapons.append(loot)
                        time.sleep(2)
                        print("\nYou loot a " + loot) 

# Equips weapons from inventory
#def equip(self):
        #print("Enter the name of the weapon you would like to equip.")
        #p_input = input("> ")
        #if p_input in self.weapons:
                #self.weapon = p_