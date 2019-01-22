import matplotlib.pyplot as plt
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s=40)
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("value", fontsize = 14)
plt.ylabel("square of values", fontsize = 14)
plt.
plt.show()
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)