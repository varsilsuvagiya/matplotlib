import matplotlib.pyplot as plt
import numpy as np

# Example data
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the scatter chart
ax.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='viridis', marker='o', edgecolors='black', linewidth=1, label='Scatter Chart')

# Set chart title and labels
ax.set_title('Scatter Chart Example', fontsize=16)
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)

# Set grid lines
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add legend
ax.legend(loc='upper right', fontsize=10)

# Customize ticks
ax.set_xticks(np.arange(0, 1.1, 0.1))
ax.set_yticks(np.arange(0, 1.1, 0.1))

# Add annotations
ax.annotate('Point', xy=(0.5, 0.5), xytext=(0.5, 0.7),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
