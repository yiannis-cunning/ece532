from PIL import Image

def hex_to_rgb(hex_value):
    """Convert a 24-bit hex value to an (R, G, B) tuple."""
    hex_value = hex_value.strip().lstrip("#")
    return tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))

def text_to_image(text_file, width, height, output_image):
    """Read a text file of hex color values and create a PNG image."""
    with open(text_file, "r") as file:
        hex_values = [line.strip() for line in file.readlines()]
    
    # Ensure the number of pixels matches width * height
    if len(hex_values) != width * height:
        raise ValueError("Incorrect number of pixels for specified dimensions.")
    
    # Create an image
    img = Image.new("RGB", (width, height))
    pixels = [hex_to_rgb(hex_value) for hex_value in hex_values]
    img.putdata(pixels)
    
    # Save the image
    img.save(output_image)
    print(f"Image saved as {output_image}")

# Example usage
text_file = "../dv/ouput_image.mem"  # Replace with your text file path
width, height = 1280, 720  # Set the desired dimensions
output_image = "../dv/output_image.png"
text_to_image(text_file, width, height, output_image)
