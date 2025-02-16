import matplotlib.pyplot as plt
import numpy as np

# Example data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the fill between
ax.fill_between(x, y1, y2, where=(y1 > y2), color='blue', alpha=0.3, label='y1 > y2')
ax.fill_between(x, y1, y2, where=(y1 <= y2), color='red', alpha=0.3, label='y1 <= y2')

# Plot the lines
ax.plot(x, y1, color='blue', label='y1 = sin(x)')
ax.plot(x, y2, color='red', label='y2 = cos(x)')

# Set chart title and labels
ax.set_title('Fill Between Example', fontsize=16)
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)

# Add legend
ax.legend(loc='upper right', fontsize=10)

# Set grid lines
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()

