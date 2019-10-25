**Changelog**

**Version 0.5** -- 8th update, 10/24/19

Added more weapons and spells.  This update also adds a loot system, where a random item is dropped after every encounter.  Different items drop for each class, and the next update will add more weapons/items and a way to equip new weapons from the inventory.  


**Version 0.42** -- 7th update, 10/21/19

Added a function to clear the screen before starting the game and improved player death checks.
More text display/formatting improvements.


**Version 0.41** -- 6th update, 10/20/19

Various enhancements to the Mage class, such as a dedicated spell screen, and some formatting fixes for combat text output.


**Version 0.4** -- 5th update, 10/20/19

Pretty big update, this one adds:

    Potions
    Some basic AI
    An inventory system

There are currently two potions in the game, health potions and mana potions.  They restore 10 points to their respective stats.
All enemies spawn with 1 health potion (or 2 for the final boss), and player classes spawn with 1 health potion (and 2 mana potions if you're a mage.)  

The AI is extremely rudimentary, and all it does is consume a health potion if its health is below 20.

The inventory can be displayed at the beginning of every turn, and shows the equipped weapon, as well as available potions.

*A small note:* I'm tremendously enjoying working on this game, I think it's the most fun I've had with programming since I started 4 months ago.  As soon as I flesh out the base game, I'll work on adding a full GUI to it.   


**Version 0.3** -- 4th update, 10/19/19

This update adds general text formatting and text highliting, making everything much prettier to look at.  This is done through the 
wonderful <a href="https://pypi.org/project/termcolor/">termcolor</a> library.


**Version 0.2** -- 3rd update, 10/19/19

This update adds all five encounters to the game.  I might add more later, but for now I think that five is plenty.  
The current enemies are, in order:

    Weak Swordsman
    Bear
    Seasoned Gladiator
    Basilisk
    Small Dragon

Each enemy has a unique weapon.


**Version 0.11** -- 2nd update, 10/19/19

This update adds functionality to allow mages to cast spells.  At the moment, there are only 3 spells: Fireball, Ice Arrow, and Meteor Shower.  
The player is able to select which spell they would like to cast before attacking each turn.


**Version 0.1** -- Initial release, 10/19/19

*Classes*

The game currently has 3 classes: Fighter, Mage, and Hunter.  The Fighter class is fully functional, but the Mage class
is missing some spell casting abilities, and the Hunter class has not been tested but should work in theory.

*Gameplay Loop*

The game only has one encounter at the moment, with a Weak Swordsman named Glorb.  Glorb has the ability to attack, but that's about it.
In future updates I'll give enemies the ability to drink health potions when they are low on health, and switch weapons/spells.

*Items/Weapons*

There are only 4 weapons right now, with each one being the default for either a player-selectable class or the enemy.

*Styling* 

The styling is non-existent at the moment.  I'm definitely going to add colored text, formatting, and the like when I get the core game fleshed out.
