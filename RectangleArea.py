L1 = int(input("Length of Rectangle 1?\n"))
W1 = int(input("Width of Rectangle 1?\n"))
L2 = int(input("Length of Rectangle 2?\n"))
W2 = int(input("Width of Rectangle 2?\n"))
A1 = L1 * W1
A2 = L2 * W2
if(A1 > A2):
	print("Rectangle 1 is greater than rectangle 2 by " + str(A1 - A2) + " square units!")
elif(A1 == A2):
	print("The rectangles are the same size!")
else:
	print("Rectangle 2 is greater than rectangle 1 by " + str(A2 - A1) + " square units!")