import potions_and_items
import time

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
def consume_potion(self, potion):
        print(f"\n{self.name} uses a {potion} potion.")
        

# Resets players stats (health/mana) before every encounter
def reset_stats(self):
    try:
        self.current_mana = self.max_mana
        print(f"\n{self.name}'s mana points have been reset.  They are now at {self.current_mana}/{self.max_mana}")
    except:
        pass
    
    self.current_health = self.max_health
    print(f"\n{self.name}'s health points have been reset.  They are now at {self.current_health}/{self.max_health}")


