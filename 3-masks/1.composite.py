# Using masks for Image.composite
import numpy as np
from PIL import Image, ImageChops


def main():
    # Create a sample mask
    image = Image.open('../lenna.png')
    image.show('Original')

    # Create a sample mask
    image1 = Image.new('1', image.size, color=1).rotate(60)
    image2 = Image.new('1', image.size, color=1).rotate(30)
    sample_mask = ImageChops.logical_and(image1, image2)
    sample_mask.show('Mask')

    # Create a darker second image
    shape = (image.size[1], image.size[0], 3)
    second_image_array = np.ones(shape, dtype=np.uint8) * 100
    second_image = Image.fromarray(second_image_array)

    # Image.composite creates a composite of two images using a given mask.
    # Where the mask has white color, the first image is copied as is,
    # otherwise the values of the second image are preserved.
    new_image = Image.composite(image, second_image, sample_mask)
    new_image.show('New image')

if __name__ == '__main__':
    main()
