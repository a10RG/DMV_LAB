import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)

# Create empty line
line, = ax.plot([], [], color="blue")

# Data
x = np.linspace(0, 10, 100)
y = x   # straight line (y = x)

# Animation function
def update(frame):
    line.set_data(x[:frame], y[:frame])  # gradually draw line
    return line,

# Create animation
ani = animation.FuncAnimation(
    fig,
    update,
    frames=len(x),
    interval=50
)
plt.show()
