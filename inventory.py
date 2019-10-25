# The inventory allows both players and enemies to store items, and access them

from termcolor import colored, cprint
import class_methods

# When creating the class, specify the weapon (enemy or player's default weapon at the moment) 
# and number of health/mana potions
class Inventory:
    
    def __init__(self, weapon, hp_num, mp_num):
        self.weapon = weapon
        self.health_potion = hp_num
        self.mana_potion = mp_num
        
        # Weapons picked up through loot system go in this array
        self.weapons = []
    
    # Prints out inventory     
    def print_inventory(self):
        
        cprint("_____________", "yellow")
        cprint("\nINVENTORY", "yellow")
        weapon = colored(f"{self.weapon}", "yellow")
        print(f"\nEquipped weapon: " + weapon)
        print(f"\nOther weapons: " + (", ").join(self.weapons))
        hp_amount = colored(str(self.health_potion) + " health potion(s)", "yellow")
        mp_amount = colored(str(self.mana_potion) + " mana potion(s)", "yellow")
        print("\nYou have " + hp_amount + " and " + mp_amount)
        #print("\nTo equip a different weapon, enter 'equip.'")
        #p_input = input("> ")
        #if p_input.lower().strip("\n") == "equip":
            #class_methods.equip(self)
        cprint("_____________", "yellow")

    
            