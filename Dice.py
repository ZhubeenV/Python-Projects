import random

class color:
   BOLD = '\033[1m'
   END = '\033[0m'


dice = ("one", "two", "three", "four", "five", "six ")

print(color.BOLD + random.choice(dice) + color.END)