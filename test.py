import enemies
import classes 
from termcolor import colored, cprint
import sys

text = colored("Hello, world!", "red", attrs=["reverse", "blink"])
print(text)

cprint("Hello, world!", "green", "on_red")

print_red_on_cyan = lambda x: cprint(x, "red", "on_cyan")
print_red_on_cyan("Hello, world!")

for i in range(10):
    cprint(i, "magenta", end="")
    
cprint("Attention!", "red", attrs=["bold"], file=sys.stderr)
    
    
    