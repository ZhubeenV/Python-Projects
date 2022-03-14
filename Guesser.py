import random
guess = random.randrange(0,10000)
num = int(input('Pick a number between 0 and 9999:\n'))
i = 0
while(guess != num):
	print(guess)
	i += 1
	guess = random.randrange(0,10000)
else:
	print(\033[1m + i + \033[0;0m)
	print(\033[1m + guess + \033[0;0m)