import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
input_values = [1, 2, 3, 4, 5]
plt.plot(input_values, squares, linewidth=5)

plt.title("square numbers", fontsize=24)
plt.xlabel("value", fontsize= 14)
plt.ylabel("square of value", fontsize= 14)

plt.tick_params(axis="both", labelsize=14)

# scatter plot #

plt.scatter(2, 4, s=200)   # s is the size of the dot

plt.title("square numbers", fontsize=24)
plt.xlabel("value", fontsize= 14)
plt.ylabel("square of value", fontsize= 14)

plt.tick_params(axis='both', which= 'major', labelsize=14)
plt.show()