import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
# Create a figure of size 8x6 inches, 80 dots per inch
my_dpi = 96
ax1 =plt.figure(figsize=(20, 10), dpi=my_dpi)

# Create a new subplot from a grid of 1x1
ax1 = plt.subplot(1, 1, 1)


ax1.add_patch(
    patches.Rectangle(
        (0.1, 0.1),   # (x,y)
        0.5,          # width
        0.5,          # height
    	facecolor='black'
    )
)

# Save figure using 72 dots per inch
# plt.savefig("exercice_2.png", dpi=72)

# Show result on screen
plt.show()
# plt.savefig('my_fig.png', dpi=my_dpi)
