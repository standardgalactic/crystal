#!/usr/bin/python3

from PIL import Image, ImageDraw

# Define the size of the icon
ICON_SIZE = 64

# Create a new image with a transparent background
image = Image.new("RGBA", (ICON_SIZE, ICON_SIZE), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Define the points of the crystal
points = [
    (32, 4),   # Top vertex
    (48, 16),  # Top-right vertex
    (56, 40),  # Bottom-right vertex
    (32, 60),  # Bottom vertex
    (8, 40),   # Bottom-left vertex
    (16, 16)   # Top-left vertex
]

# Draw the crystal shape with blue color
draw.polygon(points, fill=(0, 191, 255), outline=(0, 0, 255))

# Draw the facets with white color
draw.line([points[0], points[2]], fill=(255, 255, 255), width=2)
draw.line([points[0], points[4]], fill=(255, 255, 255), width=2)
draw.line([points[1], points[3]], fill=(255, 255, 255), width=2)
draw.line([points[5], points[3]], fill=(255, 255, 255), width=2)

# Save the icon as a .ico file
image.save("favicon.ico")
