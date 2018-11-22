# Using masks for Image.composite
import numpy as np
from PIL import Image, ImageChops


def main():
    # Open Lenna
    lenna = Image.open('../lenna.png')
    lenna.show('Lenna')

    # Open Lenna's mask, convert it to binary
    lenna_mask = Image.open('../lenna_mask.png').convert('1')
    lenna_mask.show('Lenna\'s mask')

    # Create a darker second image with one channel - grayscale
    shape = (lenna.size[1], lenna.size[0])
    second_image_array = np.ones(shape, dtype=np.uint8) * 100
    second_image = Image.fromarray(second_image_array)

    # Split channels
    red, green, blue = lenna.split()
    # Decrease the intensity of the red channel
    subtracted_red = ImageChops.subtract(red, second_image)

    # Create new image with the decreased red channel
    lenna_nored = Image.merge('RGB', (subtracted_red, green, blue))
    lenna_nored.show('Lenna with decreased red channel')

    # Image.composite creates a composite of two images using a given mask.
    # Where the mask has white color, the first image is copied as is,
    # otherwise the values of the second image are preserved.
    new_image = Image.composite(lenna_nored, lenna, lenna_mask)
    new_image.show('New image')

if __name__ == '__main__':
    main()
