low = 0
high = 100
answer = 0
response = ''
print("Please think of a number between 0 and 100!")
while response != 'c':
	answer = int((low+high)/2)
	print("Is your secret number " + str(answer) + "?")
	response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I responseed correctly.")
	if response != 'h' and response != 'l' and response != 'c':
		print("Sorry, I did not understand your input.")
		continue
	elif response == 'h':
		high = answer
	elif response == 'c':
		break
	else:
		low = answer
print("Game over. Your secret number was: ", str(answer)) 