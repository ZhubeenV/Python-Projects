num = 88
guess = int(input("Pick a number\n"))
while(guess != num):
	print("Not quite, try again")
	guess = int(input("Pick a number\n"))
else:
	print("Congrats! You got it!")