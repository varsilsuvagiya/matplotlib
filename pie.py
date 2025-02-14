import matplotlib.pyplot as plt

# Example data
labels = 'Python', 'C++', 'Ruby', 'Java', 'PHP'
sizes = [215, 130, 245, 210, 120]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
explode = (0.1, 0, 0, 0, 0)  # explode 1st slice

# Plot
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=140, colors=colors)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Set chart title and labels
plt.title('Pie Chart Example', fontsize=16)

# Add legend
plt.legend(loc='upper right', fontsize=10)

# Customize ticks
plt.xticks()

# Customize axis
plt.axis('off')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
