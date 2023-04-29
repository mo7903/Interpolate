import numpy as np
import matplotlib.pyplot as plt
from methods import *
from scipy.interpolate import pchip_interpolate
from prettytable import PrettyTable as pt

# Define the function to be interpolated
f = lambda x: np.sin(x)

# Define the range of x values
X = np.linspace(1, 10, 100)

# Compute the true function values
Y = [f(x) for x in X]

# Define the range of target x values to be interpolated
targets = np.linspace(2, 4, 50)

# Compute the values using the interpolation methods
Y_true = [f(x) for x in targets]
Y_newton_forward = [newton_forward(X, Y)(x) for x in targets]
Y_newton_backward = [newton_backward(X, Y)(x) for x in targets]
Y_pchip = [pchip_interpolate(X, Y, x) for x in targets]
Y_stirling = [stirling_interpolation(X, Y, x) for x in targets]
Y_everett = [everett_interpolation(X, Y, x) for x in targets]


# Create a table to display the results
results = pt(["x", "True Value", "Newton's Forward", "Newton's Backward", "PCHIP", "Everett", "Stirling"])

for i in range(len(targets)):
    results.add_row([targets[i], Y_true[i], Y_newton_forward[i], Y_newton_backward[i], Y_pchip[i], Y_everett[i], Y_stirling[i]])

# Print the results table
print(results)

# Plot the true function and the interpolated functions on separate graphs
plt.figure(figsize=(8, 6))
plt.plot(X, Y, label='True Function')
plt.plot(targets, Y_newton_forward, label="Newton's Forward Interpolation")
plt.legend()
plt.title("Newton's Forward Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# Plot the true function and the interpolated functions on separate graphs
plt.figure(figsize=(8, 6))
plt.plot(X, Y, label='True Function')
plt.plot(targets[40:], Y_newton_backward[40:], label="Newton's Backward Interpolation")
plt.legend()
plt.title("Newton's Backward Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(X, Y, label='True Function')
plt.plot(targets, Y_pchip, label='PCHIP Interpolation')
plt.legend()
plt.title('PCHIP Interpolation')
plt.xlabel("x")
plt.ylabel("y")
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(X, Y, label='True Function')
plt.plot(targets, Y_everett, label="Everett's Interpolation")
plt.legend()
plt.title("Everett's Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(X, Y, label='True Function')
plt.plot(targets, Y_stirling, label="Stirling's Interpolation")
plt.legend()
plt.title("Stirling's Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.show()