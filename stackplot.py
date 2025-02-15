import matplotlib.pyplot as plt
import numpy as np

# Example data
N = 60
y1 = np.random.rand(N)
y2 = np.random.rand(N)
y3 = np.random.rand(N)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the stack plot
ax.stackplot(np.arange(N), [y1, y2, y3], labels=['Y1', 'Y2', 'Y3'], colors=['blue', 'red', 'green'])

# Set chart title and labels
ax.set_title('Stack Plot Example', fontsize=16)
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)

# Add legend
ax.legend(loc='upper right', fontsize=10)

# Customize ticks
ax.set_xticks(np.arange(0, N, 10))
ax.set_yticks(np.arange(0, 1.1, 0.2))

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
