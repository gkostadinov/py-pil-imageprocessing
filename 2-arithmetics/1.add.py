# Add two images
import numpy as np
from PIL import Image, ImageChops

if __name__ == '__main__':
    image = Image.open('../lenna.png')
    image.show('Original')

    # Array size is inverted image size
    shape = (image.size[1], image.size[0], 3)

    # Create an image using numpy
    # Generate an array of ones and multiply all values by 100
    # This creates a grey-coloured image (all pixel values are (100, 100, 100))
    second_image_array = np.ones(shape, dtype=np.uint8) * 100
    second_image = Image.fromarray(second_image_array)

    # ImageChops.add clips the pixel intensity if it is above 255
    # E.g. image 1 has a pixel with intensity 200
    #      image 2 has a pixel with intensity 100
    #      100 + 200 = 300
    # However images are represented by 8-bit unsigned integers with numbers
    # ranging [0-255], so the values cap at 255 and 100 + 200 = 255, not 300
    add_image = ImageChops.add(image, second_image)
    add_image.show('Add')

    # ImageChops.add_modulo on the other side does not clip the result
    # Using the example above it does the following:
    # (100 + 200) = x mod 256 or (100 + 200) % 256
    # So in our case the new value will be: (100 + 200) % 256 = 44
    add_modulo_image = ImageChops.add_modulo(image, second_image)
    add_modulo_image.show('Add modulo')
