import matplotlib.pyplot as plt
import numpy as np

# Example data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the line chart
ax.plot(x, y, label='Sine Wave', color='blue', linestyle='-', linewidth=2, marker='o', markerfacecolor='red', markersize=5)

# Set chart title and labels
ax.set_title('Line Chart Example', fontsize=16)
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)

# Set grid lines
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add legend
ax.legend(loc='upper right', fontsize=10)

# Customize ticks
ax.set_xticks(np.arange(0, 11, 1))
ax.set_yticks(np.arange(-1, 1.1, 0.5))

# Add annotations
ax.annotate('Local Max', xy=(np.pi/2, 1), xytext=(np.pi/2 + 1, 1.2),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()

