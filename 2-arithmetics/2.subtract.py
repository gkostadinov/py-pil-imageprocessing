# Subtract two images
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

    # ImageChops.subtract clips the pixel intensity if it is below 0
    # E.g. image 1 has a pixel with intensity 200
    #      image 2 has a pixel with intensity 100
    #      100 - 200 = -100
    # However images are represented by 8-bit unsigned integers with numbers
    # ranging [0-255], so the values are clipped at 0
    # and 100 - 200 = 0, not -100
    subtract_image = ImageChops.subtract(image, second_image)
    subtract_image.show('Subtract')

    # ImageChops.subtract_modulo on the other side does not clip the result
    # Using the example above it does the following:
    # (100 - 200) = x mod 256 or (100 - 200) % 256
    # So in our case the new value will be: (100 - 200) % 256 = 156
    subtract_modulo_image = ImageChops.subtract_modulo(image, second_image)
    subtract_modulo_image.show('Subtract modulo')
