import numpy as np
import matplotlib.pyplot as plt
from methods import *
from scipy.interpolate import pchip_interpolate
from prettytable import PrettyTable as pt

f = lambda x: np.sin(x)

# Define the range of x values
X = np.linspace(1, 10, 100)

# Compute the true function values
Y = [f(x) for x in X]

# targets = np.linspace(2, 4, 100)
targets = list(range(1, 10))

# Compute the values using the interpolation methods
Y_true = [f(x) for x in targets]
Y_newton_forward = [newton_forward(X, Y)(x) for x in targets]
Y_newton_backward = [newton_backward(X, Y)(x) for x in targets]
Y_pchip = [pchip_interpolate(X, Y, x) for x in targets]
Y_stirling = [sterling_interpolation(X, Y)(x) for x in targets]
Y_everett = [everett_interpolation(X, Y)(x) for x in targets]

# Create a table to display the results
results = pt(["x", "True Value", "Newton's Forward", "Newton's Backward", "PCHIP", "Sterling", "Everett's"])

for i in range(len(targets)):
    results.add_row([targets[i], Y_true[i], Y_newton_forward[i], Y_newton_backward[i], Y_pchip[i], Y_stirling[i], Y_everett[i]])

# Print the results table
print(results)

# Plot the true function and the interpolated functions on a common graph
plt.plot(targets, Y_true, label='True Function')
plt.plot(targets, Y_newton_forward, label="Newton's Forward Interpolation")
plt.plot(targets, Y_newton_backward, label="Newton's Backward Interpolation")
plt.plot(targets, Y_pchip, label='PCHIP Interpolation')
plt.plot(targets, Y_stirling, label="Stirling Interpolation")
plt.legend()
#plt.show()


# Define the data points
X = np.array([1, 2, 3, 4, 5])
Y = np.array([f(x) for x in X])

# Define the interpolation function
f = everett_interpolation(X, Y)

# Test the interpolation function
print(f(2.5))  # Output: 6.25
# Define the x range for plotting
x_range = np.linspace(X[0], X[-1], num=100)

# Evaluate the interpolation function over the x range
y_range = [f(x) for x in x_range]

# Plot the data points and the interpolation function
plt.plot(X, Y, 'o', label='Data Points')
plt.plot(x_range, y_range, label='Interpolation')
plt.legend()
#plt.show()
