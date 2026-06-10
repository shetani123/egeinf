from string import *
for x in printable[:18]:
    n = int(f'11H{x}05', 18) + int(f'3F{x}54{x}8', 18) + int(f'G{x}{x}{x}9', 18)
    if n % 14 == 0:
        print(x, n // 14)