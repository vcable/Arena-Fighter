# Sets up battles in the arena

import classes
import enemies
import sys
from termcolor import colored, cprint
import time

# Keeps track of player character
# This class has a dynamically created variable called player_character that is
# created when the player goes through the character creation process.
# This variable ties directly to the picked class


class PlayerCharacter:

    def __init__(self):
        return


# Keeps track of current enemy
# This class contains a dynamically created variable that is 
# changed depending on the encounter.  It is tied directly to
# the enemy class 
class CurrentEnemy:
    
    def __init__(self):
        return

# Takes care of combat loop
class Combat:
    
    # Combat loop w/ turns
    def combat_loop(self):
        while CurrentEnemy.current_enemy.alive == True:
            self.enemy_turn()
            self.player_turn()
    
    # Player turn
    def player_turn(self):
        
        
        print(f"\nIt's your turn!  Select an action.")
        print("You can attack or use a potion.  Enter 'attack' or 'potion'.")
        player_input = input("> ")
       
        if player_input.lower().strip("\n") == "attack":
            PlayerCharacter.player_character.attack(CurrentEnemy.current_enemy.name)
            time.sleep(2)
            CurrentEnemy.current_enemy.take_damage(PlayerCharacter.player_character.damage_done)
            time.sleep(2)
            
            # Check death condition
            CurrentEnemy.current_enemy.check_death()
            
           
    # Enemy turn
    def enemy_turn(self):
            print(f"\nIt is {CurrentEnemy.current_enemy.name}'s turn.")
            time.sleep(2)
            CurrentEnemy.current_enemy.attack(PlayerCharacter.player_character.name)
            time.sleep(2)
            PlayerCharacter.player_character.take_damage(CurrentEnemy.current_enemy.damage_done)
            time.sleep(2)
            
            # Check death condition
            PlayerCharacter.player_character.check_death()
            

# Initializes encounters with different enemies
class Encounters:
    
    # Handles the Weak Swordsman encounter
    def w_sword_encounter(self):
        CurrentEnemy.current_enemy = enemies.WeakSwordsman("Glorb")
        combat = Combat()
        combat.combat_loop()
        time.sleep(2)
        print(f"\nYou have defeated the Weak Swordsman {CurrentEnemy.current_enemy.name}! You have tasted victory, but don't expect the rest of the fights to be this easy...")
    
    # Bear encounter   
    def bear_encounter(self):
        CurrentEnemy.current_enemy = enemies.Bear("Rusty")
        combat = Combat()
        combat.combat_loop()
        print(f"\nYou have defeated the bear {CurrentEnemy.current_enemy.name}, yet there are many battles that lie ahead...")
        
    def seasoned_g_encounter(self):
        CurrentEnemy.current_enemy = enemies.SeasonedGladiator("Olaf")
        combat = Combat()
        combat.combat_loop()
        time.sleep(2)
        print(f"\nYou have defeated the seasoned gladiator {CurrentEnemy.current_enemy.name}, but there are still many battles on the horizon...")
        
    def basilisk_encounter(self):
        CurrentEnemy.current_enemy = enemies.Basilisk("Ronny")
        combat = Combat()
        combat.combat_loop()
        time.sleep(2)
        print(f"\nYou have defeated the hissing basilisk Ronny, but there are more encounters ahead...")
        
    def dragon_encounter(self):
        CurrentEnemy.current_enemy = enemies.SmallDragon("Drogon")
        combat = Combat()
        combat.combat_loop()
        time.sleep(2)
        print(f"\nYou have defeated the small dragon Drogon, and quelled the fire in his lungs.")
        time.sleep(2)
        cprint("\nYou are the champion of the arena!", "red")
        exit(0)
        

class Game:

    def __init__(self):

        
        # Introductory message
        
        cprint(              
                             """
                                _________________________________________
                                                
                                                WELCOME TO
                                               
                                               ARENA FIGHTER
                                _________________________________________""", "red")
        
        # Create player character
        time.sleep(2)
        self.create_pc()
        
        # Start first encounter
        self.encounter_1()
        
        # Second encounter, etc
        self.encounter_2()
        
        self.encounter_3()
        
        self.encounter_4()
        
        self.encounter_5()

    # Handles creation of player character
    def create_pc(self):

        print("\nPlease select your class: Fighter, Mage, or Hunter")

        class_selection = input("> ")

        if class_selection.lower().strip("\n") == "fighter":

            print("Pick a name for your fighter!")
            fighter_name = input("> ")
            PlayerCharacter.player_character = classes.Fighter(fighter_name)

        elif class_selection.lower().strip("\n") == "mage":

            print("Pick a name for your mage!")
            mage_name = input("> ")
            PlayerCharacter.player_character = classes.Mage(mage_name)

        elif class_selection.lower().strip("\n") == "hunter":

            print("Pick a name for your hunter!")
            hunter_name = input("> ")
            PlayerCharacter.player_character = classes.Hunter(hunter_name)
            
        else:
            
            print("That is not a valid class, please try again.")
            self.create_pc()
    
    def encounter_1(self):
        
        # Makes encounters available
        arena = Encounters()
    
        # Starts first encounter
        cprint("\nWelcome to the arena, warrior!", "red")
        time.sleep(2.5)
        arena.w_sword_encounter()
        
    def encounter_2(self):
        
        PlayerCharacter.player_character.reset_stats()
        
        # Same exact functionality as encounter_1
        arena = Encounters()
        print("Having dealt with the Weak Swordsman, you wipe his blood from your blade.  \nIn the distance, you hear the ferocious growl of a bear...")
        arena.bear_encounter()
        
    def encounter_3(self):
        
        PlayerCharacter.player_character.reset_stats()
        
        arena = Encounters()
        print("The bear heaves it's last breath, rolled over on its side.\nWith barely a moment to breathe, you see your next opponent approaching...")
        arena.seasoned_g_encounter()
        
    def encounter_4(self):
        
        PlayerCharacter.player_character.reset_stats()
        
        arena = Encounters()
        print("The gladiator is gone, but you hear the hiss of a basilisk...")
        arena.basilisk_encounter()
        
    def encounter_5(self):
        
        PlayerCharacter.player_character.reset_stats()
        
        arena = Encounters()
        print("The basilisk lies at your feet, cut in half. \nYou feel the warmth of fire on the back of your neck, and look around to see an angry-looking dragon...")
        arena.dragon_encounter()
        
arena_fighter = Game()
