from termcolor import colored, cprint

# This file defines all the available weapons in the game, and their stats
# Stats: Starting simple, the only stat will be damage

class Shortsword:

    weapon_type = colored("shortsword", "yellow")
    damage = 10

class Longsword:
    
    weapon_type = colored("longsword", "yellow")
    damage = 15

class RustyShortsword:

    weapon_type = colored("rusty shortsword", "yellow")
    damage = 5
    
class WoodenStaff:
    
    weapon_type = colored("wooden staff", "yellow")
    damage = 10
    
class Longbow:
    
    weapon_type = colored("longbow", "yellow")
    damage = 10
    
class Crossbow:
    
    weapon_type = colored("crossbow", "yellow")
    damage = 15
    
class Claws:
    
    weapon_type = colored("claws", "yellow")
    damage = 10
    
class Morningstar:
    
    weapon_type = colored("morningstar", "yellow")
    damage = 13
    
class Fangs:
    
    weapon_type = colored("fangs", "yellow")
    damage = 12
    
class Firebreath:
    
    weapon_type = colored("fire breath", "yellow")
    damage = 10
    
class Slingshot:
    
    weapon_type = colored("slingshot", "yellow")
    damage = 10