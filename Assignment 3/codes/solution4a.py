import matplotlib.pyplot as plt

# Define the points of the polygon
points = [(1, 2), (3, 1), (1, 0), (0, 0), (1, 2)]  # Closing the polygon

# Extract x and y coordinates
x, y = zip(*points)

# Plot the polygon
plt.fill(x, y, "b", alpha=0.2, label="Capacity Region")

# Set axis labels and limits
plt.xlabel("R1 (packets/sec)")
plt.ylabel("R2 (packets/sec)")
plt.xlim(0, 4)
plt.ylim(0, 3)

# Add points to the plot for clarity
plt.plot(x, y, "ro")  # red dots for the vertices

# Add labels for the points
for i, txt in enumerate(points):
    plt.annotate(
        txt, (x[i], y[i]), textcoords="offset points", xytext=(0, 10), ha="center"
    )

# Show legend
plt.legend()

# Show the grid
plt.grid()

# Save the plot
plt.tight_layout()
plt.savefig("solution4a.png")
