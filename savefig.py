import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots()

# Plot something
ax.plot([1, 2, 3])

# Save the figure
plt.savefig('example.png', dpi=300, bbox_inches='tight')
