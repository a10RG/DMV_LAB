import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 12)
ax.set_ylim(0, 12)
# Create circle
circle = plt.Circle((0, 8), 0.8, color = 'purple')
ax.add_patch(circle)
# Animation function
def update(frame):
    circle.center = (frame, 6)  # Move circle horizontally
    return circle,
# Create animation
ani = animation.FuncAnimation(
    fig,
    update,
    frames=range(0, 11),
    interval=200
)
plt.show()
