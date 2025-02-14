import matplotlib.pyplot as plt
import numpy as np

# Example data
x = np.arange(5)
y = np.array([3, 5, 7, 9, 11])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the bar chart
ax.bar(x, y, width=0.8, align='center', color='blue', edgecolor='black', hatch='/', label='Bar Chart')

# Set chart title and labels
ax.set_title('Bar Chart Example', fontsize=16)
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)

# Set grid lines
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add legend
ax.legend(loc='upper right', fontsize=10)

# Customize ticks
ax.set_xticks(x)
ax.set_xticklabels(['A', 'B', 'C', 'D', 'E'])

# Customize axis
ax.set_ylim([0, 12])

# Add annotations
for i, j in zip(x, y):
    ax.annotate(str(j), xy=(i, j), xytext=(0, 3),
                textcoords='offset points', ha='center', va='bottom',
                fontsize=10)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
