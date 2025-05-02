import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from PIL import Image, ImageEnhance

# Load the image
image_path = '110259.jpg'
img = Image.open(image_path)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 8))
plt.subplots_adjust(bottom=0.25)  # Make room for sliders

# Display original image
im_display = ax.imshow(img)
ax.set_title('Interactive Brightness and Saturation Adjustment')
ax.axis('off')

# Create axes for sliders
brightness_ax = plt.axes([0.2, 0.15, 0.65, 0.03])  # [left, bottom, width, height]
saturation_ax = plt.axes([0.2, 0.08, 0.65, 0.03])

# Create sliders
brightness_slider = Slider(brightness_ax, 'Brightness', 0.2, 2.0, valinit=1.0, valstep=0.05)
saturation_slider = Slider(saturation_ax, 'Saturation', 0.0, 2.0, valinit=1.0, valstep=0.05)

# Define update function
def update(val):
    # Get current slider values
    brightness_val = brightness_slider.val
    saturation_val = saturation_slider.val
    
    # Process image
    current_img = img.copy()
    
    # Apply brightness first
    brightness_enhancer = ImageEnhance.Brightness(current_img)
    current_img = brightness_enhancer.enhance(brightness_val)
    
    # Then apply saturation
    saturation_enhancer = ImageEnhance.Color(current_img)
    current_img = saturation_enhancer.enhance(saturation_val)
    
    # Update displayed image
    im_display.set_data(current_img)
    
    # Show values on plot
    ax.set_title(f'Brightness: {brightness_val:.2f}, Saturation: {saturation_val:.2f}')
    fig.canvas.draw_idle()

# Connect sliders to update function
brightness_slider.on_changed(update)
saturation_slider.on_changed(update)

# Add a reset button
reset_ax = plt.axes([0.8, 0.025, 0.1, 0.04])
reset_button = plt.Button(reset_ax, 'Reset')

def reset(event):
    brightness_slider.reset()
    saturation_slider.reset()
reset_button.on_clicked(reset)

# Show image info
status_text = plt.figtext(0.02, 0.025, f"Original size: {img.size}", fontsize=10)

plt.show()

# Save a demo of various combinations as before
# This will execute after the interactive window is closed
fig2, axes = plt.subplots(3, 3, figsize=(15, 15))
plt.subplots_adjust(hspace=0.3)

# Define brightness and saturation levels
brightness_levels = [0.6, 1.0, 1.4]
saturation_levels = [0.3, 1.0, 1.7]

# Generate all combinations
for i, brightness in enumerate(brightness_levels):
    for j, saturation in enumerate(saturation_levels):
        current = img.copy()
        brightness_enhancer = ImageEnhance.Brightness(current)
        current = brightness_enhancer.enhance(brightness)
        
        saturation_enhancer = ImageEnhance.Color(current)
        current = saturation_enhancer.enhance(saturation)
        
        axes[i, j].imshow(current)
        axes[i, j].set_title(f'Brightness: {brightness}, Saturation: {saturation}')
        axes[i, j].axis('off')

plt.suptitle('Grid of Brightness and Saturation Combinations', fontsize=16)
plt.tight_layout()
plt.savefig('brightness_saturation_grid.png')
plt.show()