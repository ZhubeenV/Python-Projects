class color:
	BOLD = '\033[1m'
	END = '\033[0m'

def gcd(a,b):
	if b > a:
		if b % a == 0:
			return a
		else: 
			return gcd(b % a, a)
	else: 
		if a % b == 0:
			return b
		else:
			return gcd(b, a % b)        

x = int(input(color.BOLD + "What is your first number?\n" + color.END))
y = int(input(color.BOLD + "What is your second number?\n" + color.END))
print('\n' + color.BOLD + str(gcd(x,y)) + color.END)