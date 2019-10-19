import enemies
import classes 

mage = classes.Mage("bill")
weak_swordsman = enemies.WeakSwordsman("Glorb")
mage.pick_spell()
print(f"Cast equipped spell against {weak_swordsman.name}? (yes/no)")
p_input = input()
if p_input.lower().strip("\n") == "yes":
    mage.cast_fireball(weak_swordsman.name)