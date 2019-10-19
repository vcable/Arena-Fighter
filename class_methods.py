# This module defines common class methods, such as attack and deal damage

# Attacks a given target.  Damage is dependent on weapon used
def attack(self, target):
        if self.alive == False:
                pass
        else:
                print(f"{self.name} attacks {target}!")
                self.damage_done = self.weapon.damage
                print(f"{self.name} does {self.damage_done} damage with his {self.weapon.weapon_type}")

# Takes damage (subtracts taken damage from max_health)
def take_damage(self, damage):
        self.current_health -= damage 
        print(f"{self.name} took {damage} damage! Total health is now {self.current_health}/{self.max_health}")

# Checks if current_health is equal to zero.  If it is, displays death message
def check_death(self):
    if self.current_health <= 0:
        print(f"{self.name} is dead.")
        self.alive = False

