import sys
import PIL.Image

# ASCII characters used to render the image (from dark to light)
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    """
    Resizes the image maintaining the aspect ratio.
    """
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    """
    Converts the image to grayscale.
    """
    return image.convert("L")

def pixels_to_ascii(image):
    """
    Maps pixels to ASCII characters based on intensity.
    """
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters

def convert_image_to_ascii(image_path, new_width=100):
    try:
        image = PIL.Image.open(image_path)
    except Exception as e:
        print(f"Error: Unable to open image file '{image_path}'. Check the path!")
        return

    # Process the image
    try:
        new_image_data = pixels_to_ascii(grayify(resize_image(image, new_width)))
    except Exception as e:
        print(f"Error processing image: {e}")
        return

    # Format the output
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    print("\n" + "="*20 + " RESULT " + "="*20 + "\n")
    print(ascii_image)
    print("\n" + "="*48 + "\n")

if __name__ == "__main__":
    # Default width if not specified
    current_width = 100
    path = ""

    # Handle arguments
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = input("Enter the path to the image file: ")

    # Check for optional width argument
    if len(sys.argv) > 2:
        try:
            current_width = int(sys.argv[2])
        except ValueError:
            print("Warning: Width must be a number. Using default (100).")

    convert_image_to_ascii(path, current_width)
