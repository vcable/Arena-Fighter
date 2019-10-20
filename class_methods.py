import potions_and_items
import time
import inventory

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

# Takes damage (subtracts taken damage from max_health)
def take_damage(self, damage):
        self.current_health -= damage 
        print(f"\n{self.name} took {damage} damage! Total health is now {self.current_health}/{self.max_health}")

# Checks if current_health is equal to zero.  If it is, displays death message
def check_death(self):
    if self.current_health <= 0:
        print(f"\n{self.name} is dead.")
        self.alive = False
        
# Allows user to consume a potion
def player_consume_potion(self):
        print(f"\nWhich potion would you like to use? Look at your inventory, and select one! (enter 'health potion'/'mana potion')")
        time.sleep(2)
        self.inventory.print_inventory()
        p_input = input("\n> ")
        
        if p_input == "health potion" and self.inventory.health_potion > 0:
                self.current_health += 10
                self.inventory.health_potion -= 1
                print(f"\n{self.name} uses a health potion.")
                time.sleep(2)
                print(f"\n{self.name}'s current health is now {self.current_health}/{self.max_health}")
                
        elif p_input == "mana potion" and self.inventory.mana_potion > 0:
                print(f"\n{self.name} uses a mana potion.")
                self.current_mana += 10
                self.inventory.mana_potion -= 1
                time.sleep(2)
                print(f"\n{self.name}'s current mana is now {self.current_mana}/{self.max_mana}")
                
        else:
                time.sleep(2)
                print("\nEither you can't use that particular potion, or you entered some invalid input.  Try again!")
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
        
# Resets players stats (health/mana) before every encounter
def reset_stats(self):
    try:
        self.current_mana = self.max_mana
        print(f"\n{self.name}'s mana points have been reset.  They are now at {self.current_mana}/{self.max_mana}")
    except:
        pass
    
    self.current_health = self.max_health
    print(f"\n{self.name}'s health points have been reset.  They are now at {self.current_health}/{self.max_health}")


