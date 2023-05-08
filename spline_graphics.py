import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import Rbf

# Load data from CSV file
data = pd.read_csv('data.csv')
x = data['x']
y = data['y']
z = data['z']

# Create a 3D scatter plot of the input data
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='b', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

# Set up the radial basis function interpolation
rbf = Rbf(x, y, z, function='thin-plate')

# Generate a grid of points for the spline interpolation
xi, yi = np.meshgrid(np.linspace(min(x), max(x), 100), np.linspace(min(y), max(y), 100))
zi = rbf(xi, yi)

# Create a 3D surface plot of the spline interpolation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xi, yi, zi, cmap='coolwarm')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()