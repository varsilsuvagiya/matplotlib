import matplotlib.pyplot as plt
import numpy as np

# Example data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the line chart
ax.plot(x, y, label='Sine Wave', color='blue')

# Set chart title and labels
ax.set_title('Line Chart with Custom Ticks and Limits', fontsize=16)
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)

# Customize ticks
ax.set_xticks(np.arange(0, 11, 1))
ax.set_yticks(np.arange(-1, 1.1, 0.5))

# Set axis limits
ax.set_xlim([0, 10])
ax.set_ylim([-1, 1])

# Customize axis
ax.axis('tight')  # Adjust axis to fit data tightly

# Add legend
ax.legend(loc='upper right', fontsize=10)

# Show plot
plt.show()

