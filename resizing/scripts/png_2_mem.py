from PIL import Image

def print_pixel_values(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Convert image to RGB mode (in case it's not)
    img = img.convert("RGB")
    
    # Get image dimensions
    width, height = img.size
    
    # Loop through each pixel
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            print(f"Pixel ({x}, {y}): R={r}, G={g}, B={b}")

# Example usage
image_path = "your_image.png"  # Replace with your PNG file path
print_pixel_values(image_path)
