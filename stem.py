import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 2 * np.pi, 10)
y = np.sin(x)

# Create the stem chart
plt.stem(x, y, basefmt=" ", linefmt='b-', markerfmt='ro')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Stem Chart Example')

# Show the plot
plt.grid(True)
plt.show()
