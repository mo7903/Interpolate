import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Load the data
data = {}

with open("cs448b_ipasn.csv") as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        data.update({float(row["Bytes"]): float(row["Time"])})

X = sorted(data.keys())
Y = [data[k] for k in X]

# Smooth the data using a moving average filter
window_size = 51
Y_smooth = np.convolve(Y, np.ones(window_size)/window_size, mode='same')

# Fit a cubic spline to the smoothed data
cs = CubicSpline(X, Y_smooth)

# Interpolate the data using the cubic spline
targets = np.linspace(np.min(X), np.max(X), num=len(X)*10)
Y_cubic = cs(targets)

# Plot the original data
fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
ax.plot(X, Y, 'o', label='Data', markersize=2)

# Add labels and title
ax.set_xlabel('Time')
ax.set_ylabel('Bytes')
ax.set_title('Network Traffic')

# Increase linewidth and add legend
ax.legend(fontsize=12, loc='best')
ax.tick_params(axis='both', labelsize=12)
plt.tight_layout()

# Show the plot
plt.show()

# Plot the smoothed and interpolated data
fig, ax = plt.subplots(figsize=(10, 6), dpi=100)

ax.set_ylim([0, 300])
#ax.plot(X, Y, 'o', label='Data', markersize=2)
ax.plot(X, Y_smooth, label='Smoothed', linewidth=2)
ax.plot(targets, Y_cubic, label='Cubic Spline', linewidth=2)

# Add labels and title
ax.set_xlabel('Time')
ax.set_ylabel('Bytes')
ax.set_title('Network Traffic (Smoothed and Interpolated)')

# Increase linewidth and add legend
ax.legend(fontsize=12, loc='best')
ax.tick_params(axis='both', labelsize=12)
plt.tight_layout()

# Show the plot
plt.show()
