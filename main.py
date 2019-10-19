# Sets up battles in the arena

import classes
import enemies

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
        
    # Player turn
    def player_turn(self):
        
        print(f"It's your turn!  Select an action.")
        print("You can attack or use a potion.  Enter 'attack' or 'potion'.")
        player_input = input()
       
        if player_input.lower().strip("\n") == "attack":
            PlayerCharacter.player_character.attack(CurrentEnemy.current_enemy.name)
            CurrentEnemy.current_enemy.take_damage(PlayerCharacter.player_character.damage_done)
            
            # Check death condition
            CurrentEnemy.current_enemy.check_death()
            
           
    # Enemy turn
    def enemy_turn(self):
            print(f"It is {CurrentEnemy.current_enemy.name}'s turn.")
            CurrentEnemy.current_enemy.attack(PlayerCharacter.player_character.name)
            PlayerCharacter.player_character.take_damage(CurrentEnemy.current_enemy.damage_done)
            
            # Check death condition
            PlayerCharacter.player_character.check_death()
            

# Initializes encounters with different enemies
class Encounters:
    
    # Handles the Weak Swordsman encounter
    def w_sword_encounter(self):
        CurrentEnemy.current_enemy = enemies.WeakSwordsman("Glorb")
        combat = Combat()
        
        while CurrentEnemy.current_enemy.alive == True:
            combat.enemy_turn()
            combat.player_turn()
        
        print(f"You have defeated the Weak Swordsman {CurrentEnemy.current_enemy.name}! You have tasted victory, but don't expect the rest of the fights to be this easy...")
            
        

class Game:

    def __init__(self):

        
        # Introductory message
        print("Welcome to Arena Fighter")
        
        # Create player character
        self.create_pc()
        
        # Start first encounter
        self.encounter_1()

    # Handles creation of player character
    def create_pc(self):

        print("Please select your class: Fighter, Mage, or Hunter")

        class_selection = input()

        if class_selection.lower().strip("\n") == "fighter":

            print("Pick a name for your fighter!")
            fighter_name = input()
            PlayerCharacter.player_character = classes.Fighter(fighter_name)

        elif class_selection.lower().strip("\n") == "mage":

            print("Pick a name for your mage!")
            mage_name = input()
            PlayerCharacter.player_character = classes.Mage(mage_name)

        elif class_selection.lower().strip("\n") == "hunter":

            print("Pick a name for your hunter!")
            hunter_name = input()
            PlayerCharacter.player_character = classes.Hunter(hunter_name)
            
        else:
            
            print("That is not a valid class, please try again.")
            self.create_pc()
    
    def encounter_1(self):
        
        # Makes encounters available
        arena = Encounters()
    
        #Starts first encounter
        print("Welcome to the arena, warrior!")
        arena.w_sword_encounter()
    
arena_fighter = Game()