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
            str_r = "0x"
            str_r += hex(r >> 4)[2::] + hex(r & 0xf)[2::]           
            str_r += hex(g >> 4)[2::] + hex(r & 0xf)[2::]           
            str_r += hex(b >> 4)[2::] + hex(r & 0xf)[2::]           
            print(str_r)

# Example usage
image_path = "../dv/input_image.png"  # Replace with your PNG file path
print_pixel_values(image_path)
