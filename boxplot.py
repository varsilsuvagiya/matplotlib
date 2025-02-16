import matplotlib.pyplot as plt
import numpy as np
# Example data
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the box plot
ax.boxplot(data, vert=True, patch_artist=True)

# Set chart title and labels
ax.set_title('Box Plot Example', fontsize=16)
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)

# Customize ticks
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(['x1', 'x2', 'x3'])

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
